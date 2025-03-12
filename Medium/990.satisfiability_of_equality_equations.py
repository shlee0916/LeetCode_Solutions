'''
https://leetcode.com/problems/satisfiability-of-equality-equations/
'''
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        mapping = {}
        def find(val):
            if val not in mapping:
                return val
            else:
                return find(mapping[val])
            
        for left, eq, _, right in equations:
            if eq == "=":
                x = find(left)
                y = find(right)
                if x != y:
                    mapping[y] = x
                    
        for left, eq, _, right in equations:
            if eq == "!" and find(left) == find(right):
                return False
        
        return True


if __name__ == "__main__":
    sol = Solution()

    print(sol.equationsPossible(["a==b", "b!=c", "c==a"]), False)
    print(sol.equationsPossible(["a==b", "b==c", "a==c"]), True)