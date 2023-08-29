from datetime import datetime

def greet_user():
    """
        Greet user based on the current time of the day.
    """

    # Get current time. 
    current_time = datetime.now().time()

    # Determine the greeting based on the time. 