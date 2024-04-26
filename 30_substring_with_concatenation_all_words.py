class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words:
            return []

        word_len = len(words[0])
        total_words = len(words)
        window_size = word_len * total_words
        result = []

        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        for i in range(len(s) - window_size + 1):
            curr_count = {}
            j = 0

            while j < window_size:
                curr_word = s[i + j:i + j + word_len]
                if curr_word not in word_count:
                    break

                curr_count[curr_word] = curr_count.get(curr_word, 0) + 1
                if curr_count[curr_word] > word_count[curr_word]:
                    break

                j += word_len

            if j == window_size:
                result.append(i)

        return result

s = "barfoothefoobarman"
words = ["foo", "bar"]
sol = Solution()
print(sol.findSubstring(s, words)) # [0, 9] or [9, 0]

