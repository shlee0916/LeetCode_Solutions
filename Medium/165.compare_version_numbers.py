'''
https://leetcode.com/problems/compare-version-numbers/description/
'''

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1_list = version1.split(".")
        ver2_list = version2.split(".")

        if len(ver1_list) < len(ver2_list):
            for _ in range(len(ver2_list) - len(ver1_list)):
                ver1_list.append("0")
        elif len(ver1_list) > len(ver2_list):
            for _ in range(len(ver1_list) - len(ver2_list)):
                ver2_list.append("0")

        for ver1, ver2 in zip(ver1_list, ver2_list):
            if int(ver1) < int(ver2):
                return -1
            elif int(ver1) > int(ver2):
                return 1
            
        return 0
        
        
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.compareVersion(version1 = "1.01", version2 = "1.001")
    assert test1 == 0
    
    test2 = sol.compareVersion(version1 = "1.0", version2 = "1.0.0")
    assert test2 == 0
    
    test3 = sol.compareVersion(version1 = "0.1", version2 = "1.1")
    assert test3 == -1
    