class Solution:
    def kthElement(self, k, arr1, arr2):
        arr1.extend(arr2)
        arr1.sort()
        print(arr1)
        return arr1[k-1]
    

class Solution:

    def kthElement(self, a, b, k):
        
        a.extend(b)
        a.sort()
        return a[k-1]


k = 5
arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
sol = Solution()
print(sol.kthElement(k, arr1, arr2))