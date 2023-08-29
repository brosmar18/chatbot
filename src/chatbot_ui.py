import tkinter as tk
from tkinter import ttk
from datetime import datetime

def greet_user():

    # Greet user based on current time of the day. 
    # Get current time.
    current_time = datetime.now().time()



def on_send():
    user_input = user_entry.get()
    # TODO: Process user input and get chatbot response
    chat_area.insert(tk.END, f"You: {user_input}\n")
    chat_area.insert(tk.END, f"Chatbot: I'm still learning...\n")
    user_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Chatbot")

# Create a text area for chat
chat_area = tk.Text(root, wrap=tk.WORD, width=50, height=15)
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