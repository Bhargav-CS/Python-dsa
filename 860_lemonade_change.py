from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change_5 = 0
        change_10 = 0
        
        if bills[0] == 10 or bills[0] == 20:
            return False
        
        else:
            for bil in bills:
                if bil == 5:
                    change_5 += 1
                
                elif bil == 10:
                    change_10 += 1
                    change_5 -= 1
                    
                else:
                    
                    change_5 -= 1
                    
                    if change_10 > 0:
                        change_10 -= 1
                    
                    else:
                        change_5 -= 2
                        
                if change_5 < 0 or change_10 < 0:
                    return False
                        
        return True
        
                     
                
        
    
bills = [5,5,5,10,20]
# bills = [5,5,10,10,20]
# bills = [5,5,5,5,20,20,5,5,5,5]
sol = Solution()
print(sol.lemonadeChange(bills))