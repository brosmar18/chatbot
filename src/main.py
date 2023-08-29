knowledge_base = {
    "what is your name": "I'm a chatbot created to assist you.",
    "what is the capital of france": "The capital of France is Paris.",
    "who is the president of the united states": "As of my last update in September 2021, the President is Joe Biden.",
    # Add more questions and answers here
}

def handle_knowledge_query(user_input):
    """
    Handle knowledge-based queries based on predefined knowledge.
    """
    user_input = user_input.lower().strip()
    return knowledge_base.get(user_input, "I'm sorry, I don't have that information.")