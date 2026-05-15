print("Welcome to CodeAlpha Chatbot")

while True:
    user = input("You: ").lower()

    if user == "hello":
        print("Bot: Hi!")

    elif user == "how are you":
        print("Bot: I am fine, thanks!")

    elif user == "bye":
        print("Bot: Goodbye!")
        break
    elif user == "what is your name":
        print("Bot: I am CodeAlpha Bot!")


    else:
        print("Bot: Sorry, I don't understand.")