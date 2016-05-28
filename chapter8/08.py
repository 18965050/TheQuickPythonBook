x = [1, 3, -7, 4, 9, -5, 4]

print(len(x))

for i in range(len(x)):
    if x[i] < 0:
        print("Found a negative number at index ", i)