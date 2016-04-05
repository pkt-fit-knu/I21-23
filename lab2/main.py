"""A program that implements classifying data by primitive algorithms."""

from classifier import build_classifier
import json

# The constant that defines the count of
# data to be passed while training classifier
MAX_SELECTOR = 2


def read_from_file(name=""):
    """Read a csv file."""
    data = []
    import csv
    with open(name, "r") as data_file:
        datareader = csv.reader(data_file, delimiter=',', quotechar=' ')
        for row in datareader:
            data.append(row)
    return data

if __name__ == "__main__":
    data = read_from_file(name='data')
    classifier = build_classifier(data)
    print("Tree is: {}".format(classifier))
    count = len(data)
    error = 0
    for item in data:
        value = classifier.classify(item)
        print("Recognized {}, expected {}".format(value, item[-1]))
        if value != item[-1]:
            error += 1
    print("Recognition finished. Got {} of total {} incorrect".format(
        error, count))
