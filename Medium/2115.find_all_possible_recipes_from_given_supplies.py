'''
https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/description/?envType=daily-question&envId=2025-03-21
'''

from collections import deque

from typing import List


class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ans = []

        recipes_map = {}
        for recipes, ingd in zip(recipes, ingredients):
            recipes_map[recipes] = set(ingd)

        que = deque(supplies)
        while que:
            food = que.popleft()

            for recipe, ingd in recipes_map.items():
                if food in ingd:
                    ingd.remove(food)

                if len(ingd) == 0 and recipe not in ans:
                    ans.append(recipe)
                    que.append(recipe)

        return ans


if __name__ == "__main__":
    sol = Solution()

    test1 = sol.findAllRecipes(recipes = ["bread"], ingredients = [["yeast", "flour"]], supplies = ["yeast", "flour", "corn"])
    assert test1 == ["bread"]

    test2 = sol.findAllRecipes(recipes = ["bread", "sandwich"], ingredients = [["yeast", "flour"], ["bread", "meat"]], supplies = ["yeast", "flour", "meat"])
    assert test2 == ["bread", "sandwich"]

    test3 = sol.findAllRecipes(recipes = ["bread", "sandwich", "burger"], ingredients = [["yeast", "flour"], ["bread", "meat"], ["sandwich", "meat", "bread"]], supplies = ["yeast", "flour", "meat"])
    assert test3 == ["bread", "sandwich", "burger"]
