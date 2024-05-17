'''
https://leetcode.com/problems/minimum-penalty-for-a-shop/description/
'''

class Solution:
    def bestClosingTime(self, customers: str) -> int:
        hour = 0
        max_profit = 0
        cur_profit = 0

        for idx, custom in enumerate(customers):
            if custom == "Y":
                cur_profit += 1
            else:
                cur_profit -= 1

            if cur_profit > max_profit:
                max_profit = cur_profit
                hour = idx + 1

        return hour
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.bestClosingTime(customers = "NNNNN")
    assert test1 == 0

    test2 = sol.bestClosingTime(customers = "YYYY")
    assert test2 == 4
    