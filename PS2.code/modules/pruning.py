from node import *
from ID3 import *
from operator import xor

# Note, these functions are provided for your reference.  You will not be graded on their behavior,
# so you can implement them as you choose or not implement them at all if you want to use a different
# architecture for pruning.

def reduced_error_pruning(root, training_set, validation_set):
    '''
    take the a node, training set, and validation set and returns the improved node.
    You can implement this as you choose, but the goal is to remove some nodes such that doing so improves validation accuracy.
    '''


    ## get_leaves: {0: [[one path to 0], [another path to 0]],
    #                   1: [[one path to 1], [another path to 1]]}

    # Your code here
    # start at leaves


    # last element in longest path is the node that should be pruned
    leaves = {0: [], 1: []}
    path = []
    leaves_output = root.get_leaves(root, leaves, path)

    ## from get_leaves, find longest path regardless of label
    # value of any key whose length is longest



    #all_leaves = enumerate(leaves[0], leaves[1])
    max0 = max(enumerate(leaves[0]), key = lambda tup: len(tup[1]))


    max1 = max(enumerate(leaves[1]), key = lambda tup: len(tup[1]))

    final_max = max(max0, max1)

    #print leaves[0][max0[0]]

    #print final_max, max(leaves[0][max0[0]], leaves[1][max1[0]])

    # look at parent of leaf
    # trim parent at each depth
    # get validation accuracy after trimming parent
    # if validation accuracy improves, keep pruning
    # if validation accuracy gets worse, stop pruning
  #  return leaves
# 

def validation_accuracy(tree, validation_set):
    '''
    takes a tree and a validation set and returns the accuracy of the set on the given tree
    '''
    classify_output = []

    for i in range(len(validation_set)):
        #print validation_set[i]
        classify_output.append(tree.classify(validation_set[i]))

    accuracy = sum(classify_output)/float(len(validation_set))

    return accuracy

n0 = Node()
n1 = Node()


n = Node()
n.label = None
n.decision_attribute = 1
n.is_nominal = False
n.splitting_value = 0.5
n.name = "Numerical attribute"


n0.label = None
n1.label = None
#n.children = {1: n0, 2: n1}
n.children = [n0, n1]
n2 = Node()
n2.label = 0
n3 = Node()
n3.label = 1
n0.children = [n2, n3]
n0.decision_attribute = 2
n0.is_nominal = False
n0.splitting_value = 1.5
n0.name = "Second Numerical attribute"
n4 = Node()
n4.label = 0
n5 = Node()
n5.label = 1
n4.label = 0
n5.label = 1
n1.children = [n4, n5]
n1.decision_attribute = 3
n1.is_nominal = False
n1.splitting_value = 3.5

#print reduced_error_pruning(n)