'''
https://leetcode.com/problems/reverse-string/
'''
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for idx, ch in enumerate(s[:len(s) // 2]):
            s[idx] = s[len(s) - idx - 1]
            s[len(s) - idx - 1] = ch


if __name__ == "__main__":
    sol = Solution()

    test_case1 = ["h","e","l","l","o"]
    test_case2 = ["H","a","n","n","a","h"]
    sol.reverseString(test_case1)
    sol.reverseString(test_case2)

    print(test_case1, ["o","l","l","e","h"])
    print(test_case2, ["h","a","n","n","a","H"])


#### Today I got Java solution too
'''
class Solution {
    public void reverseString(char[] s) {
        for (int idx = 0; idx < s.length / 2; idx++) {
            char tmp = s[idx];
            s[idx] = s[s.length - idx - 1];
            s[s.length - idx - 1] = tmp;
        }
    }
}
'''