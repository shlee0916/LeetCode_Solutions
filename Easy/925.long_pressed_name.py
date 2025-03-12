'''
https://leetcode.com/problems/long-pressed-name/description/
'''

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_pointer = 0
        
        for idx, type_ch in enumerate(typed):
            if name_pointer < len(name) and type_ch == name[name_pointer]:
                name_pointer += 1
            elif idx == 0 or type_ch != typed[idx - 1]:
                return False
            
        return name_pointer == len(name)


if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.isLongPressedName(name = "alex", typed = "aaleex")
    assert test1 == True
    
    test2 = sol.isLongPressedName(name = "saeed", typed = "ssaaedd")
    assert test2 == False
    