print("=== Chatbot Started ===")

while True:
    user_input = input("You: ").lower().strip()

    if user_input == "hi" or user_input == "hello":
        print("Bot: Hello! I'm your assistant.")

    elif user_input == "bye" or user_input == "exit" or user_input == "goodbye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I don't understand that yet. Try saying 'hi' or 'exit'.")