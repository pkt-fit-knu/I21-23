
import imageio
import numpy as np

if __name__ == '__main__':
    image = imageio.imread("pic1.jpg")
    new_image = np.zeros((len(image), len(image[0]), len(image[0][0])))
    for i in range(1, len(image) - 1):
        print("Processing {} of {}".format(i - 1, len(image) - 2))
        for j in range(1, len(image[0]) - 1):
            for channel in range(len(image[0][0])):
                new_image[i][j][channel] += (
                    image[i + 1][j][channel] -
                    image[i - 1][j][channel] -
                    image[i][j + 1][channel] -
                    image[i][j - 1][channel] +
                    4 * image[i][j][channel]
                )
    imageio.imwrite("pic1_better.png", new_image)
