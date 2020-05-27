class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.map = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            self.nums.append(val)
            self.map[val] = len(self.nums) - 1
            return True
        return False
        
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.map:
            return False
        else:
            idxVal = self.map[val]
            last = self.nums[-1]
            self.map[last] = idxVal
            #swap the last two values
            self.swap(self.nums, idxVal, len(self.nums) - 1)
            self.nums.pop()
            del self.map[val]
            return True
        
            

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        import random
        randomNumber = random.randint(0, len(self.nums)-1)
        
        return self.nums[randomNumber]
        
    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()