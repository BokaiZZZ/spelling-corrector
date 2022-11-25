import numpy as np


def levenshtein_distance(A, B):
    
    # initialize the value matrix 
    nrow = len(A)+1
    ncol = len(B)+1
    matrix = np.zeros((nrow, ncol))
    matrix[0] = range(ncol)
    matrix[:,0] = range(nrow)
    
    # find the levenshtein distance for each position
    for i in range(1, nrow):
        for j in range(1, ncol):
            cost = 1 if A[i-1] != B[j-1] else 0 
            matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + cost)
    return matrix[i][j]


def search_word(sample):
    
    # read the word list from txt file
    f = open("./count_1w.txt", "r")
    for line in f:
        words = [line.strip().split('\t')[0] for line in f.readlines()]
    if sample in words:
        return sample
    else:    
    # calculate the distance and return a most frequent word with least distance 
        distance = []
        for w in words:
            d = levenshtein_distance(sample, w)
            if(d == 1 or d == 0):
                return w
            distance.append(d)
        return words[distance.index(min(distance))]
