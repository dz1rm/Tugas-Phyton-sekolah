print("===== NOTA BELANJA =====")

barang1 = input("Nama barang 1 : ")
harga1 = int(input("Harga barang 1 : Rp"))
jumlah1 =int(input("Jumlah barang 1 : "))

barang2 = input("Nama barang 2 : ")
harga2 = int(input("Harga barang 2 : Rp"))
jumlah2 = int(input("Jumlah barang 2 : "))

total1 = harga1 * jumlah1
total2 = harga2 * jumlah2

total_belanja = total1 + total2 

print("\n===== NOTA BELANJA =====")
print("Barang 1     :", barang1)
print("Harga        : Rp", harga1)
print("Jumlah       :", jumlah1)
print("Total        : Rp", total1)

print ()

print("Barang 2     :", barang2)
print("Harga        : Rp", harga2)
print("Jumlah       :", jumlah2)
print("Total        : Rp", total2)

print()

print("Total Belanja : Rp", total_belanja)