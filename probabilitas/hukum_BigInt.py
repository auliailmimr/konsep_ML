import numpy as np

sample_sizes = [10, 100, 1000, 10000]
means = []

for size in sample_sizes:
    sample = np.random.normal(loc=0, scale=1, size=size)
    means.append(np.mean(sample))


print(f"Rata-rata sample: {means}")