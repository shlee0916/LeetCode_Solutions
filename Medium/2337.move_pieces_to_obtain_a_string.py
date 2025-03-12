'''
https://leetcode.com/problems/move-pieces-to-obtain-a-string/?envType=daily-question&envId=2024-12-05
'''

class Solution:
    def canChange(self, start: str, target: str) -> bool:
        if start.replace("_", "") != target.replace("_", ""):
            return False

        start_idx = 0
        target_idx = 0
        length = len(start)

        while start_idx < length and target_idx < length:
            while start_idx < length and start[start_idx] == "_":
                start_idx += 1
            while target_idx < length and target[target_idx] == "_":
                target_idx += 1

            if target_idx < length and start_idx < length:
                
                if start[start_idx] == "R" and start_idx > target_idx:
                    return False

                elif start[start_idx] == "L" and start_idx < target_idx:
                    return False

            start_idx += 1
            target_idx += 1
        
        return True


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.canChange(start = "_L__R__R_", target = "L______RR")
    assert test1 == True

    test2 = sol.canChange(start = "R_L_", target = "__LR")
    assert test2 == False

    test3 = sol.canChange(start = "_R", target = "R_")
    assert test3 == False
    