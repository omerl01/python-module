from datetime import datetime, timedelta
from math import *
now = datetime.now()

# task 2
# print(now.time())

# task 3
# print(now.year)

# task 4
# year_born = int(input("enter whe you were born "))
# current_year = now.year
# age = current_year - year_born
# print(f"age: {age}")


# task 5
# now = datetime.now()
# last_day = datetime(year=2026,month=12, day=31)
# amount_of_days = last_day - now
# print(f"days: {amount_of_days.days}")

# task 6
# print(now.strftime("%A"))

# task 7
# ten_ahead = timedelta(days=10) 
# days_ahead = now + ten_ahead
# print(f"Future date: {days_ahead.date()}")

# task 8 
# first_date = input("enter first date ")
# second_date = input("enter second date ")
# dt_first_date = datetime.strptime(first_date, "%d-%m-%Y")
# dt_second_date = datetime.strptime(second_date, "%d-%m-%Y")

# delta_days = (dt_first_date - dt_second_date).days
# print(f"Difference: {abs(delta_days)}")

# task 9 
# formatted_time = now.strftime("%d/%m/%Y %H:%M")
# print(formatted_time)

# task 10
# day = now.strftime("%A")
# match day:
#     case "Saturday" | "Sunday":
#         print("Weekend: True")
#     case _:
#         print("Weekend: False")
    
    
# task 11
# print(sqrt(16))

# task 12
# print(pow(2,3))

# task 13
# print(ceil(4.2))

# task 14
# print(floor(4.8))

# task 15
# print(abs(-10))

# task 16

# print(pi)


# task 17
# r = 5
# area = pi * r**2
# print(area)

# task 18
# d = 8 -5
# print(d)

# task 19
# numbers = [5,4,3,2,6,7]


# average = sum(numbers) / len(numbers)
# print(average)

# task 20
# hours = int(now.strftime("%H"))
# result = hours * 2
# print(result)