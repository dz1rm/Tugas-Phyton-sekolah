jumlah_barang = int(input("Masukkan jumlah barang: "))

total_belanja = 0
jumlah_diatas_50000 = 0

for i in range(jumlah_barang):
    harga = int(input(f"Harga barang ke-{i + 1}: "))

    total_belanja += harga

    if harga > 50000:
        jumlah_diatas_50000 += 1

print("Total belanja =", total_belanja)
print("Jumlah barang di atas Rp50.000 =", jumlah_diatas_50000)