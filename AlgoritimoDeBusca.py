import numpy as np
sequenciaCorreta = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sequenciaErrada =  [0, 1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

def binarySearch (array, begin = 0, end = None):
    if end is None:
        end = len(array) - 1
    if begin <= end: 
        m = (begin + end) // 2
        if array[m] != sequenciaErrada[m] and array[m-1] != sequenciaErrada[m-1]:
            return binarySearch(array, begin, m - 1)
        elif array[m] != sequenciaErrada[m] and array[m-1] == sequenciaErrada[m-1]:
            print(sequenciaErrada[m])
        else:
            return binarySearch(array, m + 1, end)

binarySearch(sequenciaCorreta)  