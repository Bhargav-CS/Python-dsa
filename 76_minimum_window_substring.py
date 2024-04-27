class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        required_chars = len(t_count)
        formed_chars = 0
        window_start = 0
        window_size = float('inf')
        result = ""
        
        curr_count = {}
        for window_end in range(len(s)):
            curr_char = s[window_end]
            curr_count[curr_char] = curr_count.get(curr_char, 0) + 1
            
            if curr_char in t_count and curr_count[curr_char] == t_count[curr_char]:
                formed_chars += 1
            
            while formed_chars == required_chars:
                if window_end - window_start + 1 < window_size:
                    window_size = window_end - window_start + 1
                    result = s[window_start:window_end + 1]
                
                left_char = s[window_start]
                if left_char in t_count and curr_count[left_char] == t_count[left_char]:
                    formed_chars -= 1
                
                curr_count[left_char] -= 1
                window_start += 1
        
        return result
    

s = "ADOBECODEBANC"
t = "ABC"
sol = Solution()
print(sol.minWindow(s,t))