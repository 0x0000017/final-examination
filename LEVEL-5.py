#Programmed by: Arboleda, Adrian P.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.right = None
        self.down = None
        self.left = None
        self.up = None
        
    def print_next(self):
        current = self
        while current:
            value.append(current.data)
            print(current.data, end=" ")
            current = current.next
        value.sort()


    def print_down(self):
        current = self
        while current:
            value.append(current.data)
            print(current.data, end=" ")
            current = current.down
        value.sort()

            
    def print_left(self):
        current = self
        while current:
            value.append(current.data)
            print(current.data, end=" ")
            current = current.left
        value.sort()


    def print_up(self):
        current = self
        while current:
            value.append(current.data)
            print(current.data, end=" ")
            current = current.up
        value.sort()
        


value = []



node_a = Node(10)
node_b = Node(1)
node_c = Node(3)
node_d = Node(9)

node_b2 = Node(8)
node_b3 = Node(6)
node_b4 = Node(2)

node_c2 = Node(4)
node_c3 = Node(5)
node_c4 = Node(7)


#next
node_a.next = node_b
node_b.next = node_c
node_c.next = node_d

#down
node_b.down = node_b2
node_b2.down = node_b3
node_b3.down = node_b4
node_c.down = node_c2
node_c2.down = node_c3

#prev
node_b3.left = node_b4

#up
node_c.up = node_c4


print("Flattening the linked list: ")
node_a.print_next()
node_b.print_down()
node_c.print_down()
node_c.print_up()

print("")
res = []
[res.append(x) for x in value if x not in res]
print("After sorting the linked list: "+str(res))