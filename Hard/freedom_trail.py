'''
https://leetcode.com/problems/freedom-trail/description/?envType=daily-question&envId=2024-04-28
'''

from collections import defaultdict


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)
        ans = [0] * ring_len

        ch_idxs = defaultdict(list)
        for idx, ch in enumerate(ring):
            ch_idxs[ch].append(idx)
        
        for idx in ch_idxs[key[0]]:
            ans[idx] = min(idx, ring_len - idx) + 1

        pre_ch = key[0]
        for ch in key[1:]:
            for cur_idx in ch_idxs[ch]:
                min_val = float("inf")
                for pre_idx in ch_idxs[pre_ch]:
                    if cur_idx >= pre_idx:
                        min_val = min(min_val, ans[pre_idx] + min(cur_idx - pre_idx, pre_idx + ring_len - cur_idx) + 1)
                    else:
                        min_val = min(min_val, ans[pre_idx] + min(pre_idx - cur_idx, cur_idx + ring_len - pre_idx) + 1)

                ans[cur_idx] = min_val
              
            pre_ch = ch

        return min(ans[idx] for idx in ch_idxs[key[-1]])


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findRotateSteps(ring = "godding", key = "gd")
    assert test1 == 4
    
    test2 = sol.findRotateSteps(ring = "godding", key = "godding")
    assert test2 == 13
    