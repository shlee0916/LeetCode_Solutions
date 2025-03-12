'''
https://leetcode.com/problems/design-hashmap/description/?envType=daily-question&envId=2023-10-04
'''

class ListNode:
    def __init__(self, key: int, value: int, next = None):
        self.key = key
        self.value = value
        self.next = next


class MyHashMap:
    def __init__(self):
        self.size = 997
        self.map = [None for _ in range(self.size)]
        

    def __hasing(self, key):
        return key % self.size


    def put(self, key: int, value: int) -> None:
        hasing_key = self.__hasing(key)

        if self.map[hasing_key] == None:
            self.map[hasing_key] = ListNode(key = key, value = value)
        else:
            cur_node = self.map[hasing_key]
            while cur_node:
                if cur_node.key == key:
                    cur_node.value = value
                    return
                elif cur_node.next == None:
                    break
                else:
                    cur_node = cur_node.next

            cur_node.next = ListNode(key = key, value = value)
        

    def get(self, key: int) -> int:
        hasing_key = self.__hasing(key)

        cur_node = self.map[hasing_key]
        while cur_node:
            if cur_node.key == key:
                return cur_node.value
            cur_node = cur_node.next

        return -1
        

    def remove(self, key: int) -> None:
        hasing_key = self.__hasing(key)

        prev_node = cur_node = self.map[hasing_key]

        if cur_node is None:
            return

        if cur_node.key == key:
            self.map[hasing_key] = cur_node.next
        else:
            cur_node = cur_node.next
            while cur_node:
                if cur_node.key == key:
                    prev_node.next = cur_node.next
                    break
                cur_node, prev_node = cur_node.next, prev_node.next

        return None


if __name__ == "__main__":
    mhm = MyHashMap()

    mhm.put(1, 1)
    mhm.put(2, 2)
    assert mhm.get(1) == 1
    assert mhm.get(3) == -1
    mhm.put(2, 1)
    assert mhm.get(2) == 1
    mhm.remove(2)
    assert mhm.get(2) == -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,val)
# param_2 = obj.get(key)
# obj.remove(key)