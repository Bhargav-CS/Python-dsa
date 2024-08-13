class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split(".")))
        version2 = list(map(int, version2.split(".")))

        if len(version1) < len(version2):
            version1.extend([0] * (len(version2)- len(version1)))
            
        elif len(version2) < len(version1):
            version2.extend([0] * (len(version1)- len(version2)))
            
        for i in range(len(version1)):
            
            if version1[i] < version2[i]:
                return -1
            
            elif version1[i] > version2[i]:
                return 1
            
            elif version1[i] == version2[i] and i == len(version1) - 1:
                return 0
            
            
            
# version1 = "1.2"
# version2 = "1.10"

# version1 = "1.0"
# version2 = "1.0.0.0"

version1 = "1.01"
version2 = "1.001"

sol = Solution()
print(sol.compareVersion(version1, version2))
