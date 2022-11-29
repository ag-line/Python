import matplotlib.pyplot as plt
import random

val = [random.randint(0,5) for i in range(600)]
rolls = [0]*6 
for i in val:
  rolls[i] = rolls[i] + 1

print(rolls, sum(rolls))
plt.bar([i for i in range(1,7)],rolls)
plt.show()