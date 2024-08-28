from collections import Counter

class Solution:
    # Function to sort the array according to frequency of elements.
    def sortByFreq(self, arr: list) -> list:
        # Count the frequency of each element
        freq = Counter(arr)
        
        vec = [(x, freq[x]) for x in arr]
        
        vec.sort(key=lambda x: (-x[1], x[0]))
        
        
        ans = [x[0] for x in vec]
        
        return ans

# Example usage
arr = [9, 9, 9, 2, 5]
sol = Solution()
print(sol.sortByFreq(arr))