'''
https://leetcode.com/problems/simplify-path/description/
'''

class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        stack = []
        for dir_name in paths:
            if dir_name and dir_name != ".." and dir_name != ".":
                stack.append(dir_name)
            elif stack and dir_name == "..":
                stack.pop()
            
        return "/" + "/".join(stack)


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.simplifyPath("/home/")
    print(test1, "/home")
    assert test1 == "/home"

    test2 = sol.simplifyPath("/../")
    print(test2, "/")
    assert test2 == "/"

    test3 = sol.simplifyPath("/home//foo/")
    print(test3, "/home/foo")
    assert test3 == "/home/foo"
    