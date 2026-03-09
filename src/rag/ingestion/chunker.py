from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))

from rag.rag_utils import pdf_to_txt
from langchain_text_splitters import CharacterTextSplitter

def pdf_chunk_generator(pdf_path):
    pdf_to_txt(pdf_path, "./rag/temp.txt")
    with open("./rag/temp.txt", "r") as f:
        texts = f.read()

    # Split the text into chunks based on "CONTENTS"
    chunks = texts.split("CONTENTS")
    
    # Yield each chunk after stripping leading/trailing whitespace
    for chunk in chunks:
        yield chunk.strip()

def text_chunk_generator(text):
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )

    yield text_splitter.create_documents([text])


if __name__ == "__main__":
    # pdf_path = "./rag/Chapters/Macronutrients, Page = 89.pdf"
    # for chunk in pdf_chunk_generator(pdf_path):
    #     print("Chunk:")
    #     print(chunk)
    #     print("-" * 40)

    txt_path = "./rag/temp.txt"
    with open(txt_path, "r") as f:
        text = f.read()
        text = text.replace("\n", " ")

    for chunk in text_chunk_generator(text):
        print("Chunk:")
        print(chunk)
        print("-" * 40)