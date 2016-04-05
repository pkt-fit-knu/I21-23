from math import log


def build_classifier(data):
    """Build divide & conquer classifier."""
    def info_cmp(f, s):
        return cmp(f["info"], s["info"])
    training_nodes = list(map(
        lambda n: {
            "node": n,
            "info": n.info()
        }, [TrainingNode(data, i) for i in range(len(data[0]) - 1)]
    ))
    best_node = sorted(training_nodes, info_cmp)[0]['node']
    best_node.build_tree()
    return best_node


class TrainingNode(object):

    def __init__(self, data, column):
        """Build training node from data

        Builds training node from data assuming that last column of data is
        resulting value

        Arguments:
            column {int} -- column for node to build rule by
            data {list} -- training data for training tree build
        """
        self.data = data
        self.column = column
        self.rules = [{node[column]: node[-1]} for node in data]

    def __repr__(self):
        return str(self.rule)

    def info(self):
        """Calculate info stored in node."""
        count = {}
        for rule in self.rules:
            if rule.keys()[0] not in count:
                count[rule.keys()[0]] = 0
            count[rule.keys()[0]] += 1
        gen = 0
        for _, value in count.iteritems():
            gen += value
        res = 0
        for _, value in count.iteritems():
            res -= (float(value) / gen) * log(float(value) / gen)
        return res

    def split_data(self):
        """Split data based on rule

        Split data based on rule with deleting this training node field.
        """
        result = [
            (key, [
                [
                    row[i] for i in range(len(row)) if i != self.column
                ] for row in self.data if row[self.column] == key
            ]) for key in map(lambda x: x[self.column], self.data)
        ]
        return result

    def build_tree(self):
        """Build tree below node."""
        rules = {}
        for (key, data) in self.split_data():

            def unpack_value(x):
                try:
                    return x[key]
                except KeyError:
                    return None
            # Check whether there is only one value
            cached = None
            for value in map(unpack_value, self.rules):
                if value is None:
                    continue
                if cached is None:
                    cached = value
                if cached != value:
                    cached = None
                    break
            # If it is, save to rules
            if cached is not None:
                rules[key] = cached
                continue
            # Otherwise, build tree further
            rules[key] = build_classifier(data)
        self.rule = rules

    def classify(self, data):
        try:
            value = self.rule[data[self.column]]
            if isinstance(value, TrainingNode):
                ddata = [data[i] for i in range(len(data)) if i != self.column]
                return value.classify(ddata)
            else:
                return value
        except KeyError:
            print("Could not recognize data. Terminating classification")
            return None
