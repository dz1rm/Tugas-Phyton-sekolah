#ini dictionary
buku = {
    "judul": "Pulang",
    "penulis": "Leila S. Chudori",
    "tahun": "2012"
}

#nampilin judul buku
print("Judul buku:", buku["judul"])

#nambahin key stock
buku["stok"] = 10
#ubah dr 10 ke 8
buku["stok"] = 8

#nampilin key dan value
print("\nData Buku:")
for key, value in buku.items():
    print(key, ":", value)
    