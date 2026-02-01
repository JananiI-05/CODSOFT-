print("Rule-Based Chatbot")
print("Type 'bye' to exit\n")

while True:
    user_input = input("You: ").lower()

    if user_input == "bye":
        print("Bot: Goodbye! Have a nice day 😊")
        break

    elif user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif "your name" in user_input:
        print("Bot: I am a rule-based chatbot created using Python.")

    elif "how are you" in user_input:
        print("Bot: I'm doing great! Thanks for asking.")

    elif "help" in user_input:
        print("Bot: I can answer simple questions like greetings, name, and time.")

    elif "time" in user_input:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    else:
        print("Bot: Sorry, I didn't understand that.")
