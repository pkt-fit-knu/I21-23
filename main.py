from classifier import Classifier


def main():
    sifier = Classifier()
    data = read_from_file(name='iris.data')
    # display_correlation(data)
    classifier = Classifier()
    classifier.classify(data)
    return 0


def display_correlation(data):
    current_class = data[0]["class"]
    current_class_count = 0
    current_class_max_diff = [0.0, 0.0, 0.0, 0.0]
    current_class_values = [0.0, 0.0, 0.0, 0.0]
    for item in data:
        if current_class == item['class']:
            for i in range(len(item['vals'])):
                if current_class_count != 0:
                    current_class_max_diff[i] = (
                        current_class_max_diff[i]
                        if current_class_max_diff[i] > abs(
                            (current_class_values[i] / current_class_count) -
                            item['vals'][i]
                        ) else abs(
                            (current_class_values[i] / current_class_count) -
                            item['vals'][i]
                        )
                    )
                current_class_values[i] += item['vals'][i]
            current_class_count += 1
        else:
            print(" Class is %s, middle values are:" % current_class)
            for i in range(len(current_class_values)):
                print("\t%.1f +- %.1f" % (
                    current_class_values[i]/current_class_count,
                    current_class_max_diff[i]))
            current_class = item['class']
            current_class_count = 1
            current_class_values = item['vals']
            current_class_max_diff = [0.0, 0.0, 0.0, 0.0]
    print(" Class is %s, middle values are:" % current_class)
    for i in range(len(current_class_values)):
        print("\t%.1f +- %.1f" % (
            current_class_values[i]/current_class_count,
            current_class_max_diff[i]))
    current_class = item['class']
    current_class_count = 1
    current_class_values = item['vals']
    current_class_max_diff = [0.0, 0.0, 0.0, 0.0]


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
