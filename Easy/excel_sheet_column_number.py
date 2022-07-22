'''
https://leetcode.com/problems/excel-sheet-column-number/
'''

class Solution:
    __alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def titleToNumber(self, column_title: str) -> int:
        length = 0
        for idx, ch in enumerate(column_title[::-1]):
            length += (26**(idx)) * (self.__alpha.index(ch) + 1)
            
        return length


if __name__ == "__main__":
    sol = Solution()

    print(sol.titleToNumber("A"), 1)
    print(sol.titleToNumber("AAB"), 704)