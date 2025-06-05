'''
https://leetcode.com/problems/lexicographically-smallest-equivalent-string/?envType=daily-question&envId=2025-06-05
'''

from collections import defaultdict


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        min_ch = {}
        ch_map = defaultdict(set)
        for s1_ch, s2_ch in zip(s1, s2):
            ch_map[s1_ch].add(s2_ch)
            ch_map[s2_ch].add(s1_ch)

        for node in ch_map:
            visit = set([node])
            possible = [node]
            stack = [node]
            while stack:
                cur_node = stack.pop()

                for next_node in ch_map[cur_node]:
                    if next_node not in visit:
                        stack.append(next_node)
                        possible.append(next_node)
                        visit.add(next_node)

            smallest = min(possible)
            for node in possible:
                min_ch[node] = smallest
        
        ans = ""
        for ch in baseStr:
            ans += min_ch[ch] if ch in min_ch else ch
        
        return ans
    

# Explanation
# 그래프와 DFS 를 이용해 해결할 수 있다.
# 우선 문제의 설명에 따라 s1, s2를 사용해 ch_map을 이용해 그래프를 그린다.
# 각각의 알파벳을 node로 생각해 edge를 연결한다.
# 연결한 그래프의 node를 기준으로 그래프를 순회한다.
# 그래프를 순회하면서 방문했던 모든 node를 기록하고 해당 node중 가장 사전순으로 빠른 것을 min_ch dictionary를 통해 node에 따라 기록한다.
# 기록한 min_ch를 사용해 ans를 작성한다.
# Union-Find 알고리즘을 사용하면 더 빠른 실행시간을 가질 수 있을 것 같다.

# Union-Find
# class Solution:
#     def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
#         min_ch = {}
        
#         def find(node):
#             if node not in min_ch:
#                 return node

#             if node != min_ch[node]:
#                 min_ch[node] = find(min_ch[node])

#             return min_ch[node]

#         def union(node1, node2):
#             find_node1 = find(node1)
#             find_node2 = find(node2)

#             if find_node1 > find_node2:
#                 min_ch[find_node1] = find_node2
#             else:
#                 min_ch[find_node2] = find_node1

#         for node1, node2 in zip(s1, s2):
#             union(node1, node2)
        
#         ans = ""
#         for ch in baseStr:
#             ans += find(ch)
        
#         return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser")
    assert test1 == "makkek"

    test2 = sol.smallestEquivalentString(s1 = "hello", s2 = "world", baseStr = "hold")
    assert test2 == "hdld"

    test3 = sol.smallestEquivalentString(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode")
    assert test3 == "aauaaaaada"
