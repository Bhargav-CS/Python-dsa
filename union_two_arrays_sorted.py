class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,arr1,arr2,n,m):
        '''
        :param a: given sorted array a
        :param n: size of sorted array a
        :param b: given sorted array b
        :param m: size of sorted array b
        :return:  The union of both arrays as a list
        '''
        # code here 
        arr1, arr2 = set(arr1), set(arr2)
        out = list(arr1.union(arr2))
        out.sort()
        return out


n = 5
m = 5
arr1 = [1,2,3,4,5]
arr2 = [1,2,3,6,7]

sol = Solution()
print(sol.findUnion(arr1, arr2, n, m))