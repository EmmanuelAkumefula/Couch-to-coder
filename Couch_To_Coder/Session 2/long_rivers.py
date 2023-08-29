# # long_rivers.py
# rivers = [
#     {"name": "Nile", "lengths": 4157},
#     {"name": "Yangtze", "length": 3434},
#     {"name": "Murray-Darling", "length": 2310},
#     {"name": "Volga", "length": 2290},
#     {"name": "Mississippi", "length": 2540},
#     {"name": "Amazon", "length": 3915}
# ]

# name_to_find = str(input("Type name to search"))


# for river in rivers:
#     if   river["name"] == name_to_find:
#         print(river["name","lengths"])
#     else:
#         print("name not found!")
    
#     # print(river["name"])


rivers = [
    {"name": "Nile", "lengths": 4157},
    {"name": "Yangtze", "lengths": 3434},  # "lengths" should be "length"
    {"name": "Murray-Darling", "lengths": 2310},  # "lengths" should be "length"
    {"name": "Volga", "lengths": 2290},  # "lengths" should be "length"
    {"name": "Mississippi", "lengths": 2540},  # "lengths" should be "length"
    {"name": "Amazon", "lengths": 3915},
]

name_to_find = input("Type name to search: ")  # Removed unnecessary str()

found = False  # Flag to keep track of whether the name was found

for river in rivers:
    if river["name"] == name_to_find:
        print(f"Name: {river['name']}, Length: {river['lengths']}")
        found = True
        break  # Exit the loop once the name is found

if not found:
    print("Name not found!")






















# Task 1: Print out each river's name
# for river in rivers:
#     print(river["name"])

# # Task 2: Calculate and print the total length of all the rivers
# total_length = 0
# for river in rivers:
#     total_length += river["length"]
# print("Total length of all rivers:", total_length, "miles")

# # Extension 1: Print out every river's name that begins with the letter M
# print("Rivers with names starting with M:")
# for river in rivers:
#     if river["name"].startswith("M"):
#         print(river["name"])

