'''
https://leetcode.com/problems/word-search-ii/description/
'''
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        self.refs = 0

    def addWord(self, word):
        cur = self
        cur.refs += 1
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
            cur.refs += 1
        cur.isWord = True

    def removeWord(self, word):
        cur = self
        cur.refs -= 1
        for ch in word:
            if ch in cur.children:
                cur = cur.children[ch]
                cur.refs -= 1


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        ROWS, COLS = len(board), len(board[0])
        res, visit = set(), set()

        def dfs(row_idx, col_idx, node, word):
            if (
                row_idx not in range(ROWS) 
                or col_idx not in range(COLS)
                or board[row_idx][col_idx] not in node.children
                or node.children[board[row_idx][col_idx]].refs < 1
                or (row_idx, col_idx) in visit
            ):
                return

            visit.add((row_idx, col_idx))
            node = node.children[board[row_idx][col_idx]]
            word += board[row_idx][col_idx]
            if node.isWord:
                node.isWord = False
                res.add(word)
                root.removeWord(word)

            dfs(row_idx + 1, col_idx, node, word)
            dfs(row_idx - 1, col_idx, node, word)
            dfs(row_idx, col_idx + 1, node, word)
            dfs(row_idx, col_idx - 1, node, word)
            visit.remove((row_idx, col_idx))

        for row_idx in range(ROWS):
            for col_idx in range(COLS):
                dfs(row_idx, col_idx, root, "")

        return list(res)
    
    
if __name__ == "__main__":
    sol = Solution()
    
    test1 = sol.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],["oath","pea","eat","rain"])
    print(test1, ["oath","eat"])
    assert test1 == ["oath","eat"]
    
    test2 = sol.findWords([["a","b"],["c","d"]],["abcb"])
    print(test2, [])
    assert test2 == []