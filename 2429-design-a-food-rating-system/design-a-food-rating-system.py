import heapq

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        # Maps for quick access
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_heap = {}

        for f, c, r in zip(foods, cuisines, ratings):
            self.food_to_cuisine[f] = c
            self.food_to_rating[f] = r
            if c not in self.cuisine_to_heap:
                self.cuisine_to_heap[c] = []
            heapq.heappush(self.cuisine_to_heap[c], (-r, f))  # max-heap: (-rating, food)

    def changeRating(self, food: str, newRating: int) -> None:
        # Update food rating
        self.food_to_rating[food] = newRating
        cuisine = self.food_to_cuisine[food]
        # Push new rating into heap
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_heap[cuisine]
        # Lazy removal of outdated ratings
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)
