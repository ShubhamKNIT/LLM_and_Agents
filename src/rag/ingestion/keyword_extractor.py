from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))

from utils.ollama_model import get_chat_model
from rag.prompts import get_keyword_extraction_prompt
from langchain_core.prompts import ChatPromptTemplate
from rag.rag_utils import (
    pdf_to_txt,
    extract_json
)

def extract_keywords(pdf_path):
    pdf_to_txt(pdf_path, "./rag/temp.txt")

    with open("./rag/temp.txt", "r") as f:
        texts = f.read()

    model = get_chat_model(model_name="llama3.2:latest", port=11434)
    system_prompt = get_keyword_extraction_prompt()
    user_prompt = "Extract headings from the following text:\n\n{texts}"

    # print(texts)

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", user_prompt)
    ]).format_messages(texts=texts)
    
    response = model.invoke(prompt)
    keywords = extract_json(response.content)
    return keywords


if __name__ == "__main__":
    pdf_path = "./rag/Chapters/Macronutrients, Page = 89.pdf"
    print(extract_keywords(pdf_path))