'''
https://leetcode.com/problems/design-a-food-rating-system/
'''

from collections import defaultdict
from heapq import heappush, heappop

from typing import List


class Food:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating


    def __lt__(self, other):
        if self.rating == other.rating:
            return self.name < other.name
        
        return self.rating > other.rating


    def __str__(self):
        return f"Food: {self.name}, Rating: {self.rating}"


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisine_food_rating = defaultdict(list)
        self.food_ratings = defaultdict(int)
        self.food_cuisine = {}

        for food_name, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_ratings[food_name] = rating
            self.food_cuisine[food_name] = cuisine
            heappush(self.cuisine_food_rating[cuisine], Food(food_name, rating))


    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine[food]

        self.food_ratings[food] = newRating
        heappush(self.cuisine_food_rating[cuisine], Food(food, newRating))
        

    def highestRated(self, cuisine: str) -> str:
        highest = self.cuisine_food_rating[cuisine][0]

        while highest.rating != self.food_ratings[highest.name]:
            heappop(self.cuisine_food_rating[cuisine])
            highest = self.cuisine_food_rating[cuisine][0]

        return highest.name
            

if __name__ == "__main__":
    fr = FoodRatings(foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], 
                     cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"], 
                     ratings = [9, 12, 8, 15, 14, 7])
    
    assert fr.highestRated("korean") == "kimchi"
    assert fr.highestRated("japanese") == "ramen"
    fr.changeRating("sushi", 16)
    assert fr.highestRated("japanese") == "sushi"
    fr.changeRating("ramen", 16)
    assert fr.highestRated("japanese") == "ramen"

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)