import sys, os, platform
# task 1
# print(platform.system())

# task 2
# print(os.getcwd())

# task 3
# print(os.listdir())

# task 4
# os.mkdir("test_folder")

# task 5
# os.chdir("test_folder")
# print(os.getcwd())

# task 6

# os.close(os.open("test_file.txt", os.O_CREAT))

# task 7 
# if "test_file.txt" in os.listdir("."):
#     print("True")

# task 8
# os.remove("test_file.txt")

# task 9 
# os.chdir("../")
# print(os.getcwd())

# task 10
# os.rmdir("test_folder")

# task 11
# argument = sys.argv[1]
# print(f"argument received: {argument}")

# task 12
# arguments = len(sys.argv) -1
# print(f"total arguments: {arguments}")

# task 13
# arguments = sys.argv
# print(arguments)

# task 14
# print("this will print")
# sys.exit()
# print("this will not print")

# task 15
# print(os.environ["path"])

# task 16
# system = sys.platform
# print(f"running on: {system}")

# task 17
# dir_path = "/home/user/test/"
# file = "file.txt"
# print(os.path.join(dir_path, file))

# task 18
# path = "c:/python-module/labs/lab5.3"
# print(os.path.isfile(path))
# print(os.path.isdir(path))

# task 19
# print(os.system('ls'))

# task 20
# os.mkdir("test_folder")
# print("folder created")

# file_path = "test_folder/test_file.txt"
# os.close(os.open(file_path, os.O_CREAT))
# print("file created")

# print(os.path.isfile(file_path))

# os.remove(file_path)
# os.rmdir("test_folder")
# print("Cleanup done")
