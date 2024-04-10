class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_num = ""
        roman_dict = {
            1: "I", 4: "IV", 5: "V", 9: "IX", 10: "X", 40: "XL",
            50: "L", 90: "XC", 100: "C", 400: "CD", 500: "D",
            900: "CM", 1000: "M"
        }
        roman_keys = sorted(roman_dict.keys(), reverse=True)
        for key in roman_keys:
            while num >= key:
                roman_num += roman_dict[key]
                num -= key
        return roman_num

num = 3
sol = Solution()
print(sol.intToRoman(num)) # III