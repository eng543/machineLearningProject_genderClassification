import csv, collections

def clean_data(fileToRead, attributes):
    '''
    deal with missing data
    called inside parse function

    nominal: impute mode
    numeric: impute mean
    '''

    att_values = {}

    for row in fileToRead:
        temp = row[0].split(',')
        for i in range(len(temp)): # loop through attributes in an example
            if i in att_values.keys():
                if temp[i] == '?': # ignore the missing attribute values
                    continue
                else:
                    att_values[i].append(float(temp[i])) # put the rest of the values in a dictionary with attribute index as key
            else:
                if temp[i] == '?':
                    continue
                else:
                    att_values[i] = [float(temp[i])]

    att_means = {} # dictionary to store mean or mode for attribute at each index

    for j in att_values.keys():
        if attributes[j]['is_nominal']:
            # use mode of attribute
            sub_data = collections.Counter(att_values[j])
            att_means[j] = sub_data.most_common(1)[0][0]

        if not attributes[j]['is_nominal']:
            # use mean of attribute
            att_means[j] = sum(att_values[j])/float(len(att_values[j]))

    return att_means

#clean_data("../data/test_btrain.csv")




# Note: nominal data are integers while numeric data consists of floats
def parse(filename, keep_unlabeled):
    '''
    takes a filename and returns attribute information and all the data in array of arrays
    This function also rotates the data so that the 0 index is the winner attribute, and returns
    corresponding attribute metadata
    '''
    # initialize variables
    array = []
    csvfile = open(filename,'rb')
    fileToRead = csv.reader(csvfile, delimiter=' ',quotechar=',')

    # skip first line of data
    fileToRead.next()

    # set attributes
    attributes = [
    {
        'name': "winpercent",
        'is_nominal': False
    },
    {
        'name': "oppwinningpercent",
        'is_nominal': False
    },
    {
        'name': "weather",
        'is_nominal': True
    },
    {
        'name': "temperature",
        'is_nominal': False
    },
    {
        'name': "numinjured",
        'is_nominal': False
    },
    {
        'name': "oppnuminjured",
        'is_nominal': False
    },
    {
        'name': "startingpitcher",
        'is_nominal': True
    },
    {
        'name': "oppstartingpitcher",
        'is_nominal': True
    },
    {
        'name': "dayssincegame",
        'is_nominal': False
    },
    {
        'name': "oppdayssincegame",
        'is_nominal': False
    },
    {
        'name': "homeaway",
        'is_nominal': True
    },
    {
        'name': "rundifferential",
        'is_nominal': False
    },
    {
        'name': "opprundifferential",
        'is_nominal': False
    },
    {
        'name': "winner",
        'is_nominal': True
    }]

    att_means = clean_data(fileToRead, attributes)

    csvfile = open(filename,'rb')
    fileToRead = csv.reader(csvfile, delimiter=' ',quotechar=',')

    # skip first line of data
    fileToRead.next()

    # iterate through rows of actual data
    for row in fileToRead:
        # change each line of data into an array
        temp =row[0].split(',')
        if (not keep_unlabeled) and (temp[len(attributes) - 1] == "?"):
            continue
        for i in range(len(temp)):
            # data preprocessing
            if temp[i] == '?':
                temp[i] = att_means[i]

            elif attributes[i]['is_nominal']:
                temp[i] = int(temp[i])
            else:
                temp[i] = float(temp[i])

        # rotate data so that the target attribute is at index 0
        d = collections.deque(temp)
        d.rotate(1)
        array.append(list(d))

    array.pop()

    # rotate attributes so that it corresponds to the data
    attributes = collections.deque(attributes)
    attributes.rotate(1)
    attributes = list(attributes)

    return array, attributes

data = parse("../data/test_btrain.csv", True)[0]

attributes = parse("../data/test_btrain.csv", True)[1]

#print data