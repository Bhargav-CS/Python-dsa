# a = [1,3,5]
# n = 3
# sum = 0


# for i in range(n):
#     for j in range(n):
#         sum += bin(a[i]^a[j]).count('1')
        
# print(sum)

#User function Template for python3
class Solution:
    def sumBitDiff(self, arr, n):
        total_sum = 0
        for i in range(32):  # Assuming integers are 32-bit
            count = 0
            for j in range(n):
                if (arr[j] & (1 << i)):
                    count += 1
            total_sum += count * (n - count) * 2
        return total_sum

