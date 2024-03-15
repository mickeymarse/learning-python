import matplotlib.pyplot as plt

# data

x = [i for i in range(0,11)]
y = [y ** 2 for y in x]

print(x)
print(y)

plt.plot(x,y)

plt.xlabel("smth")
plt.ylabel("smth else")

plt.show()

