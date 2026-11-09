nama = input("Masukkan nama mahasiswa: ") 
nilai = float(input("Masukkan nilai akhir: "))
kehadiran = float(input("Masukkan kehadiran (%): "))

if nilai >= 85:
    grade = "A"
elif nilai >= 75:
    grade = "B"
elif nilai >= 65:
    grade = "C"
elif nilai >= 50:
    grade = "D"
else:
    grade = "E"

print("Grade:", grade)

if nilai >= 65 and kehadiran >= 75:
    print("Lulus")
else:
    if nilai < 65:
        print("Tidak lulus karena nilai terlalu rendah")

    if kehadiran < 75:
        print("Tidak lulus karena kehadiran tidak mencukupi")

