#BST property: left children <= node <= right children
#BST can be a priority queue or dictionary
#Supports search, minimum, maximum, predecessor, successor, insert and delete
#Worst case O(n) for operations when the tree is completely unbalanced
#Expected time O(log n)
#Time = O(h) where h is the height of the tree
#Takes O(n) time to walk the tree

#Needs to be implemented 


class Node:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None
    
    def __str__(self):
        return str(self.key)

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self,z):
        y = None        #Trailing pointer always stays above x
        x = self.root   #Traversal pointer
        #Trying to find the empty spot and its parent
        while x:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        #Inserting z
        z.parent = y
        if not y:
            self.root = z
        #placing z in the correct position. 
        elif z.key < y.key:
            y.left = z
        else: 
            y.right = z
    
        
    def bf_traverse(self): #Breadth first walk using list that is only appended to
        Q = [self.root] #This is possible due to the BST property maintained by insert
        while Q:
            print(' '.join(str(node) for node in Q))
            newQ = []
            for node in Q:
                if node.left:
                    newQ.append(node.left)
                if node.right:
                    newQ.append(node.right)
            Q = newQ
    
    def inorder_tree_walk(self,x): #O(n), can print it out in sorted order
        if x:
            self.inorder_tree_walk(x.left)
            print(x,end=' ')
            self.inorder_tree_walk(x.right)
    
    def search(self,x ,k):
        while x and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x
    
    def max(self,x):
        while x.right:
            x = x.right
        return x
    
    def min(self,x):
        while x.left:
            x = x.left
        return x

    def successor(self, x):
        if x.right:
            return self.min(x.right)
        y = x.parent
        while y and x == y.right:
            x = y
            y = y.parent
        return y

    
    #THEOREM: If a node has two children, its successor has no left child
    #and predecessor has no right child. 
    
    #Completely gets rid of u though

    def transplant(self,u,v):
        if not u.parent: #if u is the root
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        
        if v:
            v.parent = u.parent

    def delete(self,z):
        if not z.left:
            self.transplant(z,z.right)
        elif not z.right:
            self.transplant(z,z.left)
        else:
            y = self.min(z.right) #Why not just use successor method here?
            if y.parent != z: #if parent was not z, otherwise this is not required
                self.transplant(y,y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z,y)
            y.left = z.left
            y.left.parent = y