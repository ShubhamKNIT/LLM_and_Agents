from utils.ollama_model import get_chat_model
from langchain_core.prompts import ChatPromptTemplate

def get_sytem_prompt(task_description):

    model = get_chat_model("gemma3:1b")
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant that generates system prompts in markdown format to guide model behaviour."),
        ("user", "{task_description}")
    ])

    chain = prompt | model
    response = chain.invoke({"task_description": task_description})
    return response.content