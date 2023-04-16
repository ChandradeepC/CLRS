#Stacks LIFO

class STACK:

    def __init__(self):
        self.array = []
        self.top = 0
    
    def STACK_EMPTY(self):
        return self.top == 0

    def PUSH(self,x):
        self.top += 1
        if len(self.array) < self.top: #Take note here
            self.array.append(x)
        else: 
            self.array[self.top-1] = x #and here 
    
    def POP(self):
        if self.STACK_EMPTY():
            print("underflow")
        else: 
            self.top -= 1


    def display(self):
        return self.array[:self.top]
    

#Non recursively reversing a singly linked list in expected O(n) time and O(1) storage.

class NODE:

    def __init__(self,key,next=None):
        self.key = key
        self.next = next
    
    def __str__(self):
        return str(self.key)

class LIST:

    def __init__(self,values=None):
        self.head = None
        self.tail = None

        if values:
            self.MULTI_INSERT(values)
    
    def INSERT(self,value):
        
        if not self.head:
            self.tail = self.head = NODE(value)
        else:
            self.tail.next = NODE(value)
            self.tail = self.tail.next 
    
    def MULTI_INSERT(self,values):
        for value in values:
            self.INSERT(value)
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next 

    def __str__(self):
        return ' -> '.join([str(node) for node in self])
    
    def REVERSE(self): #3 pointer approach was correct just needed to print it correctly
        curr = self.head
        next = None
        prev = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        self.head = prev

            