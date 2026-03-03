class Node:
    def __init__(self,value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    
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
        self.length +=1

    def pop(self):
        temp = self.head
        perseguidor = self.head
        if self.length==0:
            return None

        else:
            while temp.next is not None:
                perseguidor = temp
                temp = temp.next
            
            self.tail = perseguidor
            self.tail.next = None
            self.length -=1
            if self.length == 0:
                self.head = None
                self.tail = None
            return temp


LL = LinkedList('A')
LL.append('B')
LL.append('C')
LL.append('D')

LL.printing()

D = LL.pop()
print(D.value,'nodo eliminado')
LL.printing()

print('------------')
print('segunda LList')
OneNodeLL = LinkedList('A')
OneNodeLL.printing()
print(OneNodeLL.pop())
OneNodeLL.printing()


print('------------')
print('tercera LList')
TerLL = LinkedList('H')
TerLL.append('I')

print(TerLL.pop())
print(TerLL.pop())
print(TerLL.pop())