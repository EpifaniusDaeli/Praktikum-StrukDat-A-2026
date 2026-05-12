class Node:#Node ini kita buat untuk nyimpan data pasien
    def __init__(self, nama, keluhan):#ini kita inisialisasi dulu atributnya yaitu nama dan keluhan
        self.nama = nama
        self.keluhan = keluhan
        self.next = None
        
class QueueLinkedList:# kelas ini dibuat untuk ngatur antrian pasien
    def __init__(self):#ini kita inisialisasi atribut untuk head, tail, size, sama counter buat nomor antriannya
        self.head = None
        self.tail = None
        self._size = 0
        self.counter = 0
        
    def enqueue(self, nama, keluhan):#fungsi ini buat nambah pasien
        new_node = Node(nama, keluhan)
        
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self._size += 1
        self.counter += 1
        return new_node
        
    def dequeue(self):#kalau fungsi ini buat manggil pasien berikutnya
        if self.is_empty():
            return
        
        x = self.head
        self.head = self.head.next
        
        if self.head is None:
            self.tail = None
            
        self._size -= 1
        return x
    
    def peek(self):#fungsi yang ini buat ngeliat pasien berikutnya tanpa hapus datanya 
        if self.is_empty():
            return 
        return self.head
    
    def is_empty(self):#ini buat ngecek data antrian
        return self._size == 0
          
    def size(self):#ini buat mengembalikan data antrian
        return self._size

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0
        
print("")        
print("="*40)
print("Sistem Antrian Poli Umum \nRS Sehat Bersama")
print("="*40)


pasien = QueueLinkedList()

antrian = "YA, antrian masih kosong" if pasien.is_empty() else "TIDAK, antrian masih ada"#langkah pertama mengecek apakah antriannya kosong atau tidak
print(f"\n[CEK] Apakah antrian kosong? -> {antrian}")

pasien1 = pasien.enqueue('Epifanius', 'Demam')#kita menambahkan pasien dengan nama Epifanius dan keluhan demam
print(f"\n[DAFTAR] {pasien1.nama} terdaftar dengan keluhan: {pasien1.keluhan} (No. Antrian: {pasien.counter})")

pasien2 = pasien.enqueue('Gilang', 'Flu batuk')#kita menambahkan pasien lagi dengan nama Gilang dan keluhan flu batuk     
print(f"[DAFTAR] {pasien2.nama} terdaftar dengan keluhan: {pasien2.keluhan} (No. Antrian: {pasien.counter})")

pasien3 = pasien.enqueue('Marni', 'Asma')#kita menambahkan pasien lagi dengan nama Marni dan keluhan asma
print(f"[DAFTAR] {pasien3.nama} terdaftar dengan keluhan: {pasien3.keluhan} (No. Antrian: {pasien.counter})")

jumlah_pasien = pasien.size()#di sini kita mengecek berapa jumlah pasien yang lagi ngantri
print(f"\n[INFO] Jumlah pasien menunggu: {jumlah_pasien}")
    
pasien_selanjutnya = pasien.peek()#di sini kita melihat siapa pasien berikutnya yang akan dilayani
print(f"[PEEK] Pasien Berikutnya : {pasien_selanjutnya.nama}-{pasien_selanjutnya.keluhan}")

panggil = pasien.dequeue()#di sini kita memanggil pasien dan menghapusnya dari antrian
print(f"\n[PANGGIL] Dokter memanggil: {panggil.nama} (keluhan: {panggil.keluhan})")

pasien4 = pasien.enqueue('Dewi', 'Sakit kepala')#kita menambah pasien lagi dengan nama dewi dan keluhan sakit kepala
print(f"[DAFTAR] {pasien4.nama} terdaftar dengan keluhan: {pasien4.keluhan} (No. Antrian: {pasien.counter})")

print("\n[ANTRIAN SAAT INI]")#di sini kita nampilin pasien yang masih mengantri dalam bentuk urutan
current = pasien.head
no = 1
while current is not None:
    print(f" {no}. {current.nama} \t -> {current.keluhan}")
    current = current.next
    no += 1
    
panggil = pasien.dequeue()#kita memanggil lagi pasien dan kita hapus datanya dari antrian
print(f"\n[PANGGIL] Dokter memanggil: {panggil.nama} (keluhan: {panggil.keluhan})")
jumlah_pasien = pasien.size()#di sini kita melihat berapa pasien yang lagi mengantri
print(f"[INFO] Jumlah pasien menunggu: {jumlah_pasien}")

pasien.clear()#di sini kita menghapus semua data pasien di antrian
print(f"\n[CLEAR] Sesi poli klinik selesai. Antrian dikosongkan.")

antrian = "YA, antrian sudah kosong" if pasien.is_empty() else "TIDAK, antrian masih ada"# di sini kita mengecek apakah antrian sudah kosong atau belum
print(f"[CEK] Apakah antrian kosong? -> {antrian}")

print("")
print("="*40)
print("Simulasi Selesai!")
print("="*40)



        
    
    
        
        
        
        
    
    