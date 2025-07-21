
def chatbot():
    print("Chatbot: Hello! You can talk to me. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi! How can i help you?")
        elif user_input == "how are you":
            print("Chatbot: I'm doing great, thanks! what about you?")
        elif user_input == "Can you clear my doubts?":
            print("Chatbot: yes i can ! Dont feel shy about asking any kind of doubts.")
        elif user_input == "Good morning":
            print("Chatbot: Very Good Morning , Have a great day !")
        elif user_input == "who created you":
            print("Chatbot: I was created by a Python programmer.")
        elif user_input == "what can you do":
            print("Chatbot: I can respond to simple messages!")
        elif user_input == "bye":
            print("Chatbot: bye! Have a great day!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand , Ask again .")

chatbot()
