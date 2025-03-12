'''
https://leetcode.com/problems/merge-intervals/description/
'''
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda ele: ele[0])
        merged = [intervals[0]]

        for inter in intervals[1:]:
            if merged[-1][1] >= inter[0]:
                tmp_inter = merged.pop()
                tmp_inter[1] = max(inter[1], tmp_inter[1])
                merged.append(tmp_inter)
            else:
                merged.append(inter)

        return merged
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    print(test1, [[1, 6], [8, 10], [15, 18]])
    assert test1 == [[1, 6], [8, 10], [15, 18]]
    
    test2 = sol.merge([[1, 4], [4, 5]])
    print(test2, [[1, 5]])
    assert test2 == [[1, 5]]
    
    test3 = sol.merge([[1, 4], [0, 4]])
    print(test3, [[0, 4]])
    assert test3 == [[0, 4]]
    