'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        '''
        head1:  head of linkedList 1
        head2:  head of linkedList 2
        n1:  len of  linkedList 1
        n2:  len of linkedList 1
        x:   given sum
        '''
        count = 0
        # Create a set to store the values of linkedList 2
        values = set()
        
        # Traverse the second linked list and store the values in the set
        curr2 = head2
        while curr2:
            values.add(curr2.data)
            curr2 = curr2.next
        
        # Traverse the first linked list
        curr1 = head1
        while curr1:
            # Check if the complement of current node's value exists in the set
            complement = x - curr1.data
            if complement in values:
                count += 1
            curr1 = curr1.next

        return count


