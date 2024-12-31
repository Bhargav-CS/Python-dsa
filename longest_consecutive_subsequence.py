    def longestConsecutive(self, arr):
        unused = set(arr)
        max_len = 0
        for a in arr:
            if a not in unused:
                continue
            unused.remove(a)
            length = 1
            smaller = a - 1
            while smaller in unused:
                length += 1
                unused.remove(smaller)
                smaller -= 1
            bigger = a + 1
            while bigger in unused:
                length += 1
                unused.remove(bigger)
                bigger += 1
            max_len = max(max_len, length)
        return max_len