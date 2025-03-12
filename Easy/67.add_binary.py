'''
https://leetcode.com/problems/add-binary/
'''

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return f"{int(a, 2) + int(b, 2):b}"
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.addBinary("1", "11"), "100")