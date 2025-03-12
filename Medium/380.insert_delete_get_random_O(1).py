'''
https://leetcode.com/problems/insert-delete-getrandom-o1/description/
'''

import random


class RandomizedSet:

    def __init__(self):
        self._set = set()

    def insert(self, val: int) -> bool:
        if val in self._set:
            return False
        else:
            self._set.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self._set:
            self._set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(list(self._set))


if __name__ == "__main__":
    sol = RandomizedSet()

    assert sol.insert(1) == True
    assert sol.insert(1) == False
    assert sol.insert(2) == True
    assert sol.insert(3) == True

    assert sol.remove(4) == False
    assert sol.remove(3) == True

    assert sol.insert(4) == True
    assert sol.insert(3) == True

    # Probability test
    test = {1: 0, 2: 0, 3: 0, 4: 0}
    for _ in range(1000000):
        test[sol.getRandom()] += 1

    print(test)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
