import random
class RandomizedSet:
    def __init__(self):
        self.number_set = set()

    def insert(self, val: int) -> bool:
        if val in self.number_set:
            return False
        self.number_set.add(val)
        return True
        
    def remove(self, val: int) -> bool:
        if val in self.number_set:
            self.number_set.remove(val)
            return True
        return False
        
    def getRandom(self) -> int:
        return random.choice(list(self.number_set))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()