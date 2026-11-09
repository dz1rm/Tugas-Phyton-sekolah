print("===== HASIL NILAI MAHASISWA =====")

nama = input("Nama                    : ")
tugas = float(input("Nilai Tugas      : "))
uts = float(input("Nilai UTS          : "))
uas = float(input("Nilai UAS          : "))

nilai_akhir = (0.30 * tugas) + (0.30 * uts) + (0.40 * uas)

print("\n===== HASIL NILAI MAHASISWA =====")
print("Nama                    :", nama)
print("Nilai Tugas             :", tugas)
print("Nilai UTS               :", uts)
print("Nilai UAS               :", uas)
print("Nilai Akhir             :", nilai_akhir)