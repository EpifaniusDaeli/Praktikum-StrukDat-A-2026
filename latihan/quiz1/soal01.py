

#Fungsi tambah buku toko
def  tambahBuku(nama, harga, stok):
    nama = {}
    x = nama[harga]=stok
    return x

# Program Utama dan Kode meminta input
for i in range(3):
    PyBookStore = {}
    c = 1
    print(f"\n===Buku ke-{c}===")
    nama = (input("Masukkan nama buku: "))    
    while True:
        harga = int(input("Masukkan harga buku: "))
        if harga <= 0:
            print("harga harus lebih besar dari 0 ")
            continue
        break        
    while True:    
        stok = int(input("Masukkan stok buku:"))
        if stok < 0:
            print("stok tidak boleh bernilai negatif")
            continue
        break
    c += 1
    PyBookStore = tambahBuku(nama, harga, stok)
   
    
print(list(PyBookStore))


 
    