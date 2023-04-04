'''
https://leetcode.com/problems/optimal-partition-of-string/solutions/?orderBy=most_votes
'''

class Solution:
    def partitionString(self, s: str) -> int:
        new_strings = []

        for ch in s:
            if new_strings and ch not in new_strings[-1]:
                new_strings[-1] += ch
            else:
                new_strings.append(ch)

        return len(new_strings)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.partitionString(s = "abacaba")
    assert test1 == 4

    test2 = sol.partitionString(s = "ssssss")
    assert test2 == 6
    