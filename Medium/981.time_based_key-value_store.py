'''
https://leetcode.com/problems/time-based-key-value-store/
'''

from collections import defaultdict


class TimeMap:
    def __init__(self):
        self.time_map = defaultdict(list)

        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        keys = self.time_map[key]
        left, right = 0, len(keys)
        
        while left < right:
            mid = (left + right) // 2
            if keys[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        
        return "" if right == 0 else keys[right - 1][1]


if __name__ == "__main__":
    tm = TimeMap()

    print(tm.set("love", "high", 10))
    print(tm.set("love", "low", 20))

    print(tm.get("love", 5))
    print(tm.get("love", 10))
    print(tm.get("love", 15))
    print(tm.get("love", 20))
    print(tm.get("love", 25))