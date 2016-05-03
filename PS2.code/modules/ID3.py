import math
from node import Node
import sys



def check_homogenous(data_set):
    '''
    ========================================================================================================
    Input:  A data_set
    ========================================================================================================
    Job:    Checks if the attribute at index 0 is the same for the data_set, if so return output otherwise None.
    ========================================================================================================
    Output: Return either the homogenous attribute or None
    ========================================================================================================
    '''
    # Your code here
    # if homogeneous, means that the tree is finished
    outcomes = [] #Nathan - moved this bit here
    for i in range(0, len(data_set)):
        outcomes.append([data_set[i][0]])
        
    positive_count = 0
    negative_count = 0

    for i in range(0, len(outcomes)):
        if outcomes[i] == [1]:
            positive_count += 1
        else:
            negative_count += 1
    if (positive_count != 0) and (negative_count != 0):
        return None
    else:
        if positive_count != 0:
            return 1
        else:
            return 0

# ======== Test Cases =============================
#data_set = [[0],[1],[1],[1],[1],[1]]
#print check_homogenous(data_set) ==  None
#data_set = [[0],[1],[None],[0]]
#print check_homogenous(data_set) ==  None
#data_set = [[1],[1],[1],[1],[1],[1]]
#print check_homogenous(data_set) ==  1

def gain_ratio_nominal(data_set, attribute):
    '''
    ========================================================================================================
    Input:  Subset of data_set, index for a nominal attribute
    ========================================================================================================
    Job:    Finds the gain ratio of a nominal attribute in relation to the variable we are training on.
    ========================================================================================================
    Output: Returns gain_ratio. See https://en.wikipedia.org/wiki/Information_gain_ratio
    ========================================================================================================
    '''
    freqs = get_hits(data_set)
    total_examples = freqs[0] + freqs[1]

    ent_data_set = []

    for i in range(0, len(data_set)):
        ent_data_set.append([data_set[i][0]])

    total_entropy = entropy(ent_data_set)

    # dict of attribute values and relevant examples
    nom_dict = split_on_nominal(data_set, attribute)


    subset_entropy = 0
    intrinsic_value = 0

    for value in nom_dict.keys():
        # information gain
        num_value = len(nom_dict[value])
        prob_value = num_value/float(total_examples)

        rel_ent_data_set = []

        for i in range(0, len(nom_dict[value])):
            rel_ent_data_set.append([nom_dict[value][i][0]])

        relative_entropy = entropy(rel_ent_data_set)

        subset_entropy += prob_value * relative_entropy

        # intrinsic value
        intrinsic_value += - prob_value * math.log(prob_value, 2)
    if intrinsic_value == 0:
        ratio = 0
    else:
        ratio = (total_entropy - subset_entropy)/intrinsic_value
        
    if ratio < 0.0001: #Nathan: epsilon
        return 0
    else:
        return ratio

# ======== Test case =============================
#data_set, attr = [[1, 2], [1, 0], [1, 0], [0, 2], [0, 2], [0, 0], [1, 3], [0, 4], [0, 3], [1, 1]], 1
#print gain_ratio_nominal(data_set,attr) == 0.11470666361703151
#data_set, attr = [[1, 2], [1, 2], [0, 4], [0, 0], [0, 1], [0, 3], [0, 0], [0, 0], [0, 4], [0, 2]], 1
#print gain_ratio_nominal(data_set,attr) == 0.2056423328155741
#data_set, attr = [[0, 3], [0, 3], [0, 3], [0, 4], [0, 4], [0, 4], [0, 0], [0, 2], [1, 4], [0, 4]], 1
#print gain_ratio_nominal(data_set,attr) == 0.06409559743967516

#data_set, attr = [[0, 3, 0], [0, 3, 1], [0, 3, 1], [0, 4, 2], [0, 4, 2], [0, 4, 3], [0, 0, 0], [0, 2, 1], [1, 4, 2], [0, 4, 2]], 2
#print gain_ratio_nominal(data_set,attr) 

#data_set, attr = [[0, 3, 0], [0, 3, 0], [0, 3, 0], [0, 4, 0], [0, 4, 0], [0, 4, 0], [0, 0, 0], [0, 2, 0], [1, 4, 1], [0, 4, 0]], 2
#print gain_ratio_nominal(data_set,attr) #== 1.0


def mode(data_set):
    '''
    ========================================================================================================
    Input:  A data_set
    ========================================================================================================
    Job:    Takes a data_set and finds mode of index 0.
    ========================================================================================================
    Output: mode of index 0.
    ========================================================================================================
    '''
    outcomes = [] #Nathan - added this bit for simplicity
    for i in range(0, len(data_set)):
        outcomes.append([data_set[i][0]])
        
    positive_count = 0
    negative_count = 0
    for i in range(0, len(outcomes)):
        if outcomes[i] == [1]:
            positive_count += 1
        else:
            negative_count += 1

    if positive_count > negative_count:
        return 1
    else:
        return 0

# ======== Test case =============================
#data_set = [[0],[1],[1],[1],[1],[1]]
#print mode(data_set) == 1
#data_set = [[0],[1],[0],[0]]
#print mode(data_set) == 0

def entropy(data_set):
    '''
    ========================================================================================================
    Input:  A data_set
    ========================================================================================================
    Job:    Calculates the entropy of the attribute at the 0th index, the value we want to predict.
    ========================================================================================================
    Output: Returns entropy. See Textbook for formula
    ========================================================================================================
    '''
    # commented out code creates this list of lists if the input happens to be the entire data_set
    outcomes = []
    for i in range(0, len(data_set)):
        outcomes.append([data_set[i][0]])

    positive_count = 0
    negative_count = 0
    for i in range(0, len(data_set)):
        if data_set[i] == [1]:
            positive_count += 1
        else:
            negative_count += 1

    if positive_count != 0 and negative_count != 0:
        total = float(positive_count + negative_count)
        p_positive = positive_count/total
        p_negative = negative_count/total

        log_positive = math.log(p_positive, 2)
        log_negative = math.log(p_negative, 2)

        entropy_calculation = - ((p_positive * log_positive) + (p_negative * log_negative))

        return entropy_calculation

    else:
        return 0

# ======== Test case =============================
#data_set = [[0],[1],[1],[1],[0],[1],[1],[1]]
#entropy(data_set) == 0.811
#data_set = [[0],[0],[1],[1],[0],[1],[1],[0]]
#print entropy(data_set) == 1.0
#data_set = [[0],[0],[0],[0],[0],[0],[0],[0]]
#print entropy(data_set) == 0

def get_hits(data_set):
    '''
    Create dictionary with tally of number of positive and negative examples.
    ERIN: MIGHT BE GOOD TO USE THIS WITHIN OTHER FUNCTION RATHER THAN INCREMENTING IN VARIABLES EACH TIME
    '''
    hits = {}

    for i in range(len(data_set)):
        if data_set[i][0] in hits:
            hits[data_set[i][0]] += 1
        else:
            hits[data_set[i][0]] = 1

    return hits

def split_on_nominal(data_set, attribute):
    '''
    ========================================================================================================
    Input:  subset of data set, the index for a nominal attribute.
    ========================================================================================================
    Job:    Creates a dictionary of all values of the attribute.
    ========================================================================================================
    Output: Dictionary of all values pointing to a list of all the data with that attribute
    ========================================================================================================
    '''

    values = []

    for i in range(0, len(data_set)):
        values.append(data_set[i][attribute])

    unique_values = list(set(values))

    values_dict = {}

    for val in unique_values:
        values_dict[val] = []

    for i in range(0, len(data_set)):
        att_value = data_set[i][attribute] #Nathan Corrected error: data_set[i][1] -> data_set[i][attribute]
        values_dict[att_value].append(data_set[i])

    return values_dict

# ======== Test case =============================
#data_set, attr = [[0, 4], [1, 3], [1, 2], [0, 0], [0, 0], [0, 4], [1, 4], [0, 2], [1, 2], [0, 1]], 1
#print split_on_nominal(data_set, attr) == {0: [[0, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3]], 4: [[0, 4], [0, 4], [1, 4]]}
#data_set, attr = [[1, 2], [1, 0], [0, 0], [1, 3], [0, 2], [0, 3], [0, 4], [0, 4], [1, 2], [0, 1]], 1
#print split_on_nominal(data_set, attr) == {0: [[1, 0], [0, 0]], 1: [[0, 1]], 2: [[1, 2], [0, 2], [1, 2]], 3: [[1, 3], [0, 3]], 4: [[0, 4], [0, 4]]}
#data_set, attr = [[1, 2, 2], [1, 0, 1], [0, 0, 0], [1, 3, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [0, 4, 1], [1, 2, 2], [0, 1, 2]], 1
#print split_on_nominal(data_set, attr)

#data_set, attr = [[0, 3, 0], [0, 3, 1], [0, 3, 1], [0, 4, 2], [0, 4, 2], [0, 4, 3], [0, 0, 0], [0, 2, 1], [1, 4, 2], [0, 4, 2]], 2
#print split_on_nominal(data_set, attr)

def gain_ratio_numeric(data_set, attribute, steps):
    '''
    ========================================================================================================
    Input:  Subset of data set, the index for a numeric attribute, and a step size for normalizing the data.
    ========================================================================================================
    Job:    Calculate the gain_ratio_numeric and find the best single threshold value
            The threshold will be used to split examples into two sets
                 those with attribute value GREATER THAN OR EQUAL TO threshold
                 those with attribute value LESS THAN threshold
            Use the equation here: https://en.wikipedia.org/wiki/Information_gain_ratio
            And restrict your search for possible thresholds to examples with array index mod(step) == 0
    ========================================================================================================
    Output: This function returns the gain ratio and threshold value
    ========================================================================================================
    '''
    # Your code here
    # max gain_ratio among all possible splits
    # steps = how many times do you calculate the gain_ratio
    # threshold = splitting_value

    freqs = get_hits(data_set)
    total_examples = freqs[0] + freqs[1]

    ent_data_set = []

    for i in range(0, len(data_set)):
        ent_data_set.append([data_set[i][0]])

    total_entropy = entropy(ent_data_set)

    step_indices = []
    k = 0
    if steps < len(data_set):
        while k < len(data_set):
            step_indices.append(k)
            k += steps
    else:
        print("boohoo we failed")
    ratios = {}

    for step in step_indices:
        temp_split_value = data_set[step][attribute] #Nathan: data_set[step][1] -> data_set[step][attribute]

        # anything less than split value is in list at 0th index, greater than equal to in 1th index
        subset_split = [[],[]]
        for i in range(0, len(data_set)):
            #print data_set[i][1], data_set[i][attribute]
            if data_set[i][attribute] < temp_split_value: #Nathan: data_set[step][1] -> data_set[step][attribute]
                subset_split[0].append([data_set[i][0]])
                #print subset_split
            else:
                subset_split[1].append([data_set[i][0]])
                #print subset_split

        subset_entropy = 0
        intrinsic_value = 0

        for value in subset_split:
            # information gain
            prob_value = len(value)/float(total_examples)
            relative_entropy = entropy(value)

            subset_entropy += prob_value * relative_entropy

            # intrinsic value
            ### step 2 case fails here due to 'math domain error'
            ## ending up with prob_value = 0 at some point
            if prob_value == 0 or prob_value == 1:
                intrinsic_value = -1 ### just so we can catch it
            else:
                intrinsic_value += - prob_value * math.log(prob_value, 2)

        if len(subset_split[0]) == 0 or len(subset_split[1]) == 0:
            ratio = 0
        else:
            ratio = (total_entropy - subset_entropy) / intrinsic_value
            #print (total_entropy - subset_entropy)

        ratios[ratio] = temp_split_value
    #print 'grnum =', ratios, '\n'
    max_ratio = max(ratios.keys())
    #print 'grnum max_ratio =', max_ratio, '\n'
    if max_ratio < 0.0001: #Nathan: epsilon
        return 0
    else:
        optimum_threshold = ratios[max_ratio]
        output = (max_ratio, optimum_threshold)
        return output


# ======== Test case =============================
#data_set,attr,step = [[1,0.05], [1,0.17], [1,0.64], [0,0.38], [0,0.19], [1,0.68], [1,0.69], [1,0.17], [1,0.4], [0,0.53]], 1, 2
#print gain_ratio_numeric(data_set,attr,step) == (0.21744375685031775, 0.19)
#data_set,attr,step = [[1, 0.35], [1, 0.24], [0, 0.67], [0, 0.36], [1, 0.94], [1, 0.4], [1, 0.15], [0, 0.1], [1, 0.61], [1, 0.17]], 1, 4
#print gain_ratio_numeric(data_set,attr,step) == (0.11689800358692547, 0.94)
#data_set,attr,step = [[1, 0.1], [0, 0.29], [1, 0.03], [0, 0.47], [1, 0.25], [1, 0.12], [1, 0.67], [1, 0.73], [1, 0.85], [1, 0.25]], 1, 1
#print gain_ratio_numeric(data_set,attr,step) == (0.23645279766002802, 0.29)

#data_set,attr,step = [[1, 0.1, 0.95], [0, 0.29, 0], [1, 0.03, 0.82], [0, 0.47, 0.03], [1, 0.25, 0.84], [1, 0.12, 0.82], [1, 0.67, 0.6], [1, 0.73, 0.6], [1, 0.85, 0.9], [1, 0.25, 0.99]], 2, 1
#print gain_ratio_numeric(data_set,attr,step)


def split_on_numerical(data_set, attribute, splitting_value):
    '''
    ========================================================================================================
    Input:  Subset of data set, the index for a numeric attribute, threshold (splitting) value
    ========================================================================================================
    Job:    Splits data_set into a tuple of two lists, the first list contains the examples where the given
	attribute has value less than the splitting value, the second list contains the other examples
    ========================================================================================================
    Output: Tuple of two lists as described above
    ========================================================================================================
    '''

    less_than = []
    greater_than = []

    for i in range(0, len(data_set)):
        if data_set[i][attribute] < splitting_value:
            less_than.append(data_set[i])
        else:
            greater_than.append(data_set[i])

    return (less_than, greater_than)

# ======== Test case =============================
#d_set,a,sval = [[1, 0.25], [1, 0.89], [0, 0.93], [0, 0.48], [1, 0.19], [1, 0.49], [0, 0.6], [0, 0.6], [1, 0.34], [1, 0.19]],1,0.48
#print split_on_numerical(d_set,a,sval) == ([[1, 0.25], [1, 0.19], [1, 0.34], [1, 0.19]],[[1, 0.89], [0, 0.93], [0, 0.48], [1, 0.49], [0, 0.6], [0, 0.6]])
#d_set,a,sval = [[0, 0.91], [0, 0.84], [1, 0.82], [1, 0.07], [0, 0.82],[0, 0.59], [0, 0.87], [0, 0.17], [1, 0.05], [1, 0.76]],1,0.17
#print split_on_numerical(d_set,a,sval) == ([[1, 0.07], [1, 0.05]],[[0, 0.91],[0, 0.84], [1, 0.82], [0, 0.82], [0, 0.59], [0, 0.87], [0, 0.17], [1, 0.76]])

def pick_best_attribute(data_set, attribute_metadata, numerical_splits_count):
    '''
    ========================================================================================================
    Input:  A data_set, attribute_metadata, splits counts for numeric
    ========================================================================================================
    Job:    Find the attribute that maximizes the gain ratio. If attribute is numeric return best split value.
            If nominal, then split value is False.
            If gain ratio of all the attributes is 0, then return False, False
            Only consider numeric splits for which numerical_splits_count is greater than zero
    ========================================================================================================
    Output: best attribute, split value if numeric
    '''

    ratios = {}

    for i in range(1, len(data_set[0])): # Assumes all points have same number of features, which they definitely should
        if attribute_metadata[i]['is_nominal'] == True: #Nathan: Just changed 1 to True to fix some of my brain confusion
            gain_ratio = gain_ratio_nominal(data_set, i)
            ratios[(i, False)] = gain_ratio

        else:
            if numerical_splits_count[i] != 0:
                gain_ratio = gain_ratio_numeric(data_set, i, 1) #Nathan: May have to change 1 to steps here - need to doublecheck grading method
                if gain_ratio != 0:
                    ratios[(i, gain_ratio[1])] = gain_ratio[0]
                else:
                    pass
            else:
                pass
    #print ratios        
    if len(ratios) != 0: #Nathan: Exception handling
        max_ratio = max(ratios.values())
        #print 'pba max_ratio =', max_ratio
        if max_ratio != 0:
            best_attribute = [x for x,y in ratios.items() if y == max_ratio]
            return best_attribute[0]
        else:
            return (False, False)
    else:
        return (False, False)

# # ======== Test Cases =============================
#numerical_splits_count = [20,20,20]
#attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
#data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [0, 0.51], [1, 0.4]]
#print pick_best_attribute(data_set, attribute_metadata, numerical_splits_count) == (1, 0.51)

#attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': True}]
#data_set = [[0, 0], [1, 0], [0, 2], [0, 2], [0, 3], [1, 1], [0, 4], [0, 2], [1, 2], [1, 5]]
#print pick_best_attribute(data_set, attribute_metadata, numerical_splits_count) == (1, False)

#attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': True}, {'name': "dummy",'is_nominal': True}]
#data_set = [[0, 0, 0], [1, 0, 0], [0, 2, 1], [0, 2, 1], [0, 3, 3], [1, 1, 2], [0, 4, 1], [0, 2, 3], [1, 2, 4], [1, 5, 2]]
#print pick_best_attribute(data_set, attribute_metadata, numerical_splits_count) == (2, False)

#attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': False}, {'name': "dummy",'is_nominal': False}]
#data_set = [[0, 0, 0.3], [1, 0, 0.11], [0, 2, 0.7], [0, 2, 0.9], [0, 3, 0.4], [1, 1, 0.13], [0, 4, 0.1], [0, 2, 0.3], [1, 2, 0.11], [1, 5, 0.12]]
#print pick_best_attribute(data_set, attribute_metadata, numerical_splits_count)

#attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
#data_set = [[1, 0.1], [0, 0.1], [0, 0.1], [0, 0.1], [0, 0.1], [1, 0.1], [1, 0.1], [1, 0.1], [0, 0.1], [1, 0.1]]
#print pick_best_attribute(data_set, attribute_metadata, numerical_splits_count)
# Uses gain_ratio_nominal or gain_ratio_numeric to calculate gain ratio.

def ID3(data_set, attribute_metadata, numerical_splits_count, depth):
    '''
    See Textbook for algorithm.
    Make sure to handle unknown values, some suggested approaches were
    given in lecture.
    ========================================================================================================
    Input:  A data_set, attribute_metadata, maximum number of splits to consider for numerical attributes,
	maximum depth to search to (depth = 0 indicates that this node should output a label)
    ========================================================================================================
    Output: The node representing the decision tree learned over the given data set
    ========================================================================================================
    '''
    # Your code here

    root = Node()
    #print 'depth =', depth
    
    if depth == 0: #Depth check
        root.label = mode(data_set)
    else:
        root.label = check_homogenous(data_set)

    #print 'label=', root.label
    if root.label != None: #If data set isn't homogeneous or max depth
        return root # Finished with this branch
    else:
        best_att = pick_best_attribute(data_set, attribute_metadata, numerical_splits_count)
        #print 'best_att=', best_att
        #print 'data_set=', data_set
        if best_att == (False, False): #Nathan: Exception here since (False, False) can be interpreted as (0, False) and ID3 tries to split on the class
            root.label = mode(data_set)
            #print 'False, False -> label=', root.label
            return root
        else:
            root.decision_attribute = best_att[0]
            root.is_nominal = attribute_metadata[best_att[0]]['is_nominal']
            root.splitting_value = best_att[1]
        
    #outcomes = [] # this is the classes in the data_set - #Nathan: moved all this to check_homogeneous
    #for i in range(0, len(data_set)):
    #    outcomes.append([data_set[i][0]])
    #done = check_homogenous(outcomes)
    #root.label = done
    
            root.name = attribute_metadata[best_att[0]]['name']      
            child_numerical_splits_count = numerical_splits_count
    ### this is not correct
    # root.children should not have subset datasets in values for each attribute thing
            if root.is_nominal == True:
                root.children = {}
                data = split_on_nominal(data_set, root.decision_attribute)
                sub_depth = depth - 1
                for i in data.keys():
                    new_node = ID3(data[i], attribute_metadata, child_numerical_splits_count, sub_depth)
                    #print new_node, 'nom'
                    #print [new_node.classify(x) == x[0] for x in data_set]
                    root.children[i] = new_node
                #root.children = split_on_nominal(data_set, root.decision_attribute)
            
            elif root.is_nominal == False:
                root.children = []
                data = split_on_numerical(data_set, root.decision_attribute, root.splitting_value)
                child_numerical_splits_count[root.decision_attribute] = child_numerical_splits_count[root.decision_attribute]-1
                sub_depth = depth - 1
                for i in range(len(data)):
                    new_node = ID3(data[i], attribute_metadata, child_numerical_splits_count, sub_depth)
                    #print new_node, 'num'
                    root.children.append(new_node)

            else:
                print 'Troubles brewing'
            
    return root

#                best_feature_values = {s.sample[best_feature]
#                                       for s in training_samples}
#                for value in best_feature_values:
#                    samples = [s for s in training_samples
#                               if s.sample[best_feature] == value]
#                    # Recursively, create a child node.
#                    root.children = create_decision_tree(samples,
#                                                      predicting_features)
#                    root_node[value] = child
#        return root_node
    
    
    #while tree.label == None:
    # GenerateTree(X)
    # If NodeEntropy(X) < ThresholdI   **entropy equation 9.3 <---- function below
                        ## threshold = 0.001
        # Create leaf labelled by majority class in X
                        ## mode function
        # Return

    #pick_best_attribute(data_set, attribute_metadata, numerical_splits_count)
    # i <- SplitAttribute(X)
    # For each branch of xi
        # Find Xi falling in branch
        # GenerateTree(Xi)

    # SplitAttribute(X) ## pick_best_attribute()
        # MinEnt <- MAX
        # For all attributes i = 1, ... , d
            # if Xi is discrete with n values
                # Split X into X1, ..., Xn by xi
                # e <- SplitEntropy(X1, ..., Xn) ** impurity equation 9.8
                # if e<MinEnt MinEnt <- e; bestf <- i
            # Else /* xi is numeric*/
                # For all possible splits
                    # Split X into X1, X2, on xi
                    # e <- SplitEntropy(X1, X2)
                    # If e<MinEnt MinEnt <- 3; bestf <- i
        # Return bestf

    ## for all attributes, calculate impurity and choose the one that has the minimum entropy (measured by equation 9.8)


    # somewhere deal with the numerical_splits_count thing

#numerical_split_counts = [20, 20, 20]
#attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': True}, {'name': "dummy",'is_nominal': True}]
#data_set = [[0, 0, 2], [1, 0, 3], [0, 2, 1], [0, 2, 3], [0, 3, 2], [1, 1, 1], [0, 4, 3], [0, 2, 3], [1, 2, 3], [1, 5, 0]]
#print ID3(data_set, attribute_metadata, numerical_split_counts, depth = 5)

#numerical_split_counts = [20, 20, 20]
#attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': True}, {'name': "dummy",'is_nominal': False}]
#data_set = [[0, 0, 0.3], [1, 0, 0.11], [0, 2, 0.7], [0, 2, 0.9], [0, 3, 0.4], [1, 1, 0.13], [0, 4, 0.1], [0, 2, 0.3], [1, 2, 0.11], [1, 5, 0.12]]
#print ID3(data_set, attribute_metadata, numerical_split_counts, depth = 5)

#numerical_split_counts = [20, 20, 20]
#attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "weather",'is_nominal': True}, {'name': "dummy",'is_nominal': False}]
#data_set = [[0, 0, 0.1], [1, 0, 8], [0, 2, 0.2], [0, 2, 0.1], [0, 3, 0.4], [1, 1, 10], [0, 4, 0.1], [0, 2, 0.1], [1, 2, 15], [1, 5, 3]]
#print ID3(data_set, attribute_metadata, numerical_split_counts, depth = 0)

#attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
#data_set = [[0, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [0, 0.01], [0, 0.33], [0, 0.42], [0, 0.42], [0, 0.51], [0, 0.4]]
#numerical_splits_count = [5, 5]
#print ID3(data_set, attribute_metadata, numerical_splits_count, 0)

#attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
#data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [1, 0.42], [0, 0.51], [1, 0.4]]
#numerical_splits_count = [1, 1]
#n = ID3(data_set, attribute_metadata, numerical_splits_count, 5)
#print n == [True, False, True, True, False, True, True, True, True, True, True]

#attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
#data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [1, 0.42], [0, 0.51], [1, 0.4]]
#numerical_splits_count = [5, 5]
#print ID3(data_set, attribute_metadata, numerical_splits_count, 5)
#print n
#n_classify = [n.classify(x) == x[0] for x in data_set]
#print n_classify
#if n and [n.classify(x) == x[0] for x in data_set] == [True, False, True, True, False, True, True, True, True, True, True]:

#attribute_metadata = [{'name': "winner",'is_nominal': True},{'name': "opprundifferential",'is_nominal': False}]
#data_set = [[1, 0.27], [0, 0.42], [0, 0.86], [0, 0.68], [0, 0.04], [1, 0.01], [1, 0.33], [1, 0.42], [1, 0.42], [0, 0.51], [1, 0.4]]
#numerical_splits_count = [5, 5]
#n = ID3(data_set, attribute_metadata, numerical_splits_count, 5)
# n and [n.classify(x) == x[0] for x in data_set] == [True, False, True, True, True, True, True, True, True, True, True]:
#print n
#n_classify = [n.classify(x) == x[0] for x in data_set]
#print n_classify