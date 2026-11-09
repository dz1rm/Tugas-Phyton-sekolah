jumlah_transaksi = int(input("Masukkan jumlah transaksi: "))

total_penjualan = 0
jumlah_minimal_100000 = 0
penjualan_tertinggi = 0
transaksi_tertinggi = 0

for i in range(jumlah_transaksi):
    penjualan = int(input(f"Penjualan transaksi ke-{i + 1}: "))

    total_penjualan += penjualan

    if penjualan >= 100000:
        jumlah_minimal_100000 += 1

    if penjualan > penjualan_tertinggi:
        penjualan_tertinggi = penjualan
        transaksi_tertinggi = i + 1

rata_rata = total_penjualan / jumlah_transaksi

print("Total penjualan = Rp", total_penjualan)
print("Jumlah transaksi >= Rp100.000 =", jumlah_minimal_100000)
print("Rata-rata penjualan = Rp", rata_rata)
print("Penjualan tertinggi = Rp", penjualan_tertinggi)
print("Transaksi tertinggi = transaksi ke-", transaksi_tertinggi)