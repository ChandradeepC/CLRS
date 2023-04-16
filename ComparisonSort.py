import math
import heapq as hq

#Insertion Sort
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

#Merge Sort (Divide and Conquer)
def MERGE(A, low, mid, high): #O(n)
    n = mid - low + 1
    m = high - mid
    L = [None]*(n+1)
    R = [None]*(m+1)

    for i in range(0,n):
        L[i] = A[low + i] #Differs here
    for j in range(0,m):
        R[j] = A[mid+j+1] #Differs here
    L[n] = math.inf
    R[m] = math.inf

    print(L)
    print(R)

    i = 0
    j = 0

    for k in range(low, high+1): #Differs here
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j+= 1
    print(A)

def MERGE_SORT(A, low, high): #O(n log n)
    if low < high:
        mid = (low+high)//2
        MERGE_SORT(A,low,mid)
        MERGE_SORT(A,mid+1,high)
        MERGE(A,low,mid,high)
    
    return A

#Max-heap
#parent = floor(i/2)
#left child = 2i + 1
#right child = 2i+ 2
#Max heap property: A[parent(i)] >= A[i]


class MAX_HEAP:

    def __init__(self, array, heap_size):
        self.array = array
        self.heap_size = heap_size
    
    def LEFT(self,i):
        return 2*i + 1
    
    def RIGHT(self,i):
        return 2*i + 2
    
    def PARENT(self, i):
        return (i-1)//2

    def MAX_HEAPIFY(self, i): #O(log n)
        l = self.LEFT(i)
        r = self.RIGHT(i)
        if l < self.heap_size and self.array[l] > self.array[i]:
            argmax = l
        else:
            argmax = i
        
        if r < self.heap_size and self.array[r] > self.array[argmax]:
            argmax = r
        
        if argmax != i:
            self.array[i], self.array[argmax] = self.array[argmax], self.array[i]
            self.MAX_HEAPIFY(argmax)
    
    def BUILD_MAX_HEAP(self): #O(n)
        self.heap_size = len(self.array)
        for i in range((len(self.array)-1)//2,-1,-1): #ignoring all the leaves? 
            self.MAX_HEAPIFY(i)
    
    def HEAPSORT(self): #O(n log n)
        self.BUILD_MAX_HEAP() 
        for i in range(len(self.array)-1, 0, -1):
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.heap_size -= 1
            self.MAX_HEAPIFY(0) # n-1 * O(log n) = O(n log n)
    
    #Priority Queue Methods
    def MAX(self):
        return self.array[0]
    
    def POP(self): #O(log n)
        if self.heap_size < 1:
            print("heap underflow")
            return
        max = self.MAX()
        self.array[0] = self.array[self.heap_size-1]
        self.heap_size -= 1
        self.MAX_HEAPIFY(0) #O(log n)
        return max
    
    def INCREASE_KEY(self,i,key): #O(log n)
        if key < self.array[i]:
            print("new key is smaller")
            return
        self.array[i] = key
        while i > 0 and self.array[self.PARENT(i)] < self.array[i]:
            self.array[i], self.array[self.PARENT(i)] = self.array[self.PARENT(i)],  self.array[i]
            i = self.PARENT(i)

    def INSERT(self,key): #O(log n)
        self.heap_size += 1
        self.array.append(-math.inf)
        self.INCREASE_KEY(self.heap_size-1,key) #O(log n)
    
    def DELETE(self,i): #O(log n)
        self.heap_size -=1
        self.array[i] = -math.inf
        self.array[i], self.array[self.heap_size] = self.array[self.heap_size], self.array[i]
        self.array = self.array[0:self.heap_size]
        self.MAX_HEAPIFY(i) #O(log n)

    #To Consider: d-ary heap, 


def MERGE_K(lists): #O(n log k)
    k = len(lists)
    heap = []
    result = []
    for i in range(k): #O(k) time
        heap.append(lists[i][0])
    hq.heapify(heap) #O(k) time
    
    while len(heap) > 0: #O(n log k)
        min = hq.heappop(heap) #O(log k) n times 
        result.append(min)
        
        for j in range(k): #O(log k) n times
            if lists[j][0] == min:
                hq.heappop(lists[j]) #O(log k)
                if len(lists[j]) == 0:
                    lists.pop(j)
                    break
                else:
                    hq.heappush(heap,lists[j][0]) #O(log k)
                    break
    
    return result

#Quicksort, BUGGED IN CLRS and Wikipedia
def PARTITION(A, low, high): #LOMUTO PARTITION
    pivot = A[high]
    i = low-1
    
    for j in range(low, high): #Take special note of these two lines
        if A[j] < pivot: #Take special note of these two lines
            i += 1
            A[i], A[j] = A[j], A[i]
    
    A[i+1], A[high] = A[high], A[i+1]
    return i+1

def QUICKSORT(A, low, high):
    if low < high:
        print(A[low:high])
        x = PARTITION(A, low, high) #O(n)
        print(A[low:high])
        QUICKSORT(A,low,x-1)
        QUICKSORT(A,x+1,high)

from random import randint, sample

def RANDOM_PARTITION(A, low, high): #Better average running time and used more practically
    x = randint(low,high)
    A[x], A[high] = A[high], A[x]
    return PARTITION(A,low,high)

def RANDOM_QUICKSORT(A,low,high):
    if low < high:
        print(A[low:high])
        x = RANDOM_PARTITION(A, low, high) #O(n)
        print(A[low:high])
        RANDOM_QUICKSORT(A,low,x-1)
        RANDOM_QUICKSORT(A,x+1,high)

from statistics import median

def MEDIAN_RANDOM_PARTITION(A, low, high):
    x,y,z = sample(range(low,high+1),3)
    x = median([x,y,z])
    A[x], A[high] = A[high], A[x]
    return PARTITION(A,low,high)

#Application- hybrid + tail recursive + 3-median
#Call needs to be len A - 1, it needs the highest index
def OPTIMIZED_QUICKSORT(A, low, high): #O(nk + nlog(n/k)) = O(nk)
    #Function does not have global minima over reals, analysis depends on hidden constants
    while low < high:
        if (high - low + 1) < 8: 
            INSERTION_SORT(A,low,high+1) #O(n^2) but reduces number of comparisons in almost sorted array
            #Take note of the +1
            break
        else:
            #Only one recursive call using tail recursion
            x = MEDIAN_RANDOM_PARTITION(A, low, high) #O(n)
            OPTIMIZED_QUICKSORT(A,low,x-1)
            low = x+1