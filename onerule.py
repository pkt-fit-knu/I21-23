from classifier import Classifier


class OneRuleClassifier(Classifier):

    """Classifier that is based on one rule algorithm """

    def __init__(self, training_data):
        super(OneRuleClassifier, self).__init__(training_data)
        self.train(training_data)

    def train(self, data=[]):
        pass

    def classify(self, data):
        pass
