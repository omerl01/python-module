# enumerate
# zip

# # servers = ["web-01", "web-02", "web-03"]
# # [(0, "web-01"), (1, "web-02"),(2, "web-03")]
# # for server in enumerate(servers):
# #     print(type(server))
# #     print(server)
# #     print(f"this is tuple {server}")
    

# servers = ["web-01", "web-02", "web-03"]
# # [(0, "web-01"), (1, "web-02"),(2, "web-03")]
# for index, server in enumerate(servers):
#     # print(type(server))
#     # print(server)
#     # print(server[0]) # index
#     # print(server[1]) # item
#     print(f"{index} Proccessing server {server}")

# task 1
# names = ["Alice", "Bob", "Charlie"]
# for  name in enumerate(names):
#     print(name)

# task 2
# servers = ["app-01", "app-02", "app-03"]
# for server in enumerate(servers, start=1):
#     print(server)

# taksk 3
# errors = ["disk full", "timeout", "connection lost"]
# for error in enumerate(errors):
#     if error[0] % 2 == 0:
#         print(error)

# task 4
# ports = [22, 80, 443, 8080]
# for port in enumerate(ports):
#     if port[0] > 1:
#         print(port)

# task 5
# users = ["admin", "dev", "ops"]
# for index, user in enumerate(users):
#     print(f"USER #{index}: {user}")

# task 6
# files = ["log1.txt", "log2.txt", "log3.txt"]
# for file in enumerate(files):
#     if file[0] > 1:
#         print(file)

# task 7
# regions = ["us-east-1", "eu-west-1", "ap-south-1"]
# for region in enumerate(regions):
#     if region[0] > 0:
#         print(region)

# task 8
# services = ["nginx", "redis", "postgres"]
# for serivce in enumerate(services):
#     if serivce[0] == 1:
#         print(serivce)

# task 9
# tasks = ["backup", "cleanup", "monitoring"]
# for task in enumerate(tasks):
#     if task[0] % 2 != 0:
#         print(task)

# task 10
containers = ["c1", "c2", "c3", "c4"]
# for index, container in enumerate(containers):
#     if index < 2:
#         print(container)
        

list = ["Alice","Bob", "Charlie"]
# list = [(0, "alice"), (1, "bob"), (2, "charlie")]

for name in (list):
    if name == "Bob":
        print(name)