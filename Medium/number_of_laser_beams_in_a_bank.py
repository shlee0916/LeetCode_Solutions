'''
https://leetcode.com/problems/number-of-laser-beams-in-a-bank/description/
'''

from typing import List


class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        total_laser = 0
        prev_laser_device = bank[0].count("1")

        for idx, row in enumerate(bank[1:]):
            cur_laser_device = row.count("1")

            if cur_laser_device > 0:
                total_laser += prev_laser_device * cur_laser_device
                prev_laser_device = cur_laser_device

        return total_laser


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.numberOfBeams(bank = ["011001", "000000", "010100", "001000"])
    assert test1 == 8
    
    test2 = sol.numberOfBeams(bank = ["000", "111", "000"])
    assert test2 == 0
    