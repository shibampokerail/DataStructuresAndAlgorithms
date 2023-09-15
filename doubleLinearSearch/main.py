from doubleLinearSearch import linearSearch
from simulDoubleLinearSearch import runSimulation
import numpy as np

array = np.array([10, 50, 16, 1, 9, 15, 16, 20, 16, 2, 5])  # O(1)
searchValue = 16  # O(1)
searchResult = linearSearch(array, searchValue)  # O(n)
print(searchResult)
print("-------------running-simulation-----------------")
runSimulation()
