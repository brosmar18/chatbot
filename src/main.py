from textblob import TextBlob
import spacy 

# Load spaCy model 
nlp = spacy.load("en_core_web_sm")

def handle_advanced_conversation(user_input):
    """
    Handle advanced conversation using spaCy's NLP capabilities.
    """
    doc = nlp(user_input)
    for ent in doc.ents:
        if ent.label_ == "GPE":
            return f"You're talking about {ent.text}, that's a place!"
        elif ent.label_ == "PERSON":
            return f"You mentioned {ent.text}, is that a person you know?"
        elif ent.label_ == "TIME":
            return f"You mentioned a time: {ent.text}. Is there an event?"
        # Add more entity types and responses
    return "I'm sorry, I couldn't find any specific entities in your message."

# Analyze the sentiment of the user input and return a response
def analyze_sentiment(user_input):
    analysis = TextBlob(user_input)
    if analysis.sentiment.polarity > 0:
        return "You seem happy, that's great!"
    elif analysis.sentiment.polarity < 0:
        return "You seem unhappy, is there anything I can do?"
    else: 
        return "You seem neutral, how can I assist you further?"

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