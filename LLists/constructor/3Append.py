class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
    
    def printing(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def append(self, value):
        new_node_to_append = Node(value)

        if self.head is None and self.tail is None:
            self.head = new_node_to_append
            self.tail = new_node_to_append
        
        else:
            self.tail.next = new_node_to_append
            self.tail = new_node_to_append


LL = LinkedList('A')
LL.append('B')
LL.append('C')
LL.append('D')

LL.printing()
