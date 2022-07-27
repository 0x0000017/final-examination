#Programmed by: Adrian Arboleda


def isRight(a, b ,c):
    if a**2 + b**2 == c**2:
        print("That is a right triangle")
    else:
        print("That is not a right triangle")

print("Enter 3 sides of triangle")
x = int(input(": "))
y = int(input(": "))
z = int(input(": "))

isRight(x, y, z)