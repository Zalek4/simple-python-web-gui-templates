import string

def create_dictionary():

    # Make a dictionary with 10 entries, that are each formatted like 'a : 1'
    dictionary = dict()
    for i in range(10):
        letter = string.ascii_lowercase[i]
        dictionary[letter] = i

    return(dictionary)