from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parent.parent.parent))

from langchain_core.prompts import ChatPromptTemplate
from rag.prompts import get_summarization_prompt
from utils.ollama_model import get_chat_model
from rag.rag_utils import (
    pdf_to_txt,
    extract_json
)

def summarize_text(pdf_path):

    pdf_to_txt(pdf_path, "./rag/temp.txt")
    with open("./rag/temp.txt", "r") as f:
        texts = f.read()

    system_prompt = get_summarization_prompt()
    user_prompt = "Summarize the following text:\n\n{texts}"

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", user_prompt)
    ]).format_messages(texts=texts)

    model = get_chat_model(model_name="llama3.2:latest", port=11434)
    response = model.invoke(prompt)

    summary = extract_json(response.content)
    return summary

if __name__ == "__main__":
    pdf_path = "./rag/Chapters/Macronutrients, Page = 89.pdf"
    print(summarize_text(pdf_path))