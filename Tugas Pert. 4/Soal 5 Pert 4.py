status_member = input("Apakah pelanggan merupakan member (ya/tidak): ")
total_belanja = float(input("Masukkan total belanja pelanggan: Rp"))

if status_member == "ya" and total_belanja >= 1000000:
    diskon = 20
elif status_member == "ya" or total_belanja < 750000:
    diskon = 10
else:
    diskon = 0

Jumlah_diskon = total_belanja * (diskon / 100)
total_bayar = total_belanja - Jumlah_diskon

print("Diskon:", diskon, "%")
print("Jumlah diskon: Rp", int(Jumlah_diskon))
print("Total yang harus dibayar: Rp", int(total_bayar))
