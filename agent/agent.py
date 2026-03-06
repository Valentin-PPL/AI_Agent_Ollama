from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage

model = ChatOllama(
    model="llama3",
    temperature=0
)

def ask_llm(prompt: str):
    messages = [HumanMessage(content=prompt)]

    for chunk in model.stream(messages):
        if chunk.content:
            print(chunk.content, end="", flush=True)

    print()