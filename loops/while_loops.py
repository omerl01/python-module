# # while loops basics
# # user_input = input("Would you like to paly? (n/y)")

# # user_input = "y"
# # while user_input != "n":
# #     print("Game is Running...")
#     # user_input = input("Would you like to play again (n/y)")
    
    
# while True:
#     user_input = input("Would you like to paly? (n/y)")
    
#     if user_input == "n":
#         break
#     print("Game is runing")

# task 1
# num = 1
# while num < 6:
#     print(num)
#     num +=1
    
# task 2
# num = 5
# while num > 0:
#     print(num)
#     num -= 1

# task 3
# num = 2
# while num <= 10:
#     print(num)
#     num +=2

# task 4
# num_sum = 0
# number = 1
# while number < 6:
#     num_sum += number
#     number += 1
# print(num_sum)

# task 5
# num = 3
# while num < 10:
#     print(num)
#     num = num * 3
    
# task 6
# user_num = input("enter number: ")
# prints = 1
# while prints < 6:
#     print(user_num)
#     prints += 1

# task 7
# user_num = input("enter number: ")
# num = 1
# while num != int(user_num) + 1:
#     print(num)
#     num +=1
# task 8 
# enter_0 = False

# while not enter_0:
#     user_input = input("enter a number: ")
#     if  user_input == "0":
#         enter_0 = True

# task 9 
# correct_pass = False
# while correct_pass == False:
#     user_pass = input("enter a password ")
#     if user_pass == "1234":
#         correct_pass = True

# task 10
# proceed = True
# while proceed:
#     user_input = input("enter y to continue and n to stop ")
#     if user_input == "n":
#         proceed = False

# task 11
# num = 1
# while num < 10:
#     if num % 2 == 0:
#         print(num)
#     num += 1

# task 12
# even_num = []
# num = 1
# while num < 20:
#     if num % 2 == 0:
#         even_num.append(num)
#     num += 1
# print(len(even_num)) 

# task 13
# num_sum = 0 
# num = 1
# while num <=10:
#     if num % 2 != 0:
#         num_sum += num
#     num +=1
# print(num_sum)

# task 14
# game_on = True
# while game_on:
#     user = input("enter a number: ")
#     if user == "q":
#         game_on = False
#     elif int(user) % 2 == 0:
#         print("even")
#     else:
#         print("odd")
    

# task 15
# entries = 1
# numbers = []
# while entries < 6:
#     number = int(input("enter a number "))
#     numbers.append(number)
#     entries += 1
# print(max(numbers))

# task 16
# while True:
#     user= input("enter exit: ")
#     if user == "exit":
#         break

# task 17
# num = 1
# while num < 11:
#     print(num)
#     num += 1
#     if num == 7:
#         break

# task 18
# num_sum = 0
# while True:
#     user = int(input("enet a number: "))
#     if user < 0:
#         break
#     num_sum += user
#     print(num_sum)

# task 19
# num = 4
# game_on = True
# while game_on:
#     user_guess = int(input("enter a guess: "))
#     if user_guess == num:
#         game_on = False

# task 20
entries = 0
while True:
    user_input = input("enter: ")
    entries += 1
    if user_input == "stop":
        break
print(entries)