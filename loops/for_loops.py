friends = ["rolf", "jen", "bob", "anne"]
for friend in friends:
    print(f"{friend} is my friend")
    
#range()
for number in range(4):
    print(f"{number} is my friend")
    
grades = [80, 75, 90, 100, 85]

total = 0 
amout = len(grades)
# for grade in grades:
#     total += grade
total = sum(grades)
print(total/amout)