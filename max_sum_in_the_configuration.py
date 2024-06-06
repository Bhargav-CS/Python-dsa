def max_sum(a, n):
    sum = 0
    for i in range(n):
        sum += a[i]
    curr_val = 0
    for i in range(n):
        curr_val += i * a[i]
    res = curr_val
    for i in range(1, n):
        next_val = (curr_val - (sum - a[i - 1]) + a[i - 1] * (n - 1))
        curr_val = next_val
        res = max(res, next_val)
    return res
    

n = 3
a = [8, 3, 1, 2]
a = [1, 2, 3]
print(max_sum(a, n)) # 29
