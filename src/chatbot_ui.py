import tkinter as tk
from tkinter import ttk
from main import handle_simple_conversation, handle_knowledge_query, analyze_sentiment, handle_advanced_conversation

# Initialize the Tkinter root window
root = tk.Tk()
root.title("Chatbot")

# Styling
root.configure(bg="light blue")

# Chat area
chat_area = tk.Text(root, wrap=tk.WORD, width=50, height=15, bg="white", fg="black", font=("Arial", 12))
chat_area.pack(padx=10, pady=10)

# User entry area
user_entry = ttk.Entry(root, width=50, font=("Arial", 12))
user_entry.pack(padx=10, pady=5)

# Global variable to hold the last chatbot message
last_bot_message = ""

# Function to handle sending a message
def on_send():
    global last_bot_message  # Declare it as global to modify it

    user_input = user_entry.get()
    chat_area.insert(tk.END, f"You: {user_input}\n")
    
    # Handle simple 'Yes' or 'No' based on last bot message
    if user_input.lower() == 'yes' and last_bot_message:
        chatbot_response = f"Great! You agreed to what I last said: {last_bot_message}"
    elif user_input.lower() == 'no' and last_bot_message:
        chatbot_response = f"Oh, you disagreed with what I last said: {last_bot_message}"
    else:
        # Try handling simple conversation first
        chatbot_response = handle_simple_conversation(user_input)
        
        # If the response is the default "I don't understand", try the knowledge base
        if chatbot_response == "I'm sorry, I don't understand that.":
            chatbot_response = handle_knowledge_query(user_input)
        
        # If the response is still the default, use advanced NLU
        if chatbot_response == "I'm sorry, I don't have that information.":
            chatbot_response = handle_advanced_conversation(user_input)

        # If no other methods work, perform sentiment analysis
        if chatbot_response in ["I'm sorry, I don't understand that.", "I'm sorry, I don't have that information.", "I'm sorry, I couldn't find any specific entities in your message."]:
            chatbot_response = analyze_sentiment(user_input)

    chat_area.insert(tk.END, f"Chatbot: {chatbot_response}\n")
    last_bot_message = chatbot_response  # Update the last_bot_message
    user_entry.delete(0, tk.END)

# Send button
send_button = ttk.Button(root, text="Send", command=on_send)
send_button.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
