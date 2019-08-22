def rotate_image(image: list):
    size = len(image)
    layer = 0
    while layer <= size // 2:
        i = layer
        while i < size - 2 * layer - 1:
            temp = image[layer][i + layer]
            image[layer][i + layer] = image[layer + i][size - 1 - layer]
            image[layer + i][size - 1 - layer] = image[size - 1 - layer][size - i - layer - 1]
            image[size - 1 - layer][size - i - layer - 1] = image[size - 1 - i - layer][layer]
            image[size - 1 - i - layer][layer] = temp
            i += 1
        layer += 1
    print(image)


if __name__ == '__main__':
    image = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    # [[3, 6, 9],
    # [2, 5, 8],
    # [1, 4, 7]]
    rotate_image(image)


