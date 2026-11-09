hari = 1
total_air = 0
jumlah_diatas_100 = 0

while hari <= 10:
    penggunaan = int(input(f"Penggunaan air hari ke-{hari}: "))

    total_air += penggunaan

    if penggunaan > 100:
        jumlah_diatas_100 += 1

    hari += 1

print("Total penggunaan air =", total_air, "liter")
print("Jumlah hari lebih dari 100 liter =", jumlah_diatas_100)