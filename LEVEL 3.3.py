import random
list = []

def generateRandom():
    rng = random.randint(1, 10)
    return rng

def reOrder(list, order):
    if order == 'asc':
        list.sort()
        print(list)
    elif order == 'desc':
        list.sort(reverse=True)
        print(list)
    else:
        print(list)
 

for x in range(10):
    list.append(generateRandom())


reOrder(list, 'asc') #Ascending
# reOrder(list, 'desc') #Descending
# reOrder(list, 'none') #None