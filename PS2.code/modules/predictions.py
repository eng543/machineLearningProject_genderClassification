import os.path
from operator import xor
from parse import *
from node import *
import csv

# DOCUMENTATION
# ========================================
# this function outputs predictions for a given data set.
# NOTE this function is provided only for reference.
# You will not be graded on the details of this function, so you can change the interface if 
# you choose, or not complete this function at all if you want to use a different method for
# generating predictions.

def create_predictions(tree, predict):
    '''
    Given a tree and a url to a data_set. Create a csv with a prediction for each result
    using the classify method in node class.
    '''
    data_set = parse(predict, True)[0]

    # classify each instance in test set
    # save classification output to csv file
    with open('data/btest_prediction.csv', 'wb') as csvfile:
        output = csv.writer(csvfile, delimiter = ',')

        for i in range(len(data_set)):
            output.writerow(str(tree.classify(data_set[i])))
