friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

# print(friends)
# print(abroad)

local = friends.difference(abroad)
# # print(local)

# # print(abroad.difference(friends))

# # blank = set()
# # print(blank)

friends = local.union(abroad)
# print(friends)

# print(local | abroad)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
intersect = art.intersection(science)

print(art & science)

bob_art = "Bob" in art
anne_art = "Anne" in art

print(bob_art)
print(anne_art)

# print(f"common elements: {intersect}")

print(
    f"""
    Local friends: {local}
    All friends: {friends}
    Common intersts: {intersect}
    """
)
