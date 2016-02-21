class Classifier():

    """ Class that implements dummy classifier. """

    __rules__ = []

    def __init__(self, training_data):
        self.train(training_data)

    def train(self, data):
        # Init analizing variables
        current_class = data[0]["class"]
        current_class_count = 0
        current_class_max_diff = [0.0, 0.0, 0.0, 0.0]
        current_class_values = [0.0, 0.0, 0.0, 0.0]

        for item in data:
            if current_class == item['class']:

                # Find new max_difference and append new values
                for i in range(len(item['vals'])):
                    if current_class_count != 0:
                        current_class_max_diff[i] = (
                            current_class_max_diff[i]
                            if current_class_max_diff[i] > abs(
                                (current_class_values[i] /
                                    current_class_count) - item['vals'][i]
                            ) else abs(
                                (current_class_values[i] /
                                    current_class_count) - item['vals'][i]
                            )
                        )
                    current_class_values[i] += item['vals'][i]
                current_class_count += 1
            else:
                # If we've got out of current selection, save point and go on
                for i in range(len(current_class_values)):
                    current_class_values[i] /= current_class_count

                self.__rules__.append({
                    'class':  current_class,
                    'values': current_class_values,
                    'diff':   current_class_max_diff,
                })
                current_class = item['class']
                current_class_count = 1
                current_class_values = item['vals']
                current_class_max_diff = [0.0, 0.0, 0.0, 0.0]

        for i in range(len(current_class_values)):
            current_class_values[i] /= current_class_count

        self.__rules__.append({
            'class':  current_class,
            'values': current_class_values,
            'diff':   current_class_max_diff,
        })

        for rule in self.__rules__:
            print(" Class is `%s`" % rule['class'])
            for i in range(len(rule['values'])):
                print("\trule: %.2f +- %.2f" % (
                        rule['values'][i],
                        rule['diff'][i]
                    ))

    def classify(self, data):
        wrong_count = 0

        __UNKNOWN__ = "Unknown"

        def apply_rule(rule, item):
            rule_fits = True
            for i in range(len(item['vals'])):
                print(rule_fits)
                print("%.2f <= %.2f and %.2f >= %.2f" % (
                    item['vals'][i], rule['values'][i] + rule['diff'][i],
                    item['vals'][i], rule['values'][i] - rule['diff'][i]
                ))
                rule_fits = rule_fits and (
                    item['vals'][i] <= rule['values'][i] + rule['diff'][i] and
                    item['vals'][i] >= rule['values'][i] - rule['diff'][i]
                )
            return rule['class'] if rule_fits else __UNKNOWN__

        for item in data:
            selected = ""
            for rule in self.__rules__:
                selected = apply_rule(rule, item)
                if selected != __UNKNOWN__:
                    break
            print("[%.1f %.1f %.1f %.1f] classified as %s, expected %s" % (
                item['vals'][0], item['vals'][1],
                item['vals'][2], item['vals'][3],
                selected, item['class']))
            if selected != item['class']:
                wrong_count += 1
        print("Recognized wrong %i of %i" % (
            wrong_count,
            len(data)
            ))
