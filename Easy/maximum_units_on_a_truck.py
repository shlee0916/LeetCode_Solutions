'''
https://leetcode.com/problems/maximum-units-on-a-truck/description/
'''

from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        box_types = boxTypes
        box_types.sort(key = lambda x: -x[1])
        truck_size = truckSize
        
        ans = 0
        for num_box, unit_num in box_types:
            if truck_size > num_box:
                truck_size -= num_box
                ans += unit_num * num_box
            else:
                ans += unit_num * truck_size
                break

        return ans


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.maximumUnits(boxTypes = [[1, 3], [2, 2], [3, 1]], truckSize = 4)
    assert test1 == 8
    
    test2 = sol.maximumUnits(boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]], truckSize = 10)
    assert test2 == 91
    