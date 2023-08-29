simple_responses = {
    "hello": "Hi there!",
    "how are you": "I'm just a program, so I don't have feelings, but thanks for asking!",
    "bye": "Goodbye!",
    "who are you": "I'm a chatbot, here to assist you."
}

def handle_simple_conversation(user_input):
    # Handle simple convos based on predefined responses. 

    user_input = user_input.lower().strip()
    return simple_responses.get(user_input, "I'm sorry, I don't understand that.")