import datetime as dt

def age_calculator():
    d = input('Please enter a date: (DD-MM-YYY) ')

    date = dt.datetime.strptime(f"{d}", "%d-%m-%Y")
    today = dt.date.today()
    age = today.year - date.year
    if today.month < date.month:
        age -=1
    elif today.month == date.month:
        if today.day < date.day:
            age -=1
    
    return age

if __name__ == "__main__":
    print(age_calculator())