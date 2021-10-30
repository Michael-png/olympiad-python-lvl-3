import math
def printCosines(header, n = 0):
    print(header)
    while 100 > n >= 0:
        n = n+1
        CosineAnswer = math.cos(n)
        print(CosineAnswer)
printCosines(header="This is the cosines of 0.1's")


