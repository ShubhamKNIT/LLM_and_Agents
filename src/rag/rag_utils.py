import re
import json
from PyPDF2 import PdfReader, PdfWriter
from langchain_docling.loader import DoclingLoader, ExportType

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

def pdf_to_mark

def sanitize_filename(name: str) -> str:
    # Remove invalid filename characters
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    # Replace multiple spaces with single space
    name = re.sub(r'\s+', ' ', name).strip()
    return name