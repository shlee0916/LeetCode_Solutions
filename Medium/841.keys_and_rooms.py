'''
https://leetcode.com/problems/keys-and-rooms/
'''
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = []
        keys.extend(rooms[0])
        
        visit = {key: 0 for key in range(len(rooms))}
        visit[0] = 1
        
        while keys:
            cur_key = keys.pop()
            if visit[cur_key] == 0:
                keys.extend(rooms[cur_key])
                visit[cur_key] = 1
            
        return all(visit.values())
    

if __name__ == "__main__":
    sol = Solution()
    
    print(sol.canVisitAllRooms([[1], [2], [3], []]), True)
    print(sol.canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]), False)