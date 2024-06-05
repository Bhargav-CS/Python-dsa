
class Solution:
    def findSwapValues(self,a, n, b, m):
        # Your code goes here
        sum_a = sum(a)
        sum_b = sum(b)
        
        hashmap ={}
        
        if sum_a > sum_b:
            req = (sum_a - sum_b) // 2
            if req % 2 !=0:
                return -1
            
            for i in range(n):
                hashmap[a[i]] = a[i] - req
        
        else:
            req = (sum_b - sum_a) // 2
            if req%2 != 0:
                return -1
            
            for i in range(n):
                hashmap[a[i]] = a[i] + req
            
        for ele in hashmap.values():
            if ele in b:
                return 1
            else:
                return -1
                
    
# n = 6
# m = 4
# a = [4, 1, 2, 1, 2, 2]
# b = [3, 6, 3, 3]

n = 4
m = 4
a = [5, 7, 4, 6]
b = [1, 2, 3, 8]
sol = Solution()
print(sol.findSwapValues(a, n, b, m))

# sum_a = sum(a)
# sum_b = sum(b)

# print(sum_a)
# print(sum_b)

# hashmap = {}

# if sum_a > sum_b:
#     req = (sum_a - sum_b) // 2
#     if req %2 != 0:
#         print("req is:", req)
#     for i in range(n):
#         hashmap[a[i]] = a[i] - req  
        
# else:
#     req = (sum_b - sum_a) // 2
#     if req%2 != 0:
#         print("req is: ", req)
#     for i in range(n):
#         hashmap[a[i]] = a[i] + req

# print("hashmap: ", hashmap)
# print("req: ", req)
# for ele in hashmap.values():
#     if ele in b:
#         print(1)
#     else:
#         print(-1)
        




