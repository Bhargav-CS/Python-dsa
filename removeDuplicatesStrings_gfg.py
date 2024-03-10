class Solution:

    
    def removeDuplicates(self, str):
        # code here
        temp = ""
        for i in str:
            if i not in temp:
                temp += i
        return temp

sol = Solution()
print(sol.removeDuplicates("geeksforgeeks")) # geeksfor