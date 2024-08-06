class Solution:
    def isValid(self, str:str):
        try:
            str = str.split(".")
            print(str)
            
            if len(str) != 4:
                return False
            
            for ele in str:
                if ele.startswith("0") and int(ele) != 0 :
                    return False
                
                if int(ele) < 0 or int(ele) > 255:
                    return False
                
            return True
        
        except ValueError:
            return False
    
str = "222.111.111.111"
# str = "5555..555"
# str = "01.01.01.01"
str = "255..255.255"
sol = Solution()
print(sol.isValid(str))

