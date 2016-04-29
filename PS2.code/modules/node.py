# DOCUMENTATION
# =====================================
# Class node attributes:
# ----------------------------
# children - a list of 2 if numeric and a dictionary if nominal.  
#            For numeric, the 0 index holds examples < the splitting_value, the 
#            1 index holds examples >= the splitting value
#
# label - is None if there is a decision attribute, and is the output label (0 or 1 for
#	the homework data set) if there are no other attributes
#       to split on or the data is homogenous
#
# decision_attribute - the index of the decision attribute being split on
#
# is_nominal - is the decision attribute nominal
#
# value - Ignore (not used, output class if any goes in label)
#
# splitting_value - if numeric, where to split
#
# name - name of the attribute being split on

class Node:
    def __init__(self):
        # initialize all attributes
        self.label = None
        self.decision_attribute = None
        self.is_nominal = None
        #self.value = None
        self.splitting_value = None
        self.children = {}
        self.name = None

    def __repr__(self):
        return repr(self.label)

    def classify(self, instance):
        '''
        given a single observation, will return the output of the tree
        '''

        current_label = self.label

        if current_label == 1:
            return current_label

        else:
            node_index = self.decision_attribute
            att_value = instance[node_index]
            current_children = self.children
            split_value = self.splitting_value
            nominal = self.is_nominal

            while current_label == None:
                if nominal == False:
                    split_on = split_value

                    if att_value < split_on:
                        next_node = current_children[0]

                    else:
                        next_node = current_children[1]

                else:
                    next_node = current_children[att_value]

                current_label = next_node.label

                if current_label != None:
                    return current_label

                else:
                    node_index = next_node.decision_attribute
                    att_value = instance[node_index]
                    current_children = next_node.children
                    nominal = next_node.is_nominal
                    split_value = next_node.splitting_value

            return next_node

    def print_tree(self, indent = 0):
        '''
        returns a string of the entire tree in human readable form
        '''
        # Your code here
    	# Nodes whose children are Nodes printed out

        # name of current attribute is one of attribues for Node object
        # series of if-then statements?


        pass


    def print_dnf_tree(self):
        '''
        returns the disjunct normalized form of the tree.
        '''
        pass

#newInstance = [1, 0.6, 1, 0] # outcome, homeaway, dayssincegame, weather
#attNames = ["outcome", "homeaway", "dayssincegame", "weather"]

#tree = Node()
#subtree1 = Node()
#subtree2 = Node()

# output nodes
#n0 = Node()
#n0.label = 0
#n1 = Node()
#n1.label = 1


#tree.decision_attribute = 1
#tree.name = "dayssincegame"
#tree.is_nominal = False
#tree.splitting_value = 2
#tree.children = [subtree1, subtree2]

#subtree1.decision_attribute = 2
#subtree1.name = "homeaway"
#subtree1.is_nominal = True
#subtree1.children = {1: subtree2, 0: n0}

#subtree2.decision_attribute = 3
#subtree2.name = "weather"
#subtree2.is_nominal = True
#subtree2.children = {0: n1, 1: n0, -1: n0}

#output = tree.classify(newInstance)

#print output

        # output from parse:
            #data[0] = array of arrays with attribute values
            #data[1] = dictionary {is_nominal: T/F, name: attributeName}

        # running decision_tree_driver
            # train_set = data[0]
            # attribute_metadata = data[1]

