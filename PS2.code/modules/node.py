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
import copy

class Node:
    def __init__(self):
        # initialize all attributes
        self.label = None
        self.decision_attribute = None
        self.is_nominal = None
        #self.value = None
        self.splitting_value = None
        self.children = None #Nathan - checkign
        self.name = None

    def __repr__(self):
        return repr(self.label)

    def classify(self, instance):
        '''
        given a single observation, will return the output of the tree
        '''

        current_label = self.label
        current_children = self.children

        if current_children == None:
            return current_label

        #if current_label == 1 or current_label == 0:
        #    return current_label

        else:
            node_index = self.decision_attribute
            att_value = instance[node_index]
            split_value = self.splitting_value
            nominal = self.is_nominal

            while current_children != None:
            #while current_label == None:
                if nominal == False:
                    split_on = split_value

                    if att_value < split_on:
                        next_node = current_children[0]

                    else:
                        next_node = current_children[1]

                else:
                    if att_value in current_children:
                        next_node = current_children[att_value]
                    ### else: return mode of examples classified at this node
                    else:
                        return current_label

                current_children = next_node.children

                if current_children == None: #current_label != None:
                    current_label = next_node.label
                    return current_label

                else:
                    #print current_children
                    node_index = next_node.decision_attribute
                    att_value = instance[node_index]
                    current_children = next_node.children
                    nominal = next_node.is_nominal
                    split_value = next_node.splitting_value

            #return next_node
        
    #for i in data.keys():
    #    root.children.add[i] = child_node
        
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
        returns the disjunct normalized form of the tree. This implementation doesn't give simplest
        label decision first, but I don't know if it matters.
        
        '''
        storage ={0: [], 1: []}
        paths = []
        output = 'IF \n'
        winners = self.get_leaves(self, storage, paths)
        
        for i in range(len(winners[1])):
            output = output + '( '
            for j in range(len(winners[1][i])):
                if winners[1][i][j][1] == -1:
                    output = output + str(winners[1][i][j][0]) + ' == ' + str(winners[1][i][j][2]) + ' '
                else:
                    output = output + str(winners[1][i][j][0]) + ' ' + str(winners[1][i][j][2]) + ' ' + str(winners[1][i][j][1]) + ' '
                if j != len(winners[1][i])-1:
                    output = output + '^ '
            output = output + ') '
            if i !=len(winners[1])-1:
                output = output + 'v \n'
        return output
        
        
    def get_leaves(self, root, storage, path):
        '''
        Given a node, will get a dictionary of all paths to labels. Currently described in 
        terms of attribute name rather than index. May be problematic for pruning - may want to
        return both in the storage dict.
        '''
        current_label = root.label
        current_children = root.children
        
        node_index = root.name
        split_value = root.splitting_value
        attribute_index = root.decision_attribute

        if current_children == None:
        #if current_label == 1 or current_label == 0:
            storage[current_label].append(path)
            
        else:
            current_children = root.children
            split_value = root.splitting_value
            nominal = root.is_nominal
            
            if nominal == True:
                for key in current_children.keys():
                    sub_path = copy.copy(path)
                    sub_path.append([node_index, -1, key, attribute_index])
                    cur = current_children[key]
                    self.get_leaves(cur, storage, sub_path)

            else:
                for i in range(len(current_children)):
                    cur = current_children[i]
                    if i == 0:
                        sub_path = copy.copy(path)
                        sub_path.append([node_index, split_value, '<', attribute_index])
                    elif i == 1:
                        sub_path = copy.copy(path)
                        sub_path.append([node_index, split_value, '>=', attribute_index])
                    else:
                        print 'wut'
                    self.get_leaves(cur, storage, sub_path)
            
        return storage
    

            
        
    
"""
newInstance = [1, 0.6, 1, 0] # outcome, homeaway, dayssincegame, weather
attNames = ["outcome", "homeaway", "dayssincegame", "weather"]

tree = Node()
subtree1 = Node()
subtree2 = Node()
 #output nodes
n0 = Node()
n0.label = 0
n1 = Node()
n1.label = 1


tree.decision_attribute = 1
tree.name = "dayssincegame"
tree.is_nominal = False
tree.splitting_value = 2
tree.children = [subtree1, subtree2]

subtree1.decision_attribute = 2
subtree1.name = "homeaway"
subtree1.is_nominal = True
subtree1.children = {1: subtree2, 0: n0}

subtree2.decision_attribute = 3
subtree2.name = "weather"
subtree2.is_nominal = True
subtree2.children = {0: n1, 1: n0, -1: n0}

output = tree.classify(newInstance)

print output
"""
#output from parse:
#data[0] = array of arrays with attribute values
#data[1] = dictionary {is_nominal: T/F, name: attributeName}
#running decision_tree_driver:
#train_set = data[0]
#attribute_metadata = data[1]



'''
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

#storage1 ={0: [], 1: []}
#path1 = []
#n.get_leaves(n, storage1, path1) # get_leaves requires storage1 and path1 to be assigned prior, print_dnf_tree doesnt
#n.print_dnf_tree()
'''

'''
n0 = Node()
n1 = Node()
n2 = Node()


n = Node()
n.label = None
n.decision_attribute = 1
n.is_nominal = True
n.name = "Nominal attribute"
n0.label = None
n1.label = 1
n2.label = 0
n.children = {0: n0, 1: n1, 2: n2}

n3 = Node()
n4 = Node()

n0.decision_attribute = 2
n0.is_nominal = False
n0.splitting_value = 0.124123412312
n0.children = {0: n3, 1: n4}
n0.name = 'Numerical attribute'
n3.label = 0
n4.label = 1



#storage1 ={0: [], 1: []} 
#path1 = []
#n.get_leaves(n, storage1, path1) # get_leaves requires storage1 and path1 to be assigned prior, print_dnf_tree doesnt
#n.print_dnf_tree()
'''