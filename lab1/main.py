"""A program that implements classifying data by primitive algorythms."""

from classifier import Classifier
from onerule import OneRuleClassifier

# The constant that defines the count of
# data to be passed while training classifier
MAX_SELECTOR = 2


def main():
    """Main program method."""
    data = read_from_file(name='iris.data')

    training_data = []
    selector = 0
    for item in data:
        if selector >= MAX_SELECTOR:
            training_data.append(item)
            selector = 0
        else:
            selector += 1
    print("Plain classifier: ")
    classifier = Classifier(training_data)
    classifier.classify(data)
    print
    print("1R classifier: ")
    classifier = OneRuleClassifier(training_data)
    classifier.classify(data)


def read_from_file(name=""):
    """Read a csv file."""
    data = []
    import csv
    with open(name, "r") as data_file:
        datareader = csv.reader(data_file, delimiter=',', quotechar=' ')
        for row in datareader:
            point = {"vals": []}
            for value in row:
                try:
                    point["vals"].append(float(value))
                except ValueError:
                    point["class"] = value
            if len(point["vals"]) == 4 and "class" in point:
                data.append(point)
    return data

if __name__ == "__main__":
    main()
