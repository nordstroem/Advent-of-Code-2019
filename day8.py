import numpy as np
from aocutil import read_file
import matplotlib.pyplot as plt

data = [int(c) for c in read_file("input8.txt").strip()]

img = np.array(data).reshape(-1, 6, 25)
layer = np.argmin(np.count_nonzero(img == 0, axis=(1, 2)))
print(np.count_nonzero(img[layer,:] == 1) * np.count_nonzero(img[layer,:] == 2))

final_image = np.full((6, 25), -1)
for sub_image in img:
    indicies_to_update = np.logical_and(sub_image != 2, final_image == -1)
    final_image[indicies_to_update] = sub_image[indicies_to_update]

plt.imshow(final_image, cmap='gray')
plt.show()