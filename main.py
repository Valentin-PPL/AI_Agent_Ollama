from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage

def main():
    model = ChatOllama(
        model="llama3",
        temperature=0
    )
    print("Welcome! I'm your AI assistant. Type 'quit' to exit.\n"
          "You can ask me to perform calculations or chat with me")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        if not user_input:
            continue

        print("\nAssistant: ", end="", flush=True)

        messages = [HumanMessage(content=user_input)]

        for chunk in model.stream(messages):
            if chunk.content:
                print(chunk.content, end="", flush=True)

        print()  # newline la final

if __name__ == "__main__":
    main()