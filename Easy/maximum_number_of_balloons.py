'''
https://leetcode.com/problems/maximum-number-of-balloons/
'''
from collections import Counter


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        cnt = Counter(text)
        cnt_balloon = Counter("balloon")
        return min([cnt[c] // cnt_balloon[c] for c in cnt_balloon])
    
    
if __name__ == "__main__":
    sol = Solution()
    
    print(sol.maxNumberOfBalloons("nlaebolko"), 1)
    print(sol.maxNumberOfBalloons("loonbalxballpoon"), 2)