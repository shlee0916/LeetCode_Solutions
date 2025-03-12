'''
https://leetcode.com/problems/excel-sheet-column-title/
'''

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = ""
        while columnNumber > 0:
            columnNumber -= 1
            ans = chr(65 + columnNumber % 26) + ans
            columnNumber = columnNumber // 26
            
        return ans
    

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.convertToTitle(3))