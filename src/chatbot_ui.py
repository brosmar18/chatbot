import tkinter as tk
from tkinter import ttk
from datetime import datetime
from main import handle_simple_conversation, handle_knowledge_query, analyze_sentiment, handle_advanced_conversation

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
    chat_area.insert(tk.END, f"You: {user_input}\n")
    
    # Try handling simple conversation first
    chatbot_response = handle_simple_conversation(user_input)
    
    # If the response is the default "I don't understand", try the knowledge base
    if chatbot_response == "I'm sorry, I don't understand that.":
        chatbot_response = handle_knowledge_query(user_input)
    
    # If the response is still the default, perform sentiment analysis
    if chatbot_response == "I'm sorry, I don't have that information.":
        chatbot_response = analyze_sentiment(user_input)

    # If no other methods work, use advanced NLU
    if chatbot_response in ["I'm sorry, I don't understand that.", "I'm sorry, I don't have that information.", "I'm sorry, I couldn't find any specific entities in your message."]:
        chatbot_response = handle_advanced_conversation(user_input)
        
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

# Entry box for user input with styles.
user_entry = ttk.Entry(root, width=50, font=("Arial", 12))
user_entry.pack(padx=10, pady=5)

# Send button with styles. 
send_button = ttk.Button(root, text="Send", command=on_send, style="C.TButton")
send_button.pack(pady=5)

# Custom button style.
style = ttk.Style()
style.configure("C.TButton", font=("Arial", 12, "bold"))

root.mainloop()