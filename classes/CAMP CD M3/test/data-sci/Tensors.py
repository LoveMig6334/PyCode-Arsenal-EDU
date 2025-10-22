import numpy as np

tensors = np.array(
    [
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 3, 14, 15]],
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 3, 14, 15]],
        [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 3, 14, 15]],
    ]
)

print(tensors)
tensors = tensors.reshape(9, 5)

print(tensors)
