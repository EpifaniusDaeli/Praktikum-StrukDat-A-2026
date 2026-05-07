class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, data=None):
        if data is not None:
            self.root = Node(data)
        else:
            self.root = None

    def insert(self, data):
        new = Node(data)
        if self.root is None:
            self.root = new
            return

        P = None
        Q = self.root

        while Q is not None and new.data != Q.data:
            P = Q
            if new.data < Q.data:
                Q = Q.left
            else:
                Q = Q.right

        if Q is not None and new.data == Q.data:
            print(f"Data {data} duplikat")
            return

        if new.data < P.data:
            P.left = new
        else:
            P.right = new

def inorder(node):
    if node:
        inorder(node.left)       
        print(node.data, end=' ')
        inorder(node.right)      


bst = BinarySearchTree()

bst.insert(65)    
bst.insert(76)           
bst.insert(45)           
bst.insert(65)          
bst.insert(50) 

inorder(bst.root)