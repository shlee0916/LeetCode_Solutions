'''
https://leetcode.com/problems/find-the-winner-of-the-circular-game/description/
'''

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = [idx + 1 for idx in range(n)]

        friends_pos = 0
        while len(friends) > 1:
            friends_pos = (friends_pos + k - 1) % len(friends)
            friends.pop(friends_pos)

        return friends[0]
    

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findTheWinner(n = 5, k = 2)
    assert test1 == 3
    
    test2 = sol.findTheWinner(n = 6, k = 5)
    assert test2 == 1
    