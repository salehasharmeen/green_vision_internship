import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def nearest_neighbor(neighbors, point):
    nearest = None
    min_distance = float('inf')
    
    for neighbor in neighbors:
        distance = euclidean_distance(neighbor, point)
        if distance < min_distance:
            min_distance = distance
            nearest = neighbor
    
    return nearest

neighbors = [tuple(map(int, input("Enter a neighbor coordinate (x y): ").split())) for _ in range(int(input("Enter the number of neighbors: ")))]
point = tuple(map(int, input("Enter the point coordinate (x y): ").split()))

nearest = nearest_neighbor(neighbors, point)
print("The nearest neighbor is:", nearest)
