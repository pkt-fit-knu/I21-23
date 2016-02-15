class Classifier():

    """
    Class that implements dummy classifier.
    Yes, I love magic constants
    """

    def __init__(self):
        super(Classifier, self).__init__()

    def classify(self, data):
        wrong_count = 0
        for item in data:
            selected = ""
            if (
                    (item['vals'][0] > 4.0 and item['vals'][0] < 6.0) and
                    (item['vals'][1] > 2.2 and item['vals'][1] < 4.5) and
                    (item['vals'][2] > 1.0 and item['vals'][2] < 2.0) and
                    (item['vals'][3] > 0 and item['vals'][3] < 0.6)):
                selected = "Iris-setosa"
            elif (
                    (item['vals'][0] > 4.5 and item['vals'][0] < 7.3) and
                    (item['vals'][1] > 2.1 and item['vals'][1] < 3.7) and
                    (item['vals'][2] > 3.0 and item['vals'][2] < 5.6) and
                    (item['vals'][3] > 0.8 and item['vals'][3] < 1.8)):
                selected = "Iris-versicolor"
            elif (
                    (item['vals'][0] > 4.9 and item['vals'][0] < 8.3) and
                    (item['vals'][1] > 2.1 and item['vals'][1] < 3.9) and
                    (item['vals'][2] > 4.3 and item['vals'][2] < 6.9) and
                    (item['vals'][3] > 1.4 and item['vals'][3] < 2.6)):
                selected = "Iris-virginica"
            print("[%.1f %.1f %.1f %.1f] classified as %s, expected %s" % (
                item['vals'][0], item['vals'][1],
                item['vals'][2], item['vals'][3],
                selected, item['class']))
            if selected != item['class']:
                wrong_count += 1
        print("Wrong recognized count is %i" % wrong_count)
