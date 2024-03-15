# print('napule'.upper())
# print('NAPULE'.lower())
# print('napule'.replace('e','3'))
# print(len('napule'))

# print(abs(-7))
# print(max(1234,4321))
# print(min(1234,4321))
import math

print("Pithagora's Theorem Calculator")
x , y = input("Type two numbers separated by a space: ").split()

first_num = int(x)
second_num = int(y)
# print(type(first_num),type(second_num))

pitha = math.sqrt((pow(first_num,2)+(pow(second_num,2))))
print(round(pitha,2))
