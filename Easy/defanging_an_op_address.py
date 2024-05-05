'''
https://leetcode.com/problems/defanging-an-ip-address/description/
'''

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.defangIPaddr(address = "1.1.1.1")
    assert test1 == "1[.]1[.]1[.]1"
    
    test2 = sol.defangIPaddr(address = "255.100.50.0")
    assert test2 == "255[.]100[.]50[.]0"
    