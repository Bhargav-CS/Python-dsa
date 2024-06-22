class Solution:
    def ExtractNumber(self, sentence:str):
        sentence = sentence.split()
        out = []
        for ele in sentence:
            if ele.isdigit():
                if "9" not in ele:
                    out.append(int(ele))
        
        if out:
            return max(out)
        else:
            return -1

# sentence  = "This is alpha 5057 and 97"
# sentence  = "zg 9 e 12 b 16 10 8 10 l 7"
sentence  = "Another input 9007"
sol = Solution()
print(sol.ExtractNumber(sentence))
