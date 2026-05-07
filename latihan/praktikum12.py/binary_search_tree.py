class Node:
    def __init__(self, id_buku, judul):
        self.id_buku = id_buku
        self.judul = judul
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self._counter = 1

    def insert(self, id_buku, judul):
        if self.root is None:
            self.root = Node(id_buku, judul)
        else:
            self._insert_bantuan(self.root, id_buku, judul)
        print(f"[INSERT] Berhasil memasukkan: ID {id_buku} - {judul}")

    def _insert_bantuan(self, current, id_buku, judul):
        if id_buku < current.id_buku:
            if current.left is None:
                current.left = Node(id_buku, judul)
            else:
                self._insert_bantuan(current.left, id_buku, judul)
        elif id_buku > current.id_buku:
            if current.right is None:
                current.right = Node(id_buku, judul)
            else:
                self._insert_bantuan(current.right, id_buku, judul)

    def search(self, id_buku):
        return self._search_rekursif(self.root, id_buku)

    def _search_rekursif(self, node_sekarang, id_buku):
        if node_sekarang is None or node_sekarang.id_buku == id_buku:
            return node_sekarang
        if id_buku < node_sekarang.id_buku:
            return self._search_rekursif(node_sekarang.left, id_buku)
        return self._search_rekursif(node_sekarang.right, id_buku)

    def traversal_inorder(self):
        self._counter = 1
        self._rekursif_inorder(self.root)

    def _rekursif_inorder(self, node):
        if node:
            self._rekursif_inorder(node.left)
            print(f"{self._counter}. {node.id_buku} - {node.judul}")
            self._counter += 1
            self._rekursif_inorder(node.right)

    def get_min(self):
        if self.root is None: return None
        curr = self.root
        while curr.left: curr = curr.left
        return curr.id_buku

    def get_max(self):
        if self.root is None: return None
        curr = self.root
        while curr.right: curr = curr.right
        return curr.id_buku

    def height(self):
        return self._rekursif_height(self.root)

    def _rekursif_height(self, node):
        if node is None: return -1
        return 1 + max(self._rekursif_height(node.left), self._rekursif_height(node.right))
    
'''
buku = BinarySearchTree()

buku.insert(50, "Dasar Pemrograman")
buku.insert(30, "Struktut Data")
buku.insert(70, "Kecerdasan Buatan")
buku.insert(20, "Matematika Diskrit")
buku.insert(40, "Basis Data")
buku.insert(60, "Jaringan Komputer")
buku.insert(80, "Sistem Operasi")

buku.traversal_inorder()
hasil_60 = buku.search(60)
if hasil_60:
    print(f"\nBuku dengan id 60 ditemuin dan berjudul: {hasil_60.judul}")
else:
    print("Buku dengan id 60 tidak ada.")

hasil_100 = buku.search(100)
if hasil_100:
    print(f"Buku dengan id 100 ditemuin dan berjudul: {hasil_100.judul}")
else:
    print(f"Buku dengan id 100 tidak ada.") 
    
print(f"\n[STATISTIK] ID Terkecil: {buku.get_min()}")
print(f"[STATISTIK] ID Terbesar: {buku.get_max()}")

print(f"[INFO] Tinggi (Height) Tree: {buku.height()}")
'''

print("SISTEM KATALOG PERPUSTAKAAN \"ILMU TERANG\"")
print("===========================================")

buku = BinarySearchTree()

buku.insert(50, "Dasar Pemrograman")
buku.insert(30, "Struktur Data")
buku.insert(70, "Kecerdasan Buatan")
buku.insert(20, "Matematika Diskrit")
buku.insert(40, "Basis Data")
buku.insert(60, "Jaringan Komputer")
buku.insert(80, "Sistem Operasi")


print("\n[INFO] Koleksi Buku (In-Order Traversal):")
buku.traversal_inorder()

print(f"\n[SEARCH] Mencari ID 60... ", end="")
h60 = buku.search(60)
print(f"Ditemukan! Judul: {h60.judul}" if h60 else "Data tidak ditemukan.")

print(f"[SEARCH] Mencari ID 100... ", end="")
h100 = buku.search(100)
print(f"Ditemukan! Judul: {h100.judul}" if h100 else "Data tidak ditemukan.")

print(f"\n[STATISTIK] ID Terkecil: {buku.get_min()}")
print(f"[STATISTIK] ID Terbesar: {buku.get_max()}")
print(f"[INFO] Tinggi (Height) Tree: {buku.height()}")

print("===========================================")
print("Simulasi Selesai!")