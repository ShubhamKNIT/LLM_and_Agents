from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from PyPDF2 import PdfReader, PdfWriter
from utils.ollama_model import get_chat_model
from utils.pretty_print import pretty_print
from rag.prompts import get_toc_prompt
from langchain_core.prompts import ChatPromptTemplate
from langchain_docling.loader import DoclingLoader, ExportType
from langchain.tools import tool
import json
import re

def extract_json(output_text):
    try:
        return json.loads(output_text)
    except json.JSONDecodeError:
        match = re.search(r'(\{.*\}|\[.*\])', output_text, re.DOTALL)
        if not match:
            raise ValueError("No JSON found in output")
        return json.loads(match.group(1))
    
def roman_to_int(s):
    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0

    for char in s.upper():
        if char not in roman_numerals:
            raise ValueError(f"Invalid Roman numeral: {char}")
        value = roman_numerals[char]
        if prev_value < value:
            total += value - 2 * prev_value
        else:
            total += value
        prev_value = value

    return total

def slice_pdf(input_pdf_path, output_pdf_path, start_page, end_page):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page_num in range(start_page - 1, end_page):
        writer.add_page(reader.pages[page_num])

    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)

    print(f"Saved pages {start_page} to {end_page} from {input_pdf_path} to {output_pdf_path}")

def pdf_to_txt(input_pdf, output_txt_path):
    loader = DoclingLoader(input_pdf, export_type=ExportType.DOC_CHUNKS)
    document = loader.load()
    
    with open(output_txt_path, "w") as f:
        for doc in document:
            content = doc.page_content
            parsed_content = content.split("CONTENTS")
            
            # Write only the part after "CONTENTS"
            f.write(parsed_content[-1].strip() + "\n") 

    print(f"Extracted text from {input_pdf} and saved to {output_txt_path}")

def get_toc(input_txt_path, output_json_path, model_name="gemma3:4b", port=8085):
    toc = ""
    with open(input_txt_path, "r") as f:
        toc = f.read()

    prompt = ChatPromptTemplate.from_messages([
        ("system", get_toc_prompt()),
        ("user", "Extract the TOC from the following PDF:\n\n{text}")
    ])

    # Format prompt as a string (or messages if your model supports chat)
    formatted_prompt = prompt.format(text=toc)
    # pretty_print(formatted_prompt)

    # Invoke model with formatted string
    model = get_chat_model(model_name=model_name, port=port)
    response = model.invoke(formatted_prompt)
    
    print("Extracted TOC:")
    extracted_toc = extract_json(response.content)

    with open(output_json_path, "w") as f:
        json.dump(extracted_toc, f, indent=4)

def post_process_toc(toc_json_path, toc_processed_json_path):
    with open(toc_json_path, "r") as f:
        toc = json.load(f)

    processed_toc = {}

    offset = 0
    for title, page in toc.items():
        # print(title, " ", page)
        if page.isalpha():
            page_num = roman_to_int(str(page).strip())
            offset = page_num
        else:
            page_num = offset + int(page)
        processed_toc[title] = page_num
        
    with open(toc_processed_json_path, "w") as f:
        json.dump(processed_toc, f, indent=4)

if __name__ == "__main__":
    input_pdf_path = "./rag/DGI-INN.pdf"
    output_pdf_path = "./rag/DGI-INN_TOC.pdf"
    toc_txt_path = "./rag/DGI-INN_TOC.txt"
    toc_json_path = "./rag/DGI-INN_TOC.json"
    toc_processed_json_path = "./rag/DGI-INN_TOC_Processed.json"
    start_page = 8  # Change to your desired start page
    end_page = 9   # Change to your desired end page
    
    slice_pdf(input_pdf_path, output_pdf_path, start_page, end_page)
    pdf_to_txt(output_pdf_path, output_txt_path=toc_txt_path)
    get_toc(toc_txt_path, toc_json_path, model_name="deepseek-r1:8b", port=11434)
    post_process_toc(toc_json_path, toc_processed_json_path)