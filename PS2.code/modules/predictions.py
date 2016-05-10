import os.path
from operator import xor
from parse import *
from node import *
import csv
import pandas as pd

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
    test_data = pd.read_csv('data/btest.csv', sep=',')
    test_data.drop(' winner', inplace=True, axis=1)

    output = []

    for i in range(len(data_set)):
        output.append(str(tree.classify(data_set[i])))

    test_data['predictions'] = output

    test_data.to_csv('data/PS2.csv', index=False)
