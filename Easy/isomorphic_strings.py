'''
https://leetcode.com/problems/isomorphic-strings/
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.isIsomorphic("foo", "bar"))
    print(sol.isIsomorphic("abb", "egg"))