from datetime import datetime

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.now()
        response = func(*args, **kwargs)
        end_time = datetime.now()
        duration = end_time - start_time
        print(f"The time taken by {func.__name__} is {duration.total_seconds()}")
        return response 
    return wrapper