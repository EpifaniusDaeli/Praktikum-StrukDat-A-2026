class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[]for _ in range(self.size)]
        
    def hash_function(self, kode):
        total = 0
        for char in str(kode):
            total += ord(char)
        return total % self.size
    
    def insert(self, kode, judul):
        index = self.hash_function(kode)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == kode:
                bucket[i] = (kode, judul)
                print(f"Buku dengan kode '{kode}' berhasil di update")
                return
            
        bucket.append((kode, judul))
        print(f"Buku '{kode} : {judul}' berhasil ditambahkan")
    
    def get(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]
        for k, v in bucket:
            if k == kode:
                return v
            
        return "Buku tidak ditemukan"
    
    def delete(self, kode):
        index = self.hash_function(kode)
        bucket = self.table[index]
        for i, (k, v) in enumerate(bucket):
            if k == kode:
                del bucket[i]
                print(f"Buku dengan kode '{kode}' berhasil dihapus")
                return True
        
        print(f"kode '{kode}' tidak ditemukan")
        return False
    
    def display(self):
        print("===== DATA BUKU ====")
        for index, bucket in enumerate(self.table):
            print(f"Index {index} : {bucket}")
        print("===========================")
        
#main program
print("="*45)
print("SISTEM PENYIMPANAN DATA BUKU PERPUSTAKAAN")
print("="*45)

buku = HashTable()
print()
buku.insert("BKK111", "Mahir C++ Dalam Satu Jam")
buku.insert("BK222", "Python Dasar")
buku.insert("BK333", "Matematika Diskrit")
buku.insert("BK444", "Atomic Habits")
buku.insert("BK555", "Cara Kaya Dalam Satu Malam")
buku.insert("BK666", "Integral Dasar")
print("-"*40)
        
print("Daftar buku sekarang:")
buku.display()
print("-"*40)

buku.insert("BK045", "Mein Kampf")
buku.insert("BK111", "Bumi Manusia")

print("[Mencari buku]....")
print(buku.get("BK666"))
print("[Mencari buku]....")
print(buku.get("BK999"))
print("Data buku terbaru:")
buku.display()
print("-"*40)

print("[MENGHAPUS BUKU]....")
buku.delete("BK111")

print("Data buku terbaru:")
buku.display()
print("-"*40)




