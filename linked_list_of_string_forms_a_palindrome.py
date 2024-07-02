class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

def compute(head):
    # Convert the linked list into a string
    string = ""
    current = head
    while current:
        string += current.data
        current = current.next
    
    # Check if the string is a palindrome
    return string == string[::-1]
    
    
    