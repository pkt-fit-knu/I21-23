from classifier import Classifier
import math


class OneRuleClassifier(Classifier):

    """Classifier that is based on one rule algorithm """

    __predictors__ = [
        lambda item: math.trunc(1 * item['vals'][0] / item['vals'][1]),
        lambda item: math.trunc(1 * item['vals'][1] / item['vals'][2]),
        lambda item: math.trunc(1 * item['vals'][2] / item['vals'][3]),
        lambda item: math.trunc(1 * item['vals'][0] / item['vals'][2])
    ]

    __RULE__ = {}

    def __init__(self, training_data):
        self.train(training_data)

    def train(self, data):
        """ Finds the most appropriate selector predictor """
        rules = self.build_rules(data)
        wrong = []
        i = 0

        # Count how much wrong count for every rule
        for rule in rules:
            wrong.append(0)
            for item in data:
                correct = item['class']
                for key, value in rule['data'].iteritems():
                    # I don't like the construct below.
                    # But at least it's readable...
                    if (
                            value == rule['predictor'](item) and
                            key == correct):
                        wrong[i] += 1
            i += 1

        if len(wrong) < 1:
            print("What the heck? No wrong items detected")
            return

        # Find the least wrong point
        least_wrong = 0
        for i in range(len(wrong)):
            if wrong[i] < wrong[least_wrong]:
                least_wrong = i

        self.__RULE__ = rules[least_wrong]

    def build_rules(self, data):
        """ Builds rules table """
        def apply_predic(predictor, data):
            """ Creates dataset based on @data processed by @predictor """
            result = []
            for item in data:
                result.append({
                    'value': predictor(item),
                    'class': item['class']
                })
            return result

        rules = []

        for predictor in self.__predictors__:
            # Generate predicted list
            predic_list = apply_predic(predictor, data)

            # Build rule
            rule = {
                'predictor': predictor,
                'data': {}
            }

            # Cache for saving current conting
            cache = {}

            # Count how much any entry is in predicate
            for item in predic_list:
                cur_class = item['class']
                cur_val = item['value']
                if cur_class not in cache:
                    cache[cur_class] = {}
                if cur_class not in cache[cur_class]:
                    cache[cur_class][cur_val] = 0
                cache[cur_class][cur_val] += 1

            # Create rule from current cache
            for _class, values in cache.iteritems():

                # If there is no values there is no sense to add it
                if len(values) < 0:
                    continue

                # Select maximal value in rule
                for val, count in values.iteritems():
                    if _class not in rule['data']:
                        rule['data'][_class] = count
                    elif rule['data'][_class] < count:
                        rule['data'][_class] = count

            # Add it to rules collection
            rules.append(rule)
        return rules

    def classify(self, data):
        wrong = 0
        for item in data:
            correct = item['class']
            for key, value in self.__RULE__['data'].iteritems():
                # I don't like the construct below.
                # But at least it's readable...
                if (
                        value == self.__RULE__['predictor'](item) and
                        key == correct):
                    print("%s expected, but found %s" % (
                        correct, key
                        ))
                    wrong += 1
        print("%i/%i is wrong" % (wrong, len(data)))
