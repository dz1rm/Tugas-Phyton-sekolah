nama = input("Masukkan nama mahasiswa                       : ")
ipk = float(input("Masukkan IPK                             : "))
kehadiran = float(input("Masukkan kehadiran (%)             : "))
penghasilan = float(input("Masukkan penghasilan orang tua   : "))

if ipk >= 3.5 and kehadiran >= 80:
    if penghasilan <= 4000000:
        print("Lolos beasiswa")
    else:
        print("Tidak lolos beasiswa, akibat penghasilan orang tua terlalu tinggi")

else: 
    if ipk < 3.5:
        print("Tidak lolos beasiswa, akibat IPK kurang dari 3.5")
        
    if kehadiran < 80:
        print("Tidak lolos beasiswa, akibat kehadiran kurang dari 80%")
