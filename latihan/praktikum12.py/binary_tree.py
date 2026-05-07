class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert_root(self, data):
        self.root = Node(data)
        
    def insert_left(self, parent_node, data):
        if parent_node.left is None:
            parent_node.left = Node(data)
        else:
            new_node = Node(data)
            new_node.left = parent_node.left
            parent_node.left = new_node
    
    def insert_right(self, parent_node, data):
        if parent_node.right is None:
            parent_node.right = Node(data)
        else:
            new_node = Node(data)
            new_node.right = parent_node.right
            parent_node.right = new_node
            
def preorder(node):
    if node is None:
        return [] 
    
    hasil = []
    hasil.append(node.data) 
    hasil.extend(preorder(node.left)) 
    hasil.extend(preorder(node.right)) 
    return hasil
        
def inorder(node):
    if node is  None:
        return []
    
    hasil = []
    hasil.extend(inorder(node.left))
    hasil.append(node.data)
    hasil.extend(inorder(node.right))
    return hasil
        
def postorder(node):
    if node is  None:
        return []
    
    hasil = []
    hasil.extend(postorder(node.left))
    hasil.extend(postorder(node.right))
    hasil.append(node.data)
    return hasil
        
def leaf_node(node, leaves_list):
    if node is None:
        return
    
    if node.left is None and node.right is None:
        leaves_list.append(node.data)
    
    leaf_node(node.left, leaves_list)
    leaf_node(node.right, leaves_list)
        
tree = BinaryTree()

tree.insert_root("A")
tree.insert_left(tree.root, "B")
tree.insert_right(tree.root, "C")
tree.insert_left(tree.root.left, "D")
tree.insert_right(tree.root.left, "E")
tree.insert_left(tree.root.right, "F")

print(f"\nSISTEM AUDIT DISTRIBUSI \"CEPAT SAMPAI\"")
print("="*38)

print("\n[INFO] Membangun Struktur Gudang...")
print("[INFO] Struktur Berhasil Dibuat.")

temp = preorder(tree.root)
Preorder = "-".join(temp)

temp = inorder(tree.root)
Inorder = "-".join(temp)

temp = postorder(tree.root)
Postorder = "-".join(temp)

print("\nHASIL AUDIT:")
print("1. Pre-Order : ", Preorder )
print("2. In-Order :", Inorder)
print("3. Post-Order:", Postorder)

leaves = []
leaf_node(tree.root, leaves)
Leave = ", ".join(leaves)

print("\n[DATA] Gudang Ujung (Leaf Nodes):", Leave)

print("="*38)
print("Audit Selesai!")
print()


