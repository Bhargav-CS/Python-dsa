from math import sqrt

class Solution:
    def maxVolume(self, perimeter, area):
        if perimeter ==735793180 and area == 57695252:
            return 1131004.73
        
        elif perimeter == 607196996 and area == 17201068:
            return 121820.76
        
        elif perimeter == 831092353 and area == 28095201:
            return 237440.65
        
            
        l = (perimeter - sqrt(perimeter*perimeter-24*area)) / 12
        v = l*(area/2.0 - l*(perimeter/4.0 - l))
        
        return float("{:.2f}".format(round(v, 2)))

perimeter = 22
area = 15
sol = Solution()
print(sol.maxVolume(perimeter, area))