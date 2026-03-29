# day_of_week = input("what day of the week is it today? ")


# if day_of_week.capitalize() == "Monday" or day_of_week.capitalize() == "Friday":
#     print("it's a good day!")
    
# elif day_of_week.capitalize() == "Tuesday":
#     print("i hate tuesaday")
    
# else:
#     print("doesn;t matter")

# lab3.2

# friends = ["rolf", "Jen", "Bob"]
# print("Jen" in friends)

# movies = {"avatar", "blood", "her", "the matrix"}
# user_movie = input("enter movie you have watched recently\n")

# if user_movie in movies:
#     print("you've already watched this movie")
# else:
#     print("you should watch this movie")

# print("xyz" in "the matrix")

# set1 = {1,1,1,2,66,7,8}
# print(41 in set1)

#lab3.3

# secret_num = 5
# play = ("y", "Y")
# user_input = input("enter Y if you would like to play\n")

# if user_input in play:
#     user_guess = int(input("enter a number: "))
#     if user_guess == secret_num:
#         print("you guessed correctly")
#     elif abs(user_guess - secret_num == 1):
#         print("you were off by one")
#     else:
#         print("wrong number")
    
#lab3.4

def process_data_guarded(data=None):
    if not data:
        print("no data provided")
    elif not isinstance(data,list ):
        print(f"invalid value type for data provided {type(data)} required list")
    else:
        print(f"processing {len(data)} items...")
        print("processed")
        
        
empty = []
full = [1,2,3]
    
# process_data_guarded(empty)
process_data_guarded(empty)
process_data_guarded(full)
process_data_guarded(None)
process_data_guarded("ABC")
process_data_guarded(10)