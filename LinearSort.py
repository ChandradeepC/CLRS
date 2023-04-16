import math

#Counting Sort
def COUNTING_SORT(A,k):
    B = [None]*len(A)
    C = [0]*(k+1) #Take note
    for j in range(0,len(A)): #O(n)
        C[A[j]] = C[A[j]] + 1 #Counting the number of elements equal to index
    
    print(C)
    #Cumulative sum to determine number of elements leq to index
    for i in range(1,k+1): #O(k)
        C[i] = C[i] + C[i-1]
    print(C)
    #Entering in to correct sorted position in B
    for j in range(len(A)-1, -1, -1): #O(n)
        B[C[A[j]]-1] = A[j] #Take note
        C[A[j]] -= 1
    
    for i in range(0,len(A)):
        A[i] = B[i]


#Radix Sort: Fucking useless and cannot be implemented so easily

#Imported Insertion Sort
def INSERTION_SORT(A, low, high): #O(n**2)
    for i in range(low+1,high):
        key = A[i]
        #Assume the left hand side is sorted
        j = i - 1
        while j > -1 and A[j] > key:
            A[j+1] = A[j]
            j = j - 1
        A[j+1] = key
    
    return A

#Bucket Sort: Assume input comes from uniform distribution from [0,1)

def BUCKET_SORT(A):
    B = [[] for i in range(len(A))] #Be very careful 
    for i in range(len(A)):
        B[math.floor(len(A)*A[i])].append(A[i])
    X = []
    print(B)

    for i in range(len(A)):
        B[i] = INSERTION_SORT(B[i], 0, len(B[i]))
        X += B[i]

    for i in range(len(A)):
        A[i] = X[i]


