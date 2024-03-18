class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node

    def length(self):
        curr = self.head
        total = 0
        while curr.next != None:
            total += 1
            curr = curr.next
        return total
    
    def display(self):
        elems = []
        curr = self.head
        while curr.next != None:
            curr = curr.next
            elems.append(curr.data)
        print(elems)

    def get(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return None
        curr_idx = 0
        curr = self.head
        while True:
            curr = curr.next
            if curr_idx == index: 
                return curr.data
            curr_idx += 1

    def erase(self, index):
        if index >= self.length() or index < 0:
            print("ERROR: 'Get' Index out of range!")
            return None
        curr_idx = 0
        curr = self.head
        while True:
            last_node = curr
            curr = curr.next
            if curr_idx == index:
                last_node.next = curr.next
                return
            curr_idx += 1



            


my_llist = linked_list()
my_llist.display()
my_llist.append(1)
my_llist.append(2)
my_llist.append(3)
my_llist.append(4)

my_llist.display()
print("Element at 2nd index: %d" % my_llist.get(2))
my_llist.erase(2)
my_llist.display()
