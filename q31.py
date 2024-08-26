from itertools import permutations

numbers = [1, 2, 3, 4]
combinations = permutations(numbers)

for combination in combinations:
    print(combination)
