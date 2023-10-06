'''
https://leetcode.com/problems/design-hashset/description/?envType=daily-question&envId=2023-10-06
'''

class MyHashSet:
    
    def __init__(self):
        self.size = 10000
        self.data = [[] for _ in range(self.size)]


    def add(self, key: int) -> None:
        data, idx = self.__index(key)

        if idx == -1:
            data.append(key)


    def remove(self, key: int) -> None:
        data, idx = self.__index(key)

        if idx != -1:
            data.remove(key)
        

    def contains(self, key: int) -> bool:
        data, idx = self.__index(key)

        return key in data


    def __hasing(self, key):
        return key % self.size

    
    def __index(self, key):
        hasing = self.__hasing(key)

        data = self.data[hasing]

        for idx, k in enumerate(data):
            if k == key:
                return data, idx
        
        return data, -1


if __name__ == "__main__":
    hash = MyHashSet()
    
    hash.add(1)
    hash.add(2)
    assert hash.contains(3) == False
    assert hash.contains(2) == True
    hash.add(2)
    assert hash.contains(2) == True
    hash.remove(2)
    assert hash.contains(2) == False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)