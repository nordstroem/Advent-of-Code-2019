import numpy as np
from aocutil import read_file
import matplotlib.pyplot as plt

data = [int(c) for c in read_file("input8.txt").strip()]

img = np.array(data).reshape(-1, 6, 25)
layer = min([(np.count_nonzero(img[i,:] == 0), i) for i in range(img.shape[0])])[1]
print(np.count_nonzero(img[layer,:] == 1) * np.count_nonzero(img[layer,:] == 2))

final_image = np.full((6, 25), -1)
for i in range(img.shape[0]):
    indicies_to_update = np.logical_and(img[i,:] != 2, final_image == -1)
    final_image[indicies_to_update] = img[i, indicies_to_update]

plt.imshow(final_image)
plt.show()