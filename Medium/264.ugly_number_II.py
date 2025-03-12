'''
https://leetcode.com/problems/ugly-number-ii/description/
'''

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        idxs = [0, 0, 0] # 2, 3, 5
        while len(res) < n:
            tmp = [res[idxs[0]] * 2, res[idxs[1]] * 3, res[idxs[2]] * 5]
            next_prime = min(tmp)
            idxs[tmp.index(next_prime)] += 1
            if next_prime not in res:
                res.append(next_prime)

        return res[-1]


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.nthUglyNumber(10)
    print(test1, 12)
    assert test1 == 12

    test2 = sol.nthUglyNumber(1)
    print(test2, 1)
    assert test2 == 1
