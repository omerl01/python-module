# set([1,2], [3,4])

# {{1,2}, {3,4}}

set_of_tuples = {(1,2), (3,4)}
# print(set_of_tuples)

# if (1,2) in set_of_tuples:
#     print("True")
# else:
#     print("False")

# if (1,3) in set_of_tuples:
#     print("True")
# else:
#     print("False")

developers = {"Alice", "Bob", "charlie"}
admins = {"Alice", "david"}

# print(developers.union(admins))
# print(developers | admins)
# print(developers.intersection(admins))
# print(developers & admins)
# print(developers.difference(admins))
# print(developers - admins)
# developers.intersection_update(admins)
# print(developers)
# developers.intersection(admins)
# print(developers)

ports = { "192.9.200", "154.2.50"}
secure_ports = {"192.9.200", "154.2.50", "124.09.43.3", "452,4,9,12"}

union = developers.union(admins)
intersection = developers.intersection(admins)
diff = developers.difference(admins)
print(
    f"""
    "union: {union},
    intersection: {intersection},
    difference: {diff}
    """
)