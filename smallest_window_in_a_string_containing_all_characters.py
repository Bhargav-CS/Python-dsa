class Solution:
    
    def smallestWindow(self, s, p):
        p_dict = {}
        s_dict = {}
        
        for i in p:
            if i in p_dict:
                p_dict[i] += 1
                
            else:
                p_dict[i] = 1
        
        start = 0
        end = 0
        min_len = float("inf")
        count = 0
        start_index = -1
        
        for end in range(len(s)):
            if s[end] in s_dict:
                s_dict[s[end]] += 1
                
            else:
                s_dict[s[end]] = 1
                
            if s[end] in p_dict and s_dict[s[end]] <= p_dict[s[end]]:
                count += 1
                
            if count == len(p):
                while s[start] not in p_dict or s_dict[s[start]] > p_dict[s[start]]:
                    if s[start] in p_dict and s_dict[s[start]] > p_dict[s[start]]:
                        s_dict[s[start]] -= 1
                        
                    start += 1
                
                window_len = end - start + 1
                
                if min_len > window_len:
                    min_len = window_len
                    start_index = start
        
        if start_index == -1:
            return -1
        
        return s[start_index:start_index + min_len]
    
    
s = "timetopractice"
p = "toc"
sol = Solution()
print(sol.smallestWindow(s, p))