import numpy as np 
n = 6
bubbles = np.random.choice(10, n, replace=False)
print(list(bubbles))

# n = 6
# r1:idx5, r2:idx4, r3:idx3, r4:idx2 ==> r + idx = 6, idx = 6 - r
for round, _ in enumerate(bubbles):
    for index, _ in enumerate(bubbles[1:]):
        print(f"Round:{round},index i = {index}, i:{bubbles[index - 1]}, j:{bubbles[index]}")
        if bubbles[index - 1] > bubbles[index]:
            temp = bubbles[index - 1]
            bubbles[index - 1] = bubbles[index]
            bubbles[index] = temp
        print(f"Bubbles after: {bubbles}")

# print(sorted(bubbles))