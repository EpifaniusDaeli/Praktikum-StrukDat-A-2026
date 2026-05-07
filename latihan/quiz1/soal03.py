#Data
katalog = [
 {'nama': 'Belajar Python', 'harga': 75000, 'stok': 5},
 {'nama': 'Struktur Data', 'harga': 95000, 'stok': 3},
 {'nama': 'Algoritma Dasar', 'harga': 60000, 'stok': 8},
]

#prosedur
def proses_transaksi(katalog, nama_buku, jumlah_beli):
    a = []
    for item, info in katalog.items():
        for key, value in info:
            if  jumlah_beli<= key in info:
                a = katalog[key] = [value]-jumlah_beli
            elif jumlah_beli > key:
                print("Stok tidak mencukupi")
            elif key not in katalog:
                print("Buku Tidak Ditemukan")
                

#Program Utama
beli = proses_transaksi()
riwayat_transaksi = ()
print(riwayat_transaksi)


             
                
    