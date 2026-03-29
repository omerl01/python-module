# my profile app - project

name= input("enter your name:  ")
age = input("enter your age: ")
city = input("enter your city: ")

user_hobbies = input("enter your hobbies here with ',' inbetween hobbies: ").split(", ")

user_data = [name, age, city]

print(f"""
Name: {name}
age: {age}
City: {city} 
Hobbies: {user_hobbies}\n
""")


popular_hobbies = ["music", "sports", "gaming", "reading"]

for hobby in user_hobbies:
    popular = hobby in popular_hobbies
    print(f"{hobby} -> {popular}")
    
hobbies_set = set(user_hobbies)

unique_hobbies = hobbies_set - set(popular_hobbies)
print("")
print(f"unique hobbies: {unique_hobbies}\n")
print(f"total hobbies: {len(user_hobbies)}\n")
print(f"number of unique hobbies: {len(unique_hobbies)}\n")


hobbies_tuple = tuple(user_hobbies)

# music_in = "music" in hobbies_tuple
# print(f"music is in user hobbies: {music_in}")
print(f"hello {name} you have: {len(user_hobbies)} hobbies")



