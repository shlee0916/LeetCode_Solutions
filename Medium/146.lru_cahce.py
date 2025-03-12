'''
https://leetcode.com/problems/lru-cache/description/
'''

from collections import OrderedDict


class LRUCache:

    def __init__(self, capacity: int):
        self.limit = capacity
        self.cache = OrderedDict()


    def get(self, key: int) -> int:
        value = -1
        if key not in self.cache:
            return value

        value = self.cache[key]
        self.cache.move_to_end(key)

        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            del self.cache[key]

        self.cache[key] = value
        if len(self.cache) > self.limit:
            self.cache.popitem(last = False)


if __name__ == "__main__":
    cache = LRUCache(2)
    
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)