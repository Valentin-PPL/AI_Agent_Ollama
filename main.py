from agent.agent import ask_llm

def main():

    print("Welcome! I'm your AI assistant. Type 'quit' to exit.\n"
          "You can ask me to perform calculations or chat with me")

    while True:
        user_input = input("\nYou: ").strip()

        if user_input == "quit":
            break

        if not user_input:
            continue

        print("\nAssistant: ", end="", flush=True)
        ask_llm(user_input)

if __name__ == "__main__":
    main()