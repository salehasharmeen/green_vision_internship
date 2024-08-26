import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

x1, y1 = map(float, input("Enter coordinates of the first point (x1 y1): ").split())
x2, y2 = map(float, input("Enter coordinates of the second point (x2 y2): ").split())
distance = euclidean_distance(x1, y1, x2, y2)
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")
