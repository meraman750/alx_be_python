from datetime import datetime, timedelta


def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")
    return formatted_date

def calculate_future_date():
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future = datetime.now() + timedelta(days=number_of_days)
    formatted_future = future.strftime('%Y-%m-%d')
    print(f"Future date: {future.strftime('%Y-%m-%d')}")
    return formatted_future

    
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
