#Programmed by: Adrian Arboleda

ch = '7'
x = int(input("Enter a number from 0-35: "))
if x <= 9:
    print(x)
else:
    letter = chr(ord(ch)+x)
    print(letter)

