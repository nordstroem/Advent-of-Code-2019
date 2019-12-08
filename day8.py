import numpy as np
from aocutil import read_file

data = [int(c) for c in read_file("input8.txt").strip()]
img = np.array(data).reshape(-1, 6, 25)
layer = min([(np.count_nonzero(img[i,:] == 0), i) for i in range(img.shape[0])])[1]
print(np.count_nonzero(img[layer,:] == 1) * np.count_nonzero(img[layer,:] == 2))
