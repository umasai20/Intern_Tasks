def chatbot():
    print("Hello! I’m ChatBot. Type something to start talking (type 'bye' to end).")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("ChatBot: Hi!")
        elif user == "how are you":
            print("ChatBot: I'm fine, thank you!")
        elif user == "thank you":
            print("ChatBot: You're welcome!")
        elif user == "bye":
            print("ChatBot: Goodbye!")
            break
        else:
            print("ChatBot: I didn’t understand that.")

chatbot()