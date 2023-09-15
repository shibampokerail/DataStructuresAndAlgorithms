from doubleLinearSearch import linearSearch
import numpy as np
array = np.array([10, 50, 16, 1, 9, 15, 16, 20, 16, 2, 5])
searchValue = 16
searchResult = linearSearch(array, searchValue)
print(searchResult) # output should be {5,6}