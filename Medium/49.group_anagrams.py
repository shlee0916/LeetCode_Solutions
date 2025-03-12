'''
https://leetcode.com/problems/group-anagrams/
'''
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        unique = {}
        for each_str in strs:
            key = "".join(sorted((each_str)))
            
            if key in unique.keys():
                unique[key].append(each_str)
            else:
                unique[key] = [each_str]
                
                
        return unique.values()
    
    
if __name__ == "__main__":
    sol = Solution()
    
    str_list = ["eat", "tea", "tan", "ate", "nat", "bat"]
    
    print(sol.groupAnagrams(str_list), [["bat"],["nat","tan"],["ate","eat","tea"]])