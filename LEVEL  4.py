#Programmed by: Adrian Arboleda

import random

rnglist = []


def generateRand():
    rng = random.randint(100, 999)
    return rng

def groupNum(list):
    evenList = []
    oddList = []
    for i in list:
        if ( i % 2 == 0):
            evenList.append(i)
        else:
            oddList.append(i)
    print("Even list: ", evenList)
    print("Odd list: ", oddList)


def groupByNine(list):
    print("All numbers divisible by 9: ")
    divByNine = []
    for i in list:
        x = [int(a) for a in str(i)]
        z = sum(x)
        if z % 9 == 0:
            temp = [str(j) for j in x]
            res = int("".join(temp))
            divByNine.append(res)
    print(divByNine)


def isPrime(list):
    print("All prime numbers in the list: ")
    primeList = []
    for i in list:
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                primeList.append(i)
    print(primeList)


def captureNine(list):
    print("All numbers that contain 9 on it: ")
    allNine = []
    for i in list:
        x = [int(a) for a in str(i)]
        if 9 in x:
            temp = [str(j) for j in x]
            res = int("".join(temp))
            allNine.append(res)
    print(allNine)




for x in range(100):
    rnglist.append(generateRand())


print(f"Random number list: {rnglist}") # A
groupNum(rnglist) #B
groupByNine(rnglist) #C
isPrime(rnglist) #D
captureNine(rnglist) #E