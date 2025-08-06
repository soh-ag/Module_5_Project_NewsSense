import logfire_setup
from agents.conversation import ConversationAgent
import sys
import io

# Set the console encoding to UTF-8 (cross-platform safe)
if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

def main():
    agent = ConversationAgent("trading_agent", "fact_checker", "summarizer_agent")

    while True:
        user_input = input("🧠 You: ")

        if user_input.lower() in {"exit", "quit"}:
            print("👋 Goodbye!")
            break

        response = agent.handle(user_input)
        print("🤖 NewsSense:", response)


if __name__ == "__main__":
    main()
