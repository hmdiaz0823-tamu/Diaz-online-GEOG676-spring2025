#GEOG 676 GIS Programming
#Spring 2026
#01/25/26

#Week2

userInput = int(input("Choose nth number in the sequence: "))

def printVertically(a, b, c, n):
    count = 3
    print(a)
    print(b)
    while count <= n:
        print(c)
        a = b
        b = c
        c = (a + b)
        count += 1

