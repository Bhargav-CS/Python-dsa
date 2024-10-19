class Solution:
    def roundToNearest (self, str) : 
            sys.set_int_max_str_digits(70000)
            num = int(str)
            string_value = str
            preceding_zeros = string_value[:len(string_value) - len(string_value.lstrip('0'))]
            
            rem = num % 10
            
            if(rem <= 5):
                num = num - rem
                return (preceding_zeros + f"{num}")
            else:
                num = num + (10 - rem)
                return (preceding_zeros + f"{num}")