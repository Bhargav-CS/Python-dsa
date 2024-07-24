def is_subsequence(S1, Q):
    it = iter(Q)
    return all(char in it for char in S1)

def solve(N, S1, M, S2, P):
    left, right = 0, M
    answer = -1
    while left <= right:
        mid = (left + right) // 2
        Q = ['*'] * M
        for i in range(mid):
            Q[P[i] - 1] = S2[P[i] - 1]
        if is_subsequence(S1, Q):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    results = []
    
    for _ in range(T):
        N = int(data[index])
        index += 1
        S1 = data[index]
        index += 1
        M = int(data[index])
        index += 1
        S2 = data[index]
        index += 1
        P = list(map(int, data[index:index + M]))
        index += M
        result = solve(N, S1, M, S2, P)
        results.append(result)
    
    for result in results:
        print(result)

if _name_ == "_main_":
    main()