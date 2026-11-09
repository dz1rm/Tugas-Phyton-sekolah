username_benar = "admin"
password_benar = "sistem123"
status_akun = "Aktif"

username = input("Masukkan username: ")
password = input("Masukkan password: ")

if username == username_benar:
    if password == password_benar:
        if status_akun == "Aktif":
            print("Login berhasil!")
        else:
            print("Akun tidak aktif")
    else:
        print("Password salah")
else:
    print("Username salah")
