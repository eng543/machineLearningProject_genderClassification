from node import *
from ID3 import *
from operator import xor

# Crying
# Note, these functions are provided for your reference.  You will not be graded on their behavior,
# so you can implement them as you choose or not implement them at all if you want to use a different
# architecture for pruning.

def reduced_error_pruning(root, tree, validation_set, full_accuracy = -1):
    if full_accuracy == -1:
        full_accuracy = validation_accuracy(tree, validation_set)
        #print full_accuracy, "full accuracy"

    current_children = root.children

    if current_children == None:
        pass

    else:
        root.children = None
        prune_accuracy = validation_accuracy(tree, validation_set)

        if prune_accuracy > full_accuracy:
            #print prune_accuracy, "prune accuracy"
            reduced_error_pruning(root, tree, validation_set, -1)

        else:
            nominal = root.is_nominal
            root.children = current_children

            if nominal == True:
                for key in current_children.keys():
                    cur_node = current_children[key]
                    reduced_error_pruning(cur_node, tree, validation_set, full_accuracy)

            else:
                for i in range(len(current_children)):
                    cur_node = current_children[i]
                    reduced_error_pruning(cur_node, tree, validation_set, full_accuracy)


def validation_accuracy(tree, validation_set):
    '''
    takes a tree and a validation set and returns the accuracy of the set on the given tree
    '''
    accuracy_summary = []

    for i in range(len(validation_set)):
        output = tree.classify(validation_set[i])
        if output == validation_set[i][0]:
            accuracy_summary.append(1)
        else:
            accuracy_summary.append(0)

    accuracy = sum(accuracy_summary) /float(len(validation_set))
    return accuracy

"""
n0 = Node()
n1 = Node()


n = Node()
n.label = 1
n.decision_attribute = 1
n.is_nominal = False
n.splitting_value = 0.5
n.name = "Numerical attribute"


n0.label = 0
n1.label = 1
#n.children = {1: n0, 2: n1}
n.children = [n0, n1]
n2 = Node()
n2.label = 0
n2.decision_attribute = 4
n3 = Node()
n3.label = 1
n3.decision_attribute = 5
n0.children = [n2, n3]
n0.decision_attribute = 2
n0.is_nominal = False
n0.splitting_value = 1.5
n0.name = "Second Numerical attribute"
n4 = Node()
n4.label = 0
n4.decision_attribute = 6
n5 = Node()
n5.label = 1
n5.decision_attribute = 7
n1.children = [n4, n5]
n1.decision_attribute = 3
n1.is_nominal = False
n1.splitting_value = 3.5

#validation_set = parse.parse("../data/test_bvalidate.csv", True)[0]

validation_set = [[1, 1, 9, 5, 3, 7, 3, 9]]

reduced_error_pruning(n, validation_set)
"""

# Testing for pruning
"""
train = '../data/test_btrain.csv'
train_set, attribute_metadata = parse(train, False)
validate = '../data/test_bvalidate.csv'
validate_set, _ = parse(validate, False)
numerical_splits_count = [10]*len(attribute_metadata)
depth = 10
full_accuracy = -1
train_set = train_set[0:100]
tree = ID3(train_set, attribute_metadata, numerical_splits_count, depth)
root = tree
cursor = open('../output/DNFpreprune.txt','w+')
cursor.write(tree.print_dnf_tree())
cursor.close()
reduced_error_pruning(root, tree, tree, train_set, full_accuracy)
cursor = open('../output/DNFpostprune.txt','w+')
cursor.write(tree.print_dnf_tree())
cursor.close()
"""