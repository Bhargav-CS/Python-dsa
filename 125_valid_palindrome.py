class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #initialize two pointers
        left, right = 0, len(s) - 1
        while left < right:
            #if the left character is not alphanumeric, move to the next character
            if not s[left].isalnum():
                left += 1
            #if the right character is not alphanumeric, move to the previous character
            elif not s[right].isalnum():
                right -= 1
            #if both characters are alphanumeric, check if they are equal
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True

s = "A man, a plan, a canal: Panama"
sol = Solution()
print(sol.isPalindrome(s)) #expected output is True

