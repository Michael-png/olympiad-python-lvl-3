def printSums():
    x = 0
    y = 0
    j = 2
    k = 3
    for i in range(10):
        j = j + 1
        x += j
        y += k
        k = k + 2
    print(x)
    print(y)