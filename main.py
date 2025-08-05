from agents.conversation import ConversationAgent


def main():
    agent = ConversationAgent()

    while True:
        user_input = input("🧠 You: ")

        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break

        response = agent.handle(user_input)
        print("🤖 NewsSense:", response)


if __name__ == "__main__":
    main()
