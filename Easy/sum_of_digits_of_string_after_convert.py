'''
https://leetcode.com/problems/sum-of-digits-of-string-after-convert/?envType=daily-question&envId=2024-09-03
'''

class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nums = []
        for ch in s:
            nums.extend(int(num) for num in str(ord(ch) - ord("a") + 1))

        for idx in range(k):
            if len(nums) == 1:
                break
            nums = [int(num) for num in str(sum(nums))]

        return int("".join(list(map(str, nums))))


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.getLucky(s = "iiii", k = 1)
    assert test1 == 36

    test2 = sol.getLucky(s = "leetcode", k = 2)
    assert test2 == 6

    test3 = sol.getLucky(s = "zbax", k = 2)
    assert test3 == 8
    