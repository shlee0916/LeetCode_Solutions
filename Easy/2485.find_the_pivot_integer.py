'''
https://leetcode.com/problems/find-the-pivot-integer/description/?envType=daily-question&envId=2024-03-13
'''

class Solution:
    def pivotInteger(self, n: int) -> int:
        prefixes = [1]
        for num in range(2, n + 1):
            prefixes.append(prefixes[-1] + num)

        ans = -1
        for idx, prefix_num in enumerate(prefixes):
            if prefix_num == prefixes[-1] - prefix_num + idx + 1:
                ans = idx + 1
                break

        return ans
        

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.pivotInteger(n = 8)
    assert test1 == 6

    test2 = sol.pivotInteger(n = 1)
    assert test2 == 1

    test3 = sol.pivotInteger(n = 4)
    assert test3 == -1
    