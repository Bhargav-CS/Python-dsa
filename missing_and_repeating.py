import heapq

class Solution:
    
    def findTwoElement(self, arr):
        heapq.heapify(arr)
        
        i = 1
        
        while arr:
            num = heapq.heappop(arr)
            print(i, num)
            
            if i != num:
                if i > num:
                    B = num
                    print("B is",B)
                    i -= 1
                
                else:
                    A = i
                    print("A is", A)
                    heapq.heappush(arr, num)
                    
            i += 1
    
        try:
            return B, A
        
        except UnboundLocalError:
            return B, i
            
        
    

# arr = [2, 2]    
# arr = [1, 3, 3]
# arr = [1, 2, 3, 4, 5, 6, 3, 8, 9]
# arr = [2, 21, 17, 16, 22, 3, 9, 10, 14, 12, 20, 11, 6, 4, 8, 7, 23, 15, 18, 13, 1, 10, 19]
arr = [12, 7, 5, 1, 13, 1, 10, 8, 11, 9, 2, 4, 3, 6]
sol = Solution()
print(sol.findTwoElement(arr))
