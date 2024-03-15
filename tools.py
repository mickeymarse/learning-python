# f strings

# user_name = "Myryam"
# user_age = 32
# user_information = f"{user_name} is {user_age} years old."
# print(user_information)

# single line if statements

# user_age = 15
# user_status = "Adult" if user_age >= 18 else "Child"
# print(user_status)

# list comprehension

# simple_list = [f"{j}{i}" for i in range(0,11,1) for j in ("a","b","c") if j == "a"]
# print(simple_list)

# lambda functions

# double_value = lambda num: num * 2
# print(double_value(10))

# some functions want a function as an argument

# random_list = [("Anna", 25), ("Paul", 40), ("Lisa", 10)]
# sorted_list = sorted(random_list, key = lambda user_tuple: user_tuple[1])
# print(sorted_list)

# EXERCISE

battleship_board = [f"{y}{x}" for x in range(1,6) for y in ("A", "B", "C", "D", "E") if f"{y}{x}" != "C3"]
print(battleship_board)
