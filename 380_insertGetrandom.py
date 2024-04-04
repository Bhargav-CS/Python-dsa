import random
class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.data_dict = {}
        self.data_len = 0
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.data_dict:
            return False
        self.data.append(val)
        self.data_dict[val] = self.data_len
        self.data_len += 1
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.data_dict:
            return False
        index = self.data_dict[val]
        last_element = self.data[-1]
        self.data[index] = last_element
        self.data_dict[last_element] = index
        self.data.pop()
        del self.data_dict[val]
        self.data_len -= 1
        return True
        

    def getRandom(self):
        """
        :rtype: int
        """
        return self.data[random.randint(0, self.data_len - 1)]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()