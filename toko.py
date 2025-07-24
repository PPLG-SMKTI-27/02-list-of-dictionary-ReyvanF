items = [
    {"Nama" : "Laptop", "Stok" : 10, "Harga" : 1000.89},
    {"Nama" : "Handphone", "Stok" : 3, "Harga" : 100.99},
    {"Nama" : "Mouse", "Stok" : 6, "Harga" : 10.19},
    {"Nama" : "Keyboard", "Stok" : 7, "Harga" : 20.5},
    {"Nama" : "Headphone", "Stok" : 2, "Harga" : 15.99}
]

angka = 1
for i in items:
    print(f"{angka}.\tNama : {i['Nama']}\n\tStok : {i['Stok']}\n\tHarga : {i['Harga']}$\n\n")
    angka = angka + 1
angka = 1

def create():
    nama = str(input("Masukkan nama barang : "))
    stok = int(input("Masukkan jumlah barang : "))
    harga = float(input("Masukkan harga barang (Dollar) : "))
    newitem = {"Nama" : nama, "Stok" : stok, "Harga" : harga}
    items.append(newitem)

create()

for i in items:
    print(f"{angka}.\tNama : {i['Nama']}\n\tStok : {i['Stok']}\n\tHarga : {i['Harga']}$\n\n")
    angka = angka + 1