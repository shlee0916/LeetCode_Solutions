'''
https://leetcode.com/problems/path-crossing/description/?envType=daily-question&envId=2023-12-23
'''

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        cur_point = (0, 0)
        visit = set([cur_point])

        for next_dir in path:
            if next_dir == "N":
                cur_point = (cur_point[0], cur_point[1] + 1)
            elif next_dir == "S":
                cur_point = (cur_point[0], cur_point[1] - 1)
            elif next_dir == "E":
                cur_point = (cur_point[0] - 1, cur_point[1])
            elif next_dir == "W":
                cur_point = (cur_point[0] + 1, cur_point[1])

            if cur_point in visit:
                return True
            
            visit.add(cur_point)

        return False


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.isPathCrossing(path = "NES")
    assert test1 == False
    
    test2 = sol.isPathCrossing(path = "NESWW")
    assert test2 == True
    