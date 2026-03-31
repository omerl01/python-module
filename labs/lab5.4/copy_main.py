from pathlib import Path
import os
import random
import time
from collections import Counter, deque
import hashlib
import calendar
import statistics
import webbrowser
import shutil
# task 1
# p = Path("test_folder/test_file.txt")
# print(p)

# task 2
# file = "c:/python-module/basic/.venv/Scripts/python.exe"
# print(os.path.isfile(file))

# task 3
# file = "c:/python-module/basic/.venv/Scripts/python.exe"
# print(f"is file: {os.path.isfile(file)}")
# print(f"is directory: {os.path.isdir(file)}")

# task 4
# print(random.randint(1,10))

# task 5
# list = ["apples", "cherries", "tomatos"]
# print(random.choice(list))

# task 6
# num = [1,2,3,4,5,6]
# random.shuffle(num)
# print(num)

# # task 7
# print("waiting")
# time.sleep(3)
# print("Done")


# task 8 
# print(time.time())

# task 9 
# list = ["a","b", "a","b","a"]
# print(Counter(list))

# task 10
# queue = deque([1,2,3])
# print(queue.popleft())

# task 11
# data = "hello".encode()
# hash_data = hashlib.md5(data)
# result = hash_data.hexdigest()
# print(result)

# task 12
# print(calendar.month(2026, 3))

# task 13
# print(statistics.mean([1,2,3,4,5]))

# task 14
# print(statistics.median([1,2,3,4,5]))

# task 15
# webbrowser.open("https://www.w3schools.com/python/ref_module_webbrowser.asp")
# print("browser opened")

# task 16
source  = "c:/python-module/labs/lab5.4/main.py"
destination = "c:/python-module/labs/lab5.4/copy_main.py"
dest = shutil.copy(source, destination)