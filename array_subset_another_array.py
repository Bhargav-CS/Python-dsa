def isSubset(a1, a2, n, m):
    freq = {}
    for i in range(n):
        if a1[i] in freq:
            freq[a1[i]] += 1
        else:
            freq[a1[i]] = 1

    for i in range(m):
        if a2[i] not in freq or freq[a2[i]] == 0:
            return "No"
        else:
            freq[a2[i]] -= 1

    return "Yes"
    

a1 = [1, 2, 3, 4, 4, 5, 6]
a2 = [1, 2, 4]

sol = isSubset(a1, a2, len(a1), len(a2))
print(sol) # True

# for i in range(len(a2)):
#     if a2[i] not in a1:
#         print(a2[i])