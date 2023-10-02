'''
https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/description/?envType=daily-question&envId=2023-10-02
'''

class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        count_aaa = count_bbb = 0

        for idx in range(1, len(colors) - 1):
            if colors[idx - 1] == colors[idx] == colors[idx + 1]:
                if colors[idx] == "A":
                    count_aaa += 1
                else:
                    count_bbb += 1

        return count_aaa > count_bbb
    

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.winnerOfGame(colors = "AAABABB")
    assert test1 == True
    
    test2 = sol.winnerOfGame(colors = "AA")
    assert test2 == False
    
    test3 = sol.winnerOfGame(colors = "ABBBBBBBAAA")
    assert test3 == False
    