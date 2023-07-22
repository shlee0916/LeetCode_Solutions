'''
https://leetcode.com/problems/slowest-key/description/
'''

from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        key = keysPressed[0]
        time = releaseTimes[0]

        for idx in range(1, len(keysPressed)):
            new_time = releaseTimes[idx] - releaseTimes[idx - 1]
            if new_time > time or (new_time == time and keysPressed[idx] > key):
                time = new_time
                key = keysPressed[idx]

        return key


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.slowestKey(releaseTimes = [9, 29, 49, 50], keysPressed = "cbcd")
    assert test1 == "c"
    
    test2 = sol.slowestKey(releaseTimes = [12, 23, 36, 46, 62], keysPressed = "spuda")
    assert test2 == "a"
    