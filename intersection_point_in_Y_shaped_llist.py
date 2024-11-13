def intersetPoint(head1,head2):
    #code here
    
    # checking the base case
    if not head1 or not head2:
        return None
    
    # Creating the dictionary
    d={}
    
    #storing the address of first list in to the dictionry for easy access
    temp=head1
    while temp:
        d[temp]=temp.data
        temp=temp.next
        
    # Checking: If the address of list 2 was in list one if so then the data of that addrees will be the answer    
    temp1=head2
    while temp1:
        if temp1 in d:
            return temp1.data
        else:
            temp1=temp1.next