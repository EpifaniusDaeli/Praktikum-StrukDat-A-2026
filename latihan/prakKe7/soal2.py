class Node:
    def __init__(self, plat):
        self.plat = plat
        self.next = None
        
def tambahKendaraan(head, plat):
    newNode = Node(plat)
    if head is None:
        return newNode
    else:
        current = head
        while current.next:
            current = current.next
        current.next = newNode
        return head
    
def hapusKendaraan(head, key):
    current = head
    previous = None
    
    if current and current.data == key:
        head = current.next
        current = None
        return head
    
    while current and current.data != key:
        previous = current
        current = current.next
        
    if current is None:
        return head
    
    previous.next = current.next
    current = None
    
    return head

def Traversal(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("Null")