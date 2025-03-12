'''
https://leetcode.com/problems/word-ladder/?envType=problem-list-v2&envId=breadth-first-search

Problem num: 127
'''

from collections import defaultdict, deque

from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        cnt = 1
        word_len = len(beginWord)
        que = deque([beginWord])
        seen = set([beginWord])
        word_map = defaultdict(list)
        
        for word in wordList:
            for idx in range(word_len):
                word_map[word[:idx] + "_" + word[idx + 1:]].append(word)

        while que:
            for _ in range(len(que)):
                cur_word = que.popleft()
                if cur_word == endWord:
                    return cnt

                for idx in range(word_len):
                    next_word = cur_word[:idx] + "_" + cur_word[idx + 1:]
                    if next_word not in seen and next_word in word_map:
                        seen.add(next_word)
                        que.extend(word_map[next_word])
                
            cnt += 1
        
        return 0


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log", "cog"])
    assert test1 == 5

    test2 = sol.ladderLength(beginWord = "hit", endWord = "cog", wordList = ["hot", "dot", "dog", "lot", "log"])
    assert test2 == 0
    