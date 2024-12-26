    def twoSum(self, arr, target):
        # code here
        ch={}
        for i in arr:
            if target-i in ch:
                return True
            ch[i]=True
        return False