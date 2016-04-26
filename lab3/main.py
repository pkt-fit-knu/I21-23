"""Histogram normalisation algorythm"""

import imageio
import numpy as np
import math


def grange(end, start=0):
    """Generator range for some cind of 'optimisation'."""
    current = start
    while(True):
        if current >= end:
            raise StopIteration()
        yield current
        current += 1


def make_hist(image):
    value_type_info = np.iinfo(image[0][0][0])
    hists = np.zeros((
        len(image[0][0]),
        math.trunc(value_type_info.max) + 1
    ))

    # Build histogram
    for line in image:
        for point in line:
            for i in range(1):
                hists[i][point[i]] += 1
    return [
        zip(
            range(math.trunc(value_type_info.max) + 1),
            hist
        ) for hist in hists
    ]


def build_normalisation_table(image, channel_hist):
    def cum(val, cache=[0]):
        if not cache:
            cache = [0]
        cache[0] += val[1]
        return [val[0], cache[0]]

    value_type_info = np.iinfo(image[0][0][0])
    cum_hist = dict(map(cum, channel_hist))
    res_assignment = dict([
        (key, round(
            (math.trunc(value_type_info.max) - 1) *
            (cum_hist[key] - cum_hist.keys()[0]) /
            ((len(image) * len(image[0])) - cum_hist.keys()[0])
        ))
        for key in dict(channel_hist).keys()
    ])
    return res_assignment

if __name__ == '__main__':
    image = imageio.imread("pic1.jpg")
    channel = 0
    value_type_info = np.iinfo(image[0][0][0])
    hists = np.zeros((len(image), len(image[0]), 1), dtype=value_type_info)
    print("Grayscaling image...")
    for i in range(len(image)):
        for j in range(len(image[i])):
            hists[i][j] = (
                image[i][j][0] / 3 + image[i][j][1] / 3 + image[i][j][2] / 3)
    print("Done")
    image = hists
    print("Normalizing image...")
    for hist in make_hist(image):
        table = build_normalisation_table(image, hist)
        print("Processing channel {}".format(channel))
        for i in range(len(image)):
            for j in range(len(image[i])):
                # print("{} => {}".format(image[i][j][channel], table[image[i][j][channel]]))
                image[i][j][channel] = math.trunc(table[image[i][j][channel]])
        channel += 1
    print("Done")

    imageio.imwrite("pic1_norm.png", image)
