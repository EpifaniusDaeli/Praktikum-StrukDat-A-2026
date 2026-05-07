#Data
BukuTI = [
 {'Buku01': 'Belajar Python', 'harga': 75000, 'stok': 5},
 {'Buku02': 'Struktur Data', 'harga': 95000, 'stok': 3},
 {'Buku03': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

#Fungsi 
def cari_buku(nama, key):
    x = '1'
    cari = []
    for item, info in BukuTI.items():
        for key, value in info:
            if x == key:
                cari += (f'{key}:{value}')
            else:
                cari = "Buku Tidak Ditemukan"
    return cari

#Program Utama
keyword = int(input("Masukkan keyword"))
Buku_Tujuan = cari_buku(BukuTI, keyword)
print(Buku_Tujuan)




        
            
        
    

