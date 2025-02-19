'''
https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/?envType=daily-question&envId=2025-02-19
'''

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        ans = []
        def _helper(cur_str, target_len):
            if len(cur_str) == target_len:
                ans.append(cur_str)
            else:
                for ch in ("a", "b", "c"):
                    if ch != cur_str[-1]:
                        _helper(cur_str + ch, target_len)
        
        for ch in ("a", "b", "c"):
            _helper(ch, n)

        return ans[k - 1] if len(ans) >= k else ""


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.getHappyString(n = 1, k = 3)
    assert test1 == "c"

    test2 = sol.getHappyString(n = 1, k = 4)
    assert test2 == ""

    test3 = sol.getHappyString(n = 3, k = 9)
    assert test3 == "cab"
    