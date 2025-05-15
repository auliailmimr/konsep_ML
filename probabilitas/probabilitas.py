#mengukur rasio keuntungan berdasar jumlah total

import numpy as np

np.random.seed(0)
throws = np.random.randint(1, 7, size=10000)
even_count=np.sum(throws%2==0)
probability_even = even_count/len(throws)
print(f"Simulated probability of rolling an even number: {probability_even}")