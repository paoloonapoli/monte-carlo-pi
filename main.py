import random

# Monte Carlo method to estimate the value of Pi

# The idea is to randomly generate points in a 2x2 square and count
# how many fall inside a circle of radius 1 inscribed within that square.

center = [1, 1]
inside_circle = 0
print("Estimate the value of Pi using the Monte Carlo method.")

for i in range(iterations := int(input("Number of iterations: "))):

    # Generate a random point in the 2x2 square
    coord = [2*random.random(), 2*random.random()]

    # Calculate the distance from the center of the circle using the Pythagorean theorem
    dist = ((coord[0] - center[0]) ** 2 + (coord[1] - center[1]) ** 2) ** 0.5
    
    if dist <= 1:
        inside_circle += 1

print(f"Estimated value of Pi: {4 * inside_circle / iterations}")

