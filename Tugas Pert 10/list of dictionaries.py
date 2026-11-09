#nambahin nama mhs
mhs = [
    {"nama": "Alya", "nilai": 85},
    {"nama": "Fika", "nilai": 90},
    {"nama": "Hanum", "nilai": 88}
]

#nampilin data dan nilai mhs
for data in mhs:
    print("Nama:", data["nama"], " Nilai:", data["nilai"])

#menambahkan nama mhs baru :D
mhs.append({"nama": "Dzikra", "nilai": 92})

#print semuanya yey
print("Jumlah data mahasiswa:", len(mhs))