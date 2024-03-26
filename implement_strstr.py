# implementation without using inbuilt functions
def strstr(s,x):
    for i in range(len(s)):
        if s[i:i+len(x)] == x:
            return i
    return -1
        

s = "ababaaaaaa"
x = "abaa"
print(strstr(s,x)) # 5

# print(s.find(x)) # 5 