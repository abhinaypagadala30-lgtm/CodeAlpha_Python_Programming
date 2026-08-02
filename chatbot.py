def basic_chatbot():
    print("🤖 Chatbot: Hello! I am your basic rule-based chatbot. How can I help you?")
    print("(Note: Type 'bye' or 'goodbye' to exit the conversation)\n")

    # Loop for continuous chatting
    while True:
        user_input = input("👤 You: ").lower().strip()

        # If-elif-else logic for handling predefined inputs
        if user_input in ["bye", "goodbye"]:
            print("🤖 Chatbot: Goodbye! Have a wonderful day!")
            break
        elif "hello" in user_input or "hi" in user_input:
            print("🤖 Chatbot: Hi there! How are you doing today?")
        elif "how are you" in user_input:
            print("🤖 Chatbot: I am doing fine, thank you! How about you?")
        elif "your name" in user_input:
            print("🤖 Chatbot: My name is Alpha Bot, built with Python.")
        elif "what can you do" in user_input:
            print("🤖 Chatbot: I can chat with you and respond to basic text commands.")
        else:
            print("🤖 Chatbot: Sorry, I didn't quite get that. Try asking 'hi' or 'how are you'.")

if __name__ == "__main__":
    basic_chatbot()
