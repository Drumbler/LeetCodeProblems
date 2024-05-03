def distribute_candies(candy_type) -> int:
    unique_candies = len(set(candy_type))
    candies_allowed_to_eat = len(candy_type) // 2
    return min(candies_allowed_to_eat, unique_candies)


print(distribute_candies([1, 1, 2, 2, 3, 3]))
