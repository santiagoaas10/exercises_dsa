class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class Linked_List:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node 
        self.length = 1


my_linked_list = Linked_List(4)

print(my_linked_list.head.value)

#vamos a crear una lista completa y a iterar sobre ella

