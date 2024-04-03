def rotate( arr, n):
    arr.insert(0, arr.pop())
    return arr


n = 5
arr = [1, 2, 3, 4, 5]
print(rotate(arr, n))

# arr.append(arr.pop(0))
# arr.