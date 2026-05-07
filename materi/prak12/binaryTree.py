class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert_root(self, data):
        self.root = Node(data)
    
    def insert_left(self, parent_node, data):
        if parent_node is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.next = parent_node.left
            parent_node.left = new_node
            
    def insert_right(self, parent_node, data):
        if parent_node is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.next = parent_node.right
            parent_node.right = new_node
            
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.data, end='->')
            self.inorder_traversal(node.right) 
            
tree = BinaryTree()





            
            
    