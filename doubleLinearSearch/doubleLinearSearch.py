import numpy as np  # pip install numpy


def convertToVector(data) -> np.array:
    '''
     So with python there is no specific "vector" variable and I researched and found out that most of the internet
     considers numpy as the vector variable.

     This function:

       ->converts any list,set or map variable into a numpy array i.e vector in python.
       ->Handles the data type mismatch error
       ->takes the "data" variable in as a parameter
       ->returns a numpy array variable

    '''

    vector = {}
    try:
        vector = list(data)
    except Exception as e:
        if isinstance(e, TypeError):
            print(
                "Data Type Mismatch! Please Supply a list of integers as a parameter for LinearSearch function")
            exit()
        else:
            raise Exception(e)

    return vector


def linearSearch(array, searchValue: int) -> set:
    '''
     This function:

       ->converts any list,set or map variable into a numpy array i.e vector using convertToVector method.
       ->takes in two parameters
            ->array : the array variable that is to be searched
            ->searchValue : the integer value that is to be searched in the array variable
       ->searches for two instances of the searchValue in the array
       ->returns a set variable ("{2,3}") with the indexes of the two instances

    '''
    array = convertToVector(array)
    count = 0
    found_indexes = []
    for i in range(len(array)):
        if array[i] == searchValue:
            found_indexes.append(count)
            if len(found_indexes) == 2:
                return set(found_indexes)
        count += 1

    return {-1}

#print(linearSearch([1,3,2,4,5,16,16], 16))
