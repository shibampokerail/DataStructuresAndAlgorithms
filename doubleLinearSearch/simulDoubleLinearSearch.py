import numpy as np  # pip install numpy
import random
import math


def convertToVector(data) -> np.array:
    '''
     So with python there is no specific "vector" variable and I researched and found out that most of the internet
     considers numpy as the vector variable because they are similar and are directly implemented in C .

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


def runSimulation():
    N_values = [10000, 20000, 35000, 50000, 75000, 100000]
    num_iterations = 1000

    for N in N_values:
        comparisons = []
        hit = 0
        miss = 0
        vector_variable = CreateRandomBatchData(N)
        for _ in range(num_iterations):
            # Generate N random values in the range [0, 15000]

            search_value = random.randint(0, 15000)
            search = linearSearch(vector_variable, search_value)
            if search[0] == True:
                hit += 1
            else:
                miss += 1
            comparisons.append(search[1])
        comparisons.sort()
        average = sum(comparisons) / len(comparisons)
        print("Input:", N)
        print("Hits:", hit)
        print("miss:", miss)
        print("min_steps:", comparisons[0])
        print("avg_steps:", average)
        print("Total_comparisions:", sum(comparisons))


def linearSearch(array, searchValue: int):
    '''
       Converts any list,set or map variable into a numpy array i.e vector using convertToVector method.
       ->takes in two parameters
            ->array : the array variable that is to be searched
            ->searchValue : the integer value that is to be searched in the array variable
       ->searches for two instances of the searchValue in the array
       ->returns a set value with a boolean value and the number of total comparisons
    '''
    array = convertToVector(array)  # c1
    count = 0  # c2
    found_indexes = []  # c3
    comp1 = 0
    comp2 = 0
    for i in range(len(array)):
        comp1 += 1
        if array[i] == searchValue:  # compare with individual
            found_indexes.append(count)
            comp2 += 1
            if len(found_indexes) == 2:  # when two instances are found
                return (True, comp1 + comp2)
        count += 1

    return (False, comp1 + comp2)


# print(linearSearch([1,3,2,4,5,16,16], 16))

def CreateRandomBatchData(VECTOR_SIZE: int) -> np.array:
    '''
      Creates a vector or in this case a numpy array on random numbers between 0-1500 according to the size specified in parameter
      :param : VECTOR_SIZE -> size of the required vector
      :return : test_values -> vector with randomized integer values
    '''

    test_values = np.array([])

    for j in range(VECTOR_SIZE):
        test_values = np.append(test_values, np.array(random.randint(0, 15000)))

    np.sort(test_values)
    return test_values

