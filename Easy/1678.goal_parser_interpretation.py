'''
https://leetcode.com/problems/goal-parser-interpretation/description/
'''

class Solution:
    def interpret(self, command: str) -> str:
        return command.replace("()", "o").replace("(al)", "al")
    

if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.interpret(command = "G()(al)")
    assert test1 == "Goal"
    
    test2 = sol.interpret(command = "G()()()()(al)")
    assert test2 == "Gooooal"
    
    test3 = sol.interpret(command = "(al)G(al)()()G")
    assert test3 == "alGalooG"
    