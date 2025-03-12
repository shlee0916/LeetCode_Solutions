'''
https://leetcode.com/problems/top-k-frequent-words/
'''
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hash_map = {}
        
        for word in words:
            if word in hash_map.keys():
                hash_map[word] += 1
            else:
                hash_map[word] = 1
                
        sorted_list = sorted(hash_map.items(), key = lambda item: (-item[1], item[0]))
        
        return [item[0] for item in sorted_list[:k]]


if __name__ == "__main__":
    sol = Solution()

    print(sol.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2), ["i","love"])
    print(sol.topKFrequent(["the","day","is","sunny","the","the","the","sunny","is","is"], 4), ["the","is","sunny","day"])