"""A program that implements resizing image by bilinear algorythm."""

import imageio
import numpy as np


def grange(end, start=0):
    """Generator range for some cind of 'optimisation'."""
    current = start
    while(True):
        if current >= end:
            raise StopIteration()
        yield current
        current += 1

if __name__ == "__main__":
    img = imageio.imread("pic1.jpg")
    new_img = np.zeros((
        len(img) * 2,
        len(img[0]) * 2,
        len(img[0][0])
    ), dtype=np.uint32)
    for y_pos in grange(len(img) - 1):
        for x_pos in grange(len(img[0]) - 1):
            apper_left = img[y_pos][x_pos]
            apper_right = img[y_pos][x_pos + 1]
            bottom_left = img[y_pos + 1][x_pos]
            bottom_right = img[y_pos + 1][x_pos + 1]

            for i in grange(len(img[0][0])):
                # First level of interpolation - linear, first row
                new_img[y_pos * 2 - 1][x_pos * 2 - 1][i] = apper_left[i]
                new_img[y_pos * 2 - 1][x_pos * 2 + 1][i] = apper_right[i]
                new_img[y_pos * 2 - 1][x_pos * 2 + 1][i] = (
                    (apper_left[i] / 2 + apper_right[i] / 2)
                )

                # First level of interpolation - linear, second row
                new_img[y_pos * 2 + 1][x_pos * 2][i] = bottom_left[i]
                new_img[y_pos * 2 + 1][x_pos * 2 + 1][i] = bottom_right[i]
                new_img[y_pos * 2 + 1][x_pos * 2][i] = (
                    (bottom_left[i] / 2 + bottom_right[i] / 2)
                )

                # First level of interpolation - linear, first column
                new_img[y_pos * 2][x_pos * 2 - 1][i] = (
                    (apper_left[i] / 2 + bottom_left[i] / 2)
                )

                # First level of interpolation - linear, second column
                new_img[y_pos * 2 + 1][x_pos * 2][i] = (
                    (apper_right[i] / 2 + bottom_right[i] / 2)
                )

                # Second level of interpolation - linear, middle column

                new_img[y_pos * 2][x_pos * 2][i] = ((
                    new_img[y_pos * 2 - 1][x_pos * 2 - 1][i] / 2 +
                    new_img[y_pos * 2 + 1][x_pos * 2 + 1][i] / 2
                ))
        print("%d/%d" % (y_pos, len(img) - 1))
    imageio.imwrite("pic1_bigger.png", new_img)
