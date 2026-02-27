from ollama_model import get_embedding_model

def main():
    # Initialize the Ollama LLM
    ollama = get_embedding_model(model_name="nomic-embed-text-v2-moe:latest", port=8085)
    text = str(input("Enter the text to tokenize: ")).strip()
    response = ollama.embed_query(text)
    print(response)

if __name__ == "__main__":
    main()