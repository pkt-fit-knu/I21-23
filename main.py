# from classifier import Classifier


def main():
    print("Hello world!!!")
    # sifier = Classifier()
    read_from_file(name='iris.data')
    return 0


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
            data.append(point)
    print(data)
    print(len(data))
    # TODO: write file
    data_file.close()
    return data

if __name__ == "__main__":
    main()
