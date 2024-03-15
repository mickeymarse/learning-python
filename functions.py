# # create a function
# def print_x_times(param = "loop", times = 5):
#     counter = 0
#     while counter < times:
#         print(param)
#         counter += 1
#     return times
        
# # call a function
# total = print_x_times("test", 6)
# print(total)

# hypothenuse calculator
# import math

# def hyp_calc(first = 1, second = 1):
#     pitha = math.sqrt((pow(first,2)+(pow(second,2))))
#     return round(pitha,2)

# print(hyp_calc())

# EXERCISE

def shouter (shout = "Buongiorno!", times = 5):
    c = 0
    if times > 10:
        return "You are too loud."
    else:
        while c < times:
            print(shout.upper())
            c += 1
    return "Done."

print (shouter("buonasera!", 9))
