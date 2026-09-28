import numpy as np


path = 'data/ekg/'
score = 0


for i in range(1,5):
    if path >= 2:
        score = score + 1
print(score)