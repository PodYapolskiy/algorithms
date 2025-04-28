import random


class RandomizedSet:
    def __init__(self):
        self.arr = []  # [val, val, ...]
        self.map = {}  # {val: index in arr}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False

        self.map[val] = len(self.arr)
        self.arr.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False

        # swap val object with last
        idx = self.map[val]
        self.arr[idx] = self.arr[-1]
        self.map[self.arr[-1]] = idx

        # pop val as it is last elem
        self.arr.pop()
        del self.map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
