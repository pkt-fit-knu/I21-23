from classifier import Classifier
from onerule import OneRuleClassifier


def main():
    data = read_from_file(name='iris.data')

    training_data = []
    selector = 0
    max_selector = 2
    for item in data:
        if selector >= max_selector:
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

    """ Reads a csv file """

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
