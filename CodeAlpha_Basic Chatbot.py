# --- Function to get chatbot response ---
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hi there! "
    elif "how are you" in user_input:
        return "I'm fine, thanks for asking! "
    elif "what is your name" in user_input:
        return "I'm your friendly chatbot "
    elif "thank" in user_input:
        return "You're welcome! "
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day! "
    else:
        return "Sorry, I didn’t understand that. Can you rephrase?"

# --- Main chatbot loop ---
print(" Chatbot: Hello! Type 'bye' to exit.\n")

while True:
    user_input = input("You: ")

    # Check for exit
    if "bye" in user_input.lower():
        print(" Chatbot: Goodbye! ")
        break

    # Get and print response
    reply = chatbot_response(user_input)
    print("Chatbot:", reply)
