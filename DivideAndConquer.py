import sys
import math 
sys.setrecursionlimit(100000)

#Maximum Sum Sub-Array
def MAX_CROSSING_SUBARRAY(A, low, high, mid): # O(n)
    leftindex = 0
    rightindex = 0
    #Left 
    leftsum = -10000
    sum = 0
    for i in range(mid, low, -1):
        sum = sum + A[i]
        if sum > leftsum:
            leftsum = sum
            leftindex = i
    #Right
    rightsum = -10000
    sum = 0
    for i in range(mid+1,high):
        sum = sum + A[i]
        if sum > rightsum: 
            rightsum = sum
            rightindex = i
    return leftindex, rightindex, leftsum + rightsum

def MAX_SUBARRAY(A, low, high): #O(n)
    #base case:
    if high == low:
        return low, high, A[low-1]
    #recursive case:
    else:
        mid = (low + high)//2
        leftlow, lefthigh, leftsum = MAX_SUBARRAY(A, low, mid)
        rightlow, righthigh, rightsum = MAX_SUBARRAY(A, mid+1, high)
        crosslow, crosshigh, crosssum = MAX_CROSSING_SUBARRAY(A, low, high, mid)
        if leftsum > rightsum and leftsum > crosssum:
            return leftlow, lefthigh, leftsum
        elif rightsum > leftsum and rightsum > crosssum:
            return rightlow, righthigh, rightsum
        else:
            return crosslow, crosshigh, crosssum
        
#To consider: Strassen's algorithm