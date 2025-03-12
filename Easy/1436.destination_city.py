'''
https://leetcode.com/problems/destination-city/description/
'''

from typing import List


class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        begin_city, end_city = map(set, zip(*paths))
        
        return (end_city - begin_city).pop()


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.destCity(paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]])
    assert test1 == "Sao Paulo"
    
    test2 = sol.destCity(paths = [["B", "C"], ["D", "B"], ["C", "A"]])
    assert test2 == "A"
    
    test3 = sol.destCity(paths = [["A", "Z"]])
    assert test3 == "Z"
    