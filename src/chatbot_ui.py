import tkinter as tk
from tkinter import ttk
from datetime import datetime
from main import handle_simple_conversation, handle_knowledge_query, analyze_sentiment

def greet_user():

    # Greet user based on current time of the day. 
    # Get current time.
    current_time = datetime.now().time()

    # Determine greeting based on time. 
    if current_time.hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_time.hour < 18:
        greeting = "Good Afternoon"
    else: 
        greeting = "Good Evening"

    chat_area.insert(tk.END, f"{greeting}, welcome to chatbot!\n")

def on_send():
    user_input = user_entry.get()
    # TODO: Process user input and get chatbot response
    chat_area.insert(tk.END, f"You: {user_input}\n")
    
    # Handle simple convos and get chatbot's response
    chatbot_response = handle_simple_conversation(user_input)

    # If the response is the default "I don't understand", try the knowledge base. 
    if chatbot_response == "I'm sorry, I don't understand that.":
        chatbot_response = handle_knowledge_query(user_input)

    # If teh response is still the default, perform sentiment analysis
    if chatbot_response == "I'm sorry, I don't have that information.":
        chatbot_response = analyze_sentiment(user_input)

    chat_area.insert(tk.END, f"Chatbot: {chatbot_response}\n")
    user_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Chatbot")

# Styling the main window
root.configure(bg="light blue")


# Text area for chat with styles.
chat_area = tk.Text(root, wrap=tk.WORD, width=50, height=15, bg="white", fg="black", font=("Arial", 12))
chat_area.pack(padx=10, pady=10)

# Call greet_user to display greenting when app launches
greet_user()

# Entry box for user input
user_entry = ttk.Entry(root, width=50)
user_entry.pack(padx=10, pady=5)

# Send button
send_button = ttk.Button(root, text="Send", command=on_send)
send_button.pack(pady=5)

root.mainloop()