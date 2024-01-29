'''
https://leetcode.com/problems/text-justification/?envType=study-plan-v2&envId=top-interview-150
'''

from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = []
        cur_line = []
        cur_len = 0

        for word in words:
            if cur_len + len(cur_line) + len(word) > maxWidth:
                for idx in range(maxWidth - cur_len):
                    cur_line[idx % (len(cur_line) - 1 or 1)] += " "

                lines.append("".join(cur_line))
                cur_line = []
                cur_len = 0

            cur_line.append(word)
            cur_len += len(word)

        return lines + [" ".join(cur_line).ljust(maxWidth)]
 

if __name__ == "__main__":
    sol = Solution()

    test1 = sol.fullJustify(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16)
    assert test1 == [
                    "This    is    an",
                    "example  of text",
                    "justification.  "
                    ]

    test2 = sol.fullJustify(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16)
    assert test2 == [
                    "What   must   be",
                    "acknowledgment  ",
                    "shall be        "
                    ]
    
    test3 = sol.fullJustify(words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"],  maxWidth = 20)
    assert test3 == [
                    "Science  is  what we",
                    "understand      well",
                    "enough to explain to",
                    "a  computer.  Art is",
                    "everything  else  we",
                    "do                  "
                    ]
