class Solution:
    def nearlySorted(self, arr, k):
        # Create a min-heap
        min_heap = []
        n = len(arr)

        # Step 1: Add the first k+1 elements to the heap
        for i in range(min(k + 1, n)):
            heapq.heappush(min_heap, arr[i])

        # Step 2: Process the rest of the elements
        index = 0
        for i in range(k + 1, n):
            # Extract the minimum element from the heap
            arr[index] = heapq.heappop(min_heap)
            index += 1
            # Add the next element from the array to the heap
            heapq.heappush(min_heap, arr[i])

        # Step 3: Extract remaining elements from the heap
        while min_heap:
            arr[index] = heapq.heappop(min_heap)
            index += 1