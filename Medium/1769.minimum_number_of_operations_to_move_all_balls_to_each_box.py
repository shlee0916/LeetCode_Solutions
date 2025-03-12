'''
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/
'''

from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        length = len(boxes)

        left = [0] * length
        left_cnt = int(boxes[0])
        for idx in range(1, length):
            left[idx] = left[idx -  1] + int(left_cnt)
            left_cnt += int(boxes[idx])

        right = [0] * length
        right_cnt = int(boxes[-1])
        for idx in range(length - 2, -1, -1):
            right[idx] = right[idx + 1] + int(right_cnt)
            right_cnt += int(boxes[idx])

        ans = []
        for left_val, right_val in zip(left, right):
            ans.append(left_val + right_val)

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.minOperations(boxes = "110")
    assert test1 == [1, 1, 3]

    test2 = sol.minOperations(boxes = "001011")
    assert test2 == [11, 8, 5, 4, 3, 4]
    