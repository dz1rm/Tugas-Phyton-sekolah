print("===== SLIP GAJI =====")

nama = input("Nama                    : ")
gaji_pokok = int(input("Gaji Pokok              : Rp"))
tunjangan = int(input("Tunjangan               : Rp"))
potongan = int(input("Potongan                : Rp"))

gaji_bersih = gaji_pokok + tunjangan - potongan

print("\n===== SLIP GAJI =====")
print("Nama                    :", nama)
print("Gaji Pokok              : Rp", gaji_pokok)
print("Tunjangan               : Rp", tunjangan)
print("Potongan                : Rp", potongan)
print("Gaji Bersih             : Rp", gaji_bersih)