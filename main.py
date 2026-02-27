from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

def main():
    # Initialize the Ollama LLM
    ollama = ChatOllama(
        model="gemma3:1b",
        base_url="http://localhost:8085",
        timeout=10
    )

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