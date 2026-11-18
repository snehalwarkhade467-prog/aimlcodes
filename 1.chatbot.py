from datetime import datetime

print("================================")
print(" Welcome to Smart Chatbot!")
print("================================")
print("(Type bye to exit)")
print("================================")

while True:
    user = input("\nYou: ").lower()

    if user == "hi" or user == "hello" or user == "hey":
        print("Bot: Hello! Nice to meet you.")

    elif user == "name":
        print("Bot: I am SmartBot, your AI assistant.")

    elif user == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user == "time":
        print("Bot: Current time is", datetime.now().strftime("%H:%M:%S"))

    elif user == "date":
        print("Bot: Today's date is", datetime.now().strftime("%d-%m-%Y"))

    elif user == "python":
        print("Bot: Python is a popular programming language used in AI.")

    elif user == "ai":
        print("Bot: Artificial Intelligence enables machines to perform tasks that normally require human intelligence.")

    elif user == "thank you":
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day!")
        break

    else:
        print("Bot: Sorry, I don't understand your question.")