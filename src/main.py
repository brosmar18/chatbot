from datetime import datetime

def greet_user():
    """
        Greet user based on the current time of the day.
    """

    # Get current time. 
    current_time = datetime.now().time()

    # Determine the greeting based on the time. 
    if current_time.hour < 12: 
        greeting = "Good Morning"
    elif 12 <= current_time.hour < 18:
        greeting = "Godo afternoon"
    else: 
        greeting = "Good Evening"

    print(f"{greeting}, welcome to chatbot!")


# Call the function
greet_user()