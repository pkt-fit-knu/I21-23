from classifier import Classifier


def main():
    data = read_from_file(name='iris.data')
    classifier = Classifier(data)
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
