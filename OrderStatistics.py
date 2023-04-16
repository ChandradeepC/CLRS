import math

def MINIMUM(A): #n-1 comparisons , O(n)
    min = A[0]
    for i in range(1,len(A)):
        if min > A[i]:
            min = A[i]
    return min

#SELCTION PROBLEM. suppose distinct and linear expected running time
from random import randint

def PARTITION(A, low, high): #LOMUTO PARTITION
    pivot = A[high]
    i = low-1
    
    for j in range(low, high): #Take special note of these two lines
        if A[j] < pivot: #Take special note of these two lines
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i+1], A[high] = A[high], A[i+1]
    return i+1    

def RANDOM_PARTITION(A, low, high): #Better average running time and used more practically
    x = randint(low,high)
    A[x], A[high] = A[high], A[x]
    return PARTITION(A,low,high)

def RANDOMIZED_SELECT(A,low,high,i): #expected linear time
    if low == high:
        return A[low]
    
    pivot = RANDOM_PARTITION(A,low,high)
    k = pivot - low + 1

    if i == k:
        return A[pivot]
    elif i < k:
        return RANDOMIZED_SELECT(A,low,pivot-1,i)
    else:
        return RANDOMIZED_SELECT(A,pivot+1,high,i-k)
    

#Applications

def K_QUANTILES(A,low,high,k, Q): #Would be nlogn with sorting and division but can be done in nlogk time
    if k == 1:
        return
    else:
        n = high-low+1
        i = math.floor(k/2)
        statistic = math.floor(i*n/k)
        x = RANDOMIZED_SELECT(A, low, high, statistic) #This partitions it as well along x
        print("low:",low,"high:",high,"stat:",statistic,"array:",A, "element:",x)
        Q.append(x)
        #MOD_PARTITION(A, low, high, x)
        K_QUANTILES(A, low, low+statistic, math.floor(k/2), Q) #Fuck this was hard
  
        K_QUANTILES(A, low+statistic, high, math.ceil(k/2), Q) #But i figured it out myself
        #overall error is always within 2

A = [1,0.11, 0.13,2,3,4.5,5,6,6.5,78,65,5.55,4,5.11, 5.67, 5.66, 9.09, 20,0.45, 3.456]
Q = []
K_QUANTILES(A, 0, len(A)-1, 7, Q)
Q

#Median of 2 sorted arrays in O(log n) time
#CLRS median definition is weird
#Correct median + Correct Implementation for two arrays of size n with log(n) time
import math
from statistics import median

def slice(X,k): #absolutely insane step
    if len(X) % 2 == 0:
        return X[:k//2]
    else:
        return X[:k//2 + 1]

def MEDIAN_2(X,Y): #O(log n)

    print(X,Y, median(X),median(Y))

    if len(X) <= 2:
        return (max(X[0],Y[0]) + min(X[1],Y[1])) / 2
    elif median(X) < median(Y):
        return MEDIAN_2(X[(len(X))//2:], slice(Y,len(Y)))
    else:
        return MEDIAN_2(slice(X,len(X)), Y[(len(Y))//2:])


X = [1,12,15,26,38]
Y = [2,13,17,30,45]
MEDIAN_2(X,Y)


#Oil company determine best fit line in O(n) time
#x axis does not matter, just find the y medians in linear time. 

#Weighted median
#Using n log n sorting algorithm - trivial 
#Using expected linear time select algorithm 

from random import randint

def WEIGHTED_PARTITION(A, W, low, high): #LOMUTO PARTITION
    pivot = A[high-1]
    i = low-1
    
    for j in range(low, high-1): #Take special note of these two lines
        if A[j] < pivot: #Take special note of these two lines
            i += 1
            A[i], A[j] = A[j], A[i]
            W[i], W[j] = W[j], W[i]
            print(A,W)
    
    A[i+1], A[high-1] = A[high-1], A[i+1]
    W[i+1], W[high-1] = W[high-1], W[i+1]
    print(A, W)
    return i+1

def WEIGHTED_RANDOM_PARTITION(A, W, low, high): #Better average running time and used more practically
    x = randint(low,high-1)
    A[x], A[high-1] = A[high-1], A[x]
    W[x], W[high-1] = W[high-1], W[x]
    return WEIGHTED_PARTITION(A, W, low,high)


def WEIGHTED_MEDIAN(X,W, low, high, l, r): #Expected linear time
    if low == high:
        return X[low]
    
    pivot = WEIGHTED_RANDOM_PARTITION(X,W,low,high) 

    lsum = sum(W[low:pivot])
    usum = sum(W[pivot+1:high])

    print (X[pivot], X, W, low,high, lsum+l, usum+r, "\n")

    if lsum + l < 0.5 and usum + r <= 0.5:
        return X[pivot]
    elif lsum + l < 0.5 and usum + r > 0.5:
        return WEIGHTED_MEDIAN(X,W,pivot+1,high,l+lsum+W[pivot],r)
    elif lsum + l >= 0.5 and usum + r <= 0.5:
        return WEIGHTED_MEDIAN(X,W,low,pivot,l,r+usum+W[pivot])

# X = [0.1,0.35,0.05,0.1,0.15,0.05,0.2]
# W = [0.1,0.35,0.05,0.1,0.15,0.05,0.2]
# W2 = [0.05,0.05,0.05,0.7,0.05,0.05,0.05]

# WEIGHTED_MEDIAN(X,W2,0,len(X),0,0)

#Post office location: talk to RTD
#weighted median will solve all dimensions with L1 norm. 