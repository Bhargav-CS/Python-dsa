class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        if not head:
            return
        
        slow = head
        fast = head
        
        # Detect the loop using the two-pointer technique
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                # Loop detected, find the starting node of the loop
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                
                # Break the loop
                while fast.next != slow:
                    fast = fast.next
                
                fast.next = None  # Remove the loop
                return