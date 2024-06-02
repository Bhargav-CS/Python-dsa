class Solution:
    #Function to check if a string can be obtained by rotating
    #another string by exactly 2 places.
    def isRotated(self,str1,str2):
        #code here
        str1 = str1 + str1
        print("string 1 is: ", str1)
        print("string 2 is: ", str2)
        print("string 1[2:] is: ", str1[2:len(str2)+ 2])
        print("string 1[:-2] is: ", str1[len(str2)-2:-2])
        
        if str1[2:len(str2)+ 2] == str2 or str1[len(str2)-2:-2] == str2:
            return 1
        return 0

# str1 = "amazon"
# str2 = "azonam"
str1 = "daxjheq"
str2 = "eqdaxjh"
sol = Solution()
print(sol.isRotated(str1, str2)) # Output: 1
