from typing import List
import bisect

class Solution:
    def countPairs(self, arr: List[int], brr: List[int]) -> int:
        brr.sort()
        freq = [0] * 5
        for num in brr:
            if num <= 4:
                freq[num] += 1
        
        ans = 0
        for num in arr:
            ans += self.count(num, brr, len(brr), freq)
        
        return ans
    
    def count(self, x: int, brr: List[int], n: int, freq: List[int]) -> int:
        if x == 0:
            return 0
        if x == 1:
            return freq[0]
        
        # Count greater values using binary search
        l = bisect.bisect_right(brr, x)
        ans = n - l
        
        if x == 2:
            return ans + freq[0] + freq[1] - freq[3] - freq[4]
        if x == 3:
            return ans + freq[0] + freq[1] + freq[2]
        return ans + freq[0] + freq[1]

# Example usage
arr = [2, 1, 6]
brr = [1, 5]
sol = Solution()
print(sol.countPairs(arr, brr))  # Expected output: 3