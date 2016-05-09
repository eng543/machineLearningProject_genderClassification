from node import *
from ID3 import *
from operator import xor
#import copy

# Crying
# Note, these functions are provided for your reference.  You will not be graded on their behavior,
# so you can implement them as you choose or not implement them at all if you want to use a different
# architecture for pruning.

def reduced_error_pruning(root, tree, full_tree, validation_set, full_accuracy = -1):
    '''
    Take the a node and validation set and returns the improved node.
    Traverses tree using depth first search, pruning each node in order and testing validation accuracy following pruning
    Difference in pruned accuracy and accuracy on full tree stored in prune_diff attribute for Node object.
    Returns a pruned tree as soon as error on full tree no longer exceeds error on pruned trees.
    '''
    
    if full_accuracy == -1:
        full_accuracy = validation_accuracy(root, validation_set)
        print 'made full_accuracy'
        #full_tree = copy.deepcopy(root)
        
        
    #print full_accuracy, 'full_accuracy'
    # use scheme from get_leaves to navigate through the tree
    # copy root node for pruning
    #tree_prune = copy.copy(tree) #copy.deepcopy(root)
    #root_prune = copy.copy(root)
    
    #print len(root.local_data), 'length of local data'
    if root.children == None:
        print 'found a leaf'
        #print 'found labeled node'
        pass

    else:
        
        
        #print root_prune.children
        #root_prune = copy.copy(root_prune)
        #print tree_prune.children[0].children, root_prune.children
        
        placeholder_children = root.children
        #print root.children, 'before'
        root.children = None # Set children to be none
        
        #print tree_prune.children[0].children, root_prune.children
        #print full_accuracy
        #tree_copy = copy(full_tree)
        #tree_copy.
        
        prune_accuracy = validation_accuracy(tree, validation_set) # Run accuracy on potential pruning
        print 'tested a prune'
        #print prune_accuracy, depth
        root.children = placeholder_children #root_prune_perm.children
        #print root.children, 'after'
        
        
        # store pruning - full accuracy in prune_diff attribute for Node object
        # store in original node (not copy), and use that node to continue moving through tree
        root.prune_diff = prune_accuracy - full_accuracy
        print root.prune_diff
        
        
        #tree_copy = copy.copy(tree)
        current_children = root.children
        nominal = root.is_nominal
        
        #root_prune.label = root.mode
        
        #tree.children[0].children[0].children[0]
        if nominal == True:
            for key in current_children.keys():
                cur_node = current_children[key]
                reduced_error_pruning(cur_node, tree, full_tree, validation_set, full_accuracy) # pass accuracy for full tree on to the next step

                #tree_prune_copy
                #tree.children[key] = cur_node
                #tree_prune_copy = copy.copy(tree)
                
                
                #cur_node = tree_copy.current_children[key]
                #tree_copy.cur_prune
                #print cur_prune
                
                #reduced_error_pruning(cur_node, tree, full_tree, validation_set, full_accuracy) # pass accuracy for full tree on to the next step
                
        else:
            for i in range(len(root.children)):
                cur_node = current_children[i]
                reduced_error_pruning(cur_node, tree, full_tree, validation_set, full_accuracy)
                
                #child_placeholder = tree.children[i].children
                #cur_node.children = None
                #prune_accuracy = validation_accuracy(tree, validation_set)
                #cur_node.children = child_placeholder
                #for i in range(len(cur_node.children)):
                    
                
                
                
                #tree_prune_copy = tree_copy
                #cur_node.children = None
                #child_placeholder = tree_copy.children[i].children
                #tree_copy.children[i].children = None
                #prune_accuracy = validation_accuracy(tree_copy, validation_set)
                #tree_prune_copy.children[i].children = child_placeholder
                #cur_node = tree_prune_copy.children[i]
                
                #tree_prune_copy.children[i].children[i].children == None
                #prune_accuracy
        
                
                #reduced_error_pruning(cur_node, tree, full_tree, validation_set, tally, full_accuracy)
                #tree_prune_copy.children[i].children == None
                
                #prune_accuracy = validation_accuracy(tree_prune_copy, validation_set)
                #root.prune_diff = prune_accuracy - full_accuracy
                
                
                
                #cur_node = current_children[key]
                #cur_node = current_children[i]
                #tree.children[i] 
                #= cur_node
                #cur_prune = tree_copy.current_children[i]
                #print cur_prune
                #reduced_error_pruning(cur_node, tree_copy, full_tree, validation_set, tally, full_accuracy)

    max_gain = find_max_gain(root)
    print max_gain, 'max gain, ', root.prune_diff, 'root.prune_diff'
    #print root.children, root.prune_diff, root.decision_attribute
    

    if max_gain > 0:
        # prune whichever node has max gain
        pruned_tree = prune_best_node(root, max_gain)

        # continue pruning using newly pruned tree, reset full_accuracy to default
        reduced_error_pruning(pruned_tree, validation_set, -1)
    else: # if no more improvement in pruned vs. full error, stop and return the resulting pruned tree
        return tree

def find_max_gain(root):
    '''
    Takes a tree undergoing pruning and returns the largest reduction in error when comparing
    error on pruned tree and error on full tree.
    '''
    max_gain = 0

    prune_accuracy = root.prune_diff
    if prune_accuracy > max_gain:
        prune_accuracy = max_gain

    current_children = root.children
    nominal = root.is_nominal

    if current_children != None:
        if nominal == True:
            for key in current_children.keys():
                cur = current_children[key]
                find_max_gain(cur)

        else:
            for i in range(len(current_children)):
                cur = current_children[i]
                find_max_gain(cur)

    return max_gain

def prune_best_node(root, max_gain):
    '''
    Takes a tree undergoing pruning, and the maximum improvement in error after pruning
    Finds the root associated with this error improvement and prunes it from the tree
    Returns a pruned tree
    '''
    root_acc = root.prune_diff

    if root_acc == max_gain:
        root.children = None
        return root

    else:
        current_children = root.children
        nominal = root.is_nominal
        

        if nominal == True:
            for key in current_children.keys():
                cur = current_children[key]
                prune_best_node(cur, max_gain)

        else:
            for i in range(len(current_children)):
                cur = current_children[i]
                prune_best_node(cur, max_gain)


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