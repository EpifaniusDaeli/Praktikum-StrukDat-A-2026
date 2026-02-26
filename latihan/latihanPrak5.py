# 1 :Data
stok_barang =[15, 40, 30, 10, 25]

#a
print(stok_barang)
stok_barang[3] = 50
print(stok_barang)

#b
stok_barang.append(5)
stok_barang.sort(reverse = True)
print(stok_barang)

#c
hasil = sum(stok_barang)
print(hasil)

#d
rata = hasil / len(stok_barang)
variable = "stok aman" if rata > 20 else "waspada"
print(variable)
    

#2
data_aktivitas = [("Diki",88), ("Aqul", 45), ("Abid", 92), ("Rehan", 70)]
for x in data_aktivitas:
 a, b = x
for x in data_aktivitas:
    if b > 80:
        print(f'{a}, mendapatkan predikat gold')
    elif b > 50 or  b<80:
        print(f'{a}', "mendapatakan predikat silver")
    else:
        print(f'{a}, mendaptakan predikat bronze')

#3
ukm_coding = {"Andi", "Budi", "Caca", "Deni"}
ukm_robotik = {"Caca", "Deni", "Euis", "Fafa"}
#a
print("Mahasiswa yang hanya mendaftar di umkm_coding:", ukm_coding-ukm_robotik)
#b
print("mahasiswa unik yang mendaftar di salah satu atau kedua UKM tersebut:",  ukm_coding | ukm_robotik)
#c
print("Apakah andi merupakan anggota ukm_robotik:", "andi" in ukm_robotik)

#4
gudang_pc = [
{"item": "Monitor", "harga": 1500000, "stok": 5},
{"item": "Keyboard", "harga": 400000, "stok": 12},
{"item": "Mouse", "harga": 250000, "stok": 20}
]

for x in gudang_pc:
    for a, b in x.items():
        if b == "keyboard":
            x["kategori"] = "Aksesoris"
            break
        
gudang_pc.append({"item": "Headset", "harga":35000, "stok":8})

for x in gudang_pc:
    print(f"item{x ["item"] }| Total_aset : Rp {x["harga"]*x["stok"]}")
   


  

























