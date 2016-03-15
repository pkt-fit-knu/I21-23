"""A program that implements resizing image by bilinear algorythm."""

# import imageio
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math


def main():
    """Main program method."""
    img = mpimg.imread('pic1.jpg')

    # Init storage for data count
    value_type_info = np.iinfo(img[0][0][0])
    hists = np.zeros((len(img[0][0]), math.trunc(value_type_info.max) + 1))

    # Build histogram
    for line in img:
        for point in line:
            for i in xrange(3):
                hists[i][point[i]] += 1

    # Display histogram
    imgplot = plt.plot(
        range(math.trunc(value_type_info.max) + 1), hists[0],
        range(math.trunc(value_type_info.max) + 1), hists[1],
        range(math.trunc(value_type_info.max) + 1), hists[2],
    )
    plt.show(imgplot)

if __name__ == "__main__":
    main()
