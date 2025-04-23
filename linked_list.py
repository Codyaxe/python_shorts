class Node():
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
class LinkedList():
    def __init__(self):
        self.head = None

    def size(self):
        current = self.head
        size = 0
        while current.next:
            current.next
            size += 1
        return size
    
    def prepend(self, data):
        new_node = Node(data)
        if self.head == None:
            new_node.next = None
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
    
    def removebeginning(self):
        if self.head == None:
            return print("Linked List is empty!")
        self.head = self.head.next

    def removeend(self):
        if self.head == None:
            return print("Linked List is empty!")
        if self.head.next == None:
            self.head = None
            return
        point = self.head
        point_two = self.head.next
        while point_two.next:
            point = point.next
            point_two = point_two.next
        point.next = None

    def removeat(self, index):
        if self.head is None:
            print("Linked List is empty!")
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(index - 1):
            if current.next is None:
                print("Index out of bounds!")
                return
            current = current.next
        if current.next is None:
            print("Index out of bounds!")
            return
        current.next = current.next.next
        
    def insert(self, data, index):
        new_node = Node(data)
        current = self.head
        for i in range(index - 1):
            current = current.next
        new_node.next = current.next
        current.next = new_node