from langchain_ollama import ChatOllama, OllamaEmbeddings

def get_chat_model(model_name: str = "gemma3:1b", port: int = 8085) -> ChatOllama:

    return ChatOllama(
        model=model_name,
        base_url=f"http://localhost:{port}",
        timeout=10,
        max_tokens=2048
    )
    
def get_embedding_model(model_name: str = "nomic-embed-text-v2-moe:latest", port: int = 8085) -> OllamaEmbeddings:

    return OllamaEmbeddings(
        model=model_name,
        base_url=f"http://localhost:{port}"
    )