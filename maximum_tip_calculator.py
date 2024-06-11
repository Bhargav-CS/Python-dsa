from typing import List

class Solution:
    def maxTip(self, n: int, x: int, y: int, arr: List[int], brr: List[int]) -> int:
        v = sorted([(abs(a - b), (a, b)) for a, b in zip(arr, brr)], reverse=True)
        
        print(v)
        
        ans = 0
        for _, (a, b) in v:
            print(f"Current values: x={x}, y={y}, a={a}, b={b}")
            if x == 0:
                ans += b
                y -= 1
                print(f"Adding b={b} to ans. Remaining y={y}")
            elif y == 0:
                ans += a
                x -= 1
                print(f"Adding a={a} to ans. Remaining x={x}")
            else:
                if a > b:
                    ans += a
                    x -= 1
                    print(f"Adding a={a} to ans. Remaining x={x}")
                else:
                    ans += b
                    y -= 1
                    print(f"Adding b={b} to ans. Remaining y={y}")
        return ans


n = 5
x = 3
y = 3
arr = [1, 2, 3, 4, 5]
brr = [5, 4, 3, 2, 1]

sol = Solution()
print(sol.maxTip(n, x, y, arr, brr))