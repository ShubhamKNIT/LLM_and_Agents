from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent))

import os
import json
from rag.rag_utils import (
    slice_pdf,
    sanitize_filename
)

def read_toc(toc_json_path):
    with open(toc_json_path, "r") as f:
        toc = json.load(f)
    return toc

def split_chapterwise(toc_json_path, page_offset, input_pdf_path, chapter_dir):
    toc = read_toc(toc_json_path)

    page_li = list()
    title_li = list()
    for title, page_num in toc.items():
        title_li.append(title)
        page_li.append(page_offset + page_num)

    os.makedirs(chapter_dir, exist_ok=True)
    
    for i in range(0, len(page_li) - 1):
        start_page_num = page_li[i]
        end_page_num = page_li[i + 1] - 1
        title = title_li[i]
        title = sanitize_filename(title)
        print(f"Processing chapter: {title} (Pages: {start_page_num} to {end_page_num})")

        chapter_path = f"{chapter_dir}/{title}.pdf"

        slice_pdf(input_pdf_path, chapter_path, start_page_num, end_page_num)

# if __name__ == "__main__":
#     toc_json_path = "./rag/DGI-INN_TOC_Processed.json"
#     page_offset = 9  # Change to your desired page offset
#     input_pdf_path = "./rag/DGI-INN.pdf"
#     chapter_dir = "./rag/Chapters"

#     split_chapterwise(toc_json_path, page_offset, input_pdf_path, chapter_dir)


