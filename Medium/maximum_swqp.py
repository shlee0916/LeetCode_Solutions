'''
https://leetcode.com/problems/maximum-swap/?envType=daily-question&envId=2024-10-17
'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = [int(ch) for ch in str(num)]
        max_idx = len(nums) - 1
        left = 0
        right = 0
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] > nums[max_idx]:
                max_idx = idx
            elif nums[idx] < nums[max_idx]:
                left = idx
                right = max_idx

        nums[left], nums[right] = nums[right], nums[left]

        return int("".join(str(num) for num in nums))


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.maximumSwap(num = 2736)
    assert test1 == 7236

    test2 = sol.maximumSwap(num = 9973)
    assert test2 == 9973
    