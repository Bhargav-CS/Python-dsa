class Solution:
    def insertAtBottom(self,st,x):
        st.insert(0, x)
        return st


st = [4, 3, 2, 1, 8]
x = 2
sol = Solution()
print(sol.insertAtBottom(st, x)) 