def maxProduct(self,arr):
        # code here
        n = len(arr)
        maxProd = arr[0]
        minProd = arr[0]
        result = arr[0]

        for i in range(1, n):
            if arr[i] < 0:
                maxProd, minProd = minProd, maxProd

            maxProd = max(arr[i], maxProd * arr[i])
            minProd = min(arr[i], minProd * arr[i])

            result = max(result, maxProd)

        return result