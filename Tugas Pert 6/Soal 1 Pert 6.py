jumlah_jenis = int(input("Masukkan jumlah jenis barang (1-20): "))

while jumlah_jenis < 1 or jumlah_jenis > 20:
    print("Jumlah barang harus antara 1-20!")
    jumlah_jenis = int(input("Masukkan jumlah jenis barang: "))

total_belanja = 0
total_diskon = 0
jumlah_barang = 0

for i in range(1, jumlah_jenis + 1):
    print("\nBarang ke-", i)

    nama = input("Masukkan nama barang (STOP untuk selesai): ")

    if nama.upper() == "STOP":
        print("Input barang dihentikan.")
        break

    harga = int(input("Masukkan harga satuan: "))

    while harga < 1000:
        print("Harga minimal Rp1.000!")
        harga = int(input("Masukkan harga satuan: "))

    jumlah = int(input("Masukkan jumlah barang (1-100): "))

    while jumlah < 1 or jumlah > 100:
        print("Jumlah harus antara 1-100!")
        jumlah = int(input("Masukkan jumlah barang: "))

    subtotal = harga * jumlah

    if subtotal > 500000:
        diskon = subtotal * 0.10
        print("Barang mendapat diskon 10%.")
    else:
        diskon = 0

    if jumlah > 10:
        print("Pembelian grosir")

    total_belanja += subtotal
    total_diskon += diskon
    jumlah_barang += 1

    print("Nama barang:", nama)
    print("Subtotal: Rp", subtotal)
    print("Diskon: Rp", diskon)
    print("Total setelah diskon: Rp", subtotal - diskon)

print("\n=== STRUK PEMBELIAN ===")
print("Jumlah jenis barang:", jumlah_barang)
print("Total belanja sebelum diskon: Rp", total_belanja)
print("Total diskon: Rp", total_diskon)
print("Total pembayaran: Rp", total_belanja - total_diskon)
print("Terima kasih!")
