from ollama_model import get_chat_model
from langchain_core.prompts import ChatPromptTemplate

def main():
    # Initialize the Ollama LLM
    ollama = get_chat_model(model_name="gemma3:1b", port=8085)

    url = str(input("Enter the URL to summarize: ")).strip()
    # Example prompt
    user_msg = "Summarize the given site {url}"
    sytem_msg = "You are a helpful assistant that summarizes the content of a URL."

    # Create a chat prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", sytem_msg),
        ("user", user_msg)
    ]).format(url=url)

    response = ollama.invoke(prompt)
    print(response)
    
if __name__ == "__main__":
    main()