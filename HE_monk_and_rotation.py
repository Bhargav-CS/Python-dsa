def rotation(N, K, A):
    x = K%N
    print(*(A[N-x:]+A[:N-x]))

t = int(input())

for i in range(t):
    N, K = input().split()
    N = int(N)
    K = int(K)
    A = list(map(int, input().split()))
    rotation(N, K, A)

    