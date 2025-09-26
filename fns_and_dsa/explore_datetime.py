from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    return current_date

def calculate_future_date():
    formatted_date = display_current_datetime().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future = display_current_datetime() + timedelta(days=number_of_days)
    print(f"Future date: {future.strftime('%Y-%m-%d')}")

    
if __name__ == "__main__":
    calculate_future_date()