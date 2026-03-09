from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

from utils.ollama_model import get_chat_model
from rag.prompts import get_toc_prompt
from langchain_core.prompts import ChatPromptTemplate
from rag.rag_utils import (
    extract_json,
    roman_to_int
)
import json

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
    for title, page_number in toc.items():
        print(title, " ", page_number)
        if page_number.isalpha():
            page_num = roman_to_int(str(page_number).strip())
            offset = page_num
        elif page_number.isdigit():
            page_num = offset + int(str(page_number).strip())
        else:
            raise ValueError(f"Invalid page number format: {page_number}")
        processed_toc[title] = page_num
        
    with open(toc_processed_json_path, "w") as f:
        json.dump(processed_toc, f, indent=4)

# if __name__ == "__main__":
#     input_pdf_path = "./rag/DGI-INN.pdf"
#     output_pdf_path = "./rag/DGI-INN_TOC.pdf"
#     toc_txt_path = "./rag/DGI-INN_TOC.txt"
#     toc_json_path = "./rag/DGI-INN_TOC.json"
#     toc_processed_json_path = "./rag/DGI-INN_TOC_Processed.json"
#     start_page = 8  # Change to your desired start page_number
#     end_page = 9   # Change to your desired end page_number
    
#     slice_pdf(input_pdf_path, output_pdf_path, start_page, end_page)
#     pdf_to_txt(output_pdf_path, output_txt_path=toc_txt_path)
#     get_toc(toc_txt_path, toc_json_path, model_name="deepseek-r1:8b", port=11434)
#     post_process_toc(toc_json_path, toc_processed_json_path)