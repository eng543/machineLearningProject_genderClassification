from random import shuffle
from ID3 import *
from operator import xor
from parse import parse
import matplotlib.pyplot as plt
import os.path
from pruning import validation_accuracy
import numpy as np
import copy

# NOTE: these functions are just for your reference, you will NOT be graded on their output
# so you can feel free to implement them as you choose, or not implement them at all if you want
# to use an entirely different method for graphing

def get_graph_accuracy_partial(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, pct):
    '''
    get_graph_accuracy_partial - Given a training set, attribute metadata, validation set, numerical splits count, and percentage,
    this function will return the validation accuracy of a specified (percentage) portion of the training setself.
    '''
    # single accuracy for whatver percentage you've chosen
    # call validation_accuracy from pruning.py
    shuffle(train_set)
    sub_data = train_set[0:pct]
    sub_numerical_splits_count = copy.copy(numerical_splits_count)
    sub_tree = ID3(sub_data, attribute_metadata, sub_numerical_splits_count, depth)
    accuracy = validation_accuracy(sub_tree, validate_set)
    return accuracy

def get_graph_data(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, iterations, pcts):
    '''
    Given a training set, attribute metadata, validation set, numerical splits count, iterations, and percentages,
    this function will return an array of the averaged graph accuracy partials based off the number of iterations.
    '''
    avg_accuracies = []
    pcts_copy = []
    for data_pct in pcts:
        accs = []
        for i in range(iterations):
            acc = get_graph_accuracy_partial(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, data_pct)
            accs.append(acc)
        avg_accuracies.append(np.mean(accs))
        print data_pct, 'checked'
    return avg_accuracies

# get_graph will plot the points of the results from get_graph_data and return a graph
def get_graph(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, iterations, lower, upper, increment):
    '''
    get_graph - Given a training set, attribute metadata, validation set, numerical splits count, depth, iterations, lower(range),
    upper(range), and increment, this function will graph the results from get_graph_data in reference to the drange
    percentages of the data.
    '''
    
    percentages = np.arange(lower, upper, increment).tolist()
    pcts_index = [int(round(i)) for i in np.multiply(percentages,len(train_set))]
    percentages.append(1.0)
    pcts_index.append(len(train_set)-1)
    accuracies = get_graph_data(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, iterations, pcts_index)
    
    plt.plot(percentages, accuracies, '-o')
    plt.title('Learning Curves')
    plt.ylabel('Average accuracies')
    plt.xlabel('Fraction of Training Set Used')
    plt.xticks(np.arange(0, 1, 0.1))
    plt.show()
    return percentages, accuracies
    

#train = '/Users/Nathan/machineLearningProject_genderClassification/PS2.code/data/test_btrain.csv'
#train_set, attribute_metadata = parse(train, False)
#validate = '/Users/Nathan/machineLearningProject_genderClassification/PS2.code/data/test_bvalidate.csv'
#validate_set, _ = parse(validate, False)
#numerical_splits_count = [10]*len(attribute_metadata)
#depth = 10
#lower = 0.05
#upper = 1.00
#increment = 0.05
#iterations = 5

#get_graph(train_set, attribute_metadata, validate_set, numerical_splits_count, depth, iterations, lower, upper, increment)