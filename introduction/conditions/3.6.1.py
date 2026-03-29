
# def tuple_func(list):
#     sum = 0
#     for num in list:
#         sum += num
#     length = len(list)
#     average = sum / length
#     result = (sum, length, average)
#     print(result)
my_list = (5,4,3,2,1,7,8,10,50,40,30)
# tuple_func(my_list)

# def high_low(list):
#     max_num = max(list)
#     low_num = min(list)
#     print(f"highest {max_num} and lowest: {low_num}")
    
# high_low(my_list)
    
# def even(list):
#     even_list = []
#     for num in list:
#         if num % 2 == 0:
#             even_list.append(num)
#     even_list.sort()
#     print(even_list)

# even(my_list)


# def even_odd(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")
   

# even_odd(6)

#exerrcise 5
# def test_scores(list):
#     passing_tests = []
#     for test in list:
#         if test > 60:
#             passing_tests.append(test)
#     print(passing_tests)

# scores = [60, 70, 80, 50, 100, 90, 55]
# test_scores(scores)

# 6

# def empty_full(list):
#     if not list:
#         return None
#     else:
#         average = sum(list) / len(list)
#         print(average)
        
# empty = []
# full = [5,4,3,7,8]
# empty_full(empty)
# empty_full(full)


# def func(x,y):
#     print(f"hi {x} you're {y} ")
    
# func(y="funny", x="omer")

# def higher_then(list, num):
#     higher_numbers = []
#     for number in list:
#         if number > num:
#             higher_numbers.append(number)
#     print(higher_numbers)
    
# check_num = 10

# higher_then(my_list, check_num)

# def is_reverse(list, reverse=False):
#     if reverse:
#         print(sorted(list, reverse=True))

# reverse = True
# is_reverse(my_list, reverse)
              
# 9 
# def highest(*args):
#     return max(args)

# print(highest(1,5,6,10,12,14,17,2))

#10

# def even_numbers(*args):
#     even = []
#     for num in args:
#         if num % 2 == 0:
#             even.append(num)
#     return even

# print(even_numbers(6,4,3,1,2,9,80))

# 11
# def hi(name, age):
#     print(f"hi {name}, your age is {age}")
    
# hi(age=24, name="omer")

# 12 
# def math_solve(list, action):
#     if action == "min":
#         print(min(list))
#     elif action == "max":
#         print(max(list))
#     elif action == "sum":
#         print(sum(list))
        
# math_list = [5,2,5,7,8,10]

# math_solve(math_list, "sum")
# math_solve(math_list, "max")
# math_solve(math_list, "min")

# 13

# def outer(x,y):
#     def inner():
#         return x +y
#     return inner()

# print(outer(5,3))

# 14
# def outer(message):
#     def inner():
#         print(message)
#     inner()
# outer("hi there")

# 15
# def outer():
#     number = 10
#     def inner():
#         nonlocal number
#         number += 1
#     inner()
#     print(number)
# outer()        

# 16
# def add_one(num):
#     num +=1
#     return num

# def full_func(list, func):
#     new_list = []
#     for num in list:
#         new_num = func(num)
#         new_list.append(new_num)
#     return new_list

# print(full_func(my_list,add_one))

# 17

# def root(func, num):
#     return(func(num))

# def root_op(num):
#     return num ** 2

# print(root(root_op, 10))

# # 18 
# def func(list, threshold, reverse=False):
#     new_list = []
#     for num in list:
#         if num > threshold:
#             new_list.append(num)
#     if reverse == True:
#         return sorted(new_list, reverse=True)
#     else:
#         return sorted(new_list)
    
    
# min_num = 5
# cutrent_list = [5,8,9,7,90,80,3,60]
# print(func(cutrent_list,min_num))
# reverse = True
# print(func(cutrent_list,min_num, reverse))

# 19
# def func(*args):
#     sum_num = sum(args)
#     maximum = max(args)
#     minimum = min(args)
#     my_tuple = (sum_num, maximum, minimum)
#     return my_tuple

# print(func(1,2,5,6,7,8,4,90))

# # 20
# def func(a_list):
#     odd_numbers = []
#     even_numbers = []
#     for num in a_list:
#         if num % 2 ==0:
#             even_numbers.append(num)
#         else:
#             odd_numbers.append(num)
#     return (odd_numbers, even_numbers)

# print(func(my_list))