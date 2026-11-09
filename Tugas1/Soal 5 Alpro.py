print("===== BIAYA PERJALANAN =====")

jarak = float(input("Jarak                      : "))
konsumsi = float(input("Konsumsi kendaraan      : "))
harga_bbm = float(input("Harga BBM              : Rp"))
parkir = float(input("Parkir                    : Rp"))
biaya_lainnya = float(input("Biaya lainnya      : Rp"))

kebutuhan_bbm = jarak / konsumsi
biaya_bbm = kebutuhan_bbm * harga_bbm

total_biaya = biaya_bbm + parkir + biaya_lainnya

print("\n===== BIAYA PERJALANAN =====")
print("Jarak                    :", jarak, "km")
print("Konsumsi kendaraan       :", konsumsi, "km/liter")
print("Kebutuhan BBM            :", kebutuhan_bbm, "liter")
print("Biaya BBM                : Rp", biaya_bbm)
print("Biaya Parkir             : Rp", parkir)
print("Biaya Lainnya            : Rp", biaya_lainnya)
print("Total Biaya              : Rp", total_biaya)

