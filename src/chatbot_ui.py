import tkinter as tik
from tkinter import ttk

def on_send():
    user_input = user_entry.get()
    # TODO: Process user input and get chatbot response. 
    chat_area.insert(tik.End, f"You: {user_input}\n")
    chat_area.insert(tik.END, f"Chatbot: I'm still learning...\n")
    user_entry.delete(0, tk.END)

    