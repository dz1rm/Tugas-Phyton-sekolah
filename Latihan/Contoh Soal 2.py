nama =  input("Nama: ")
ipk = float(input("IPK: "))
kehadiran = float(input("Kehadiran (%): "))
penghasilan = float(input("Penghasilan orang tua: "))

if ipk >= 3.25 and kehadiran >= 80:
    if penghasilan <= 4000000:
        print("memenuhi beasiswa")
    else:
        print("tidak memenuhi beasiswa, abkibat penghasilan terlalu tinggi")

else:
    if ipk < 3.25:
        print("tidak memenuhi beasiswa, abkibat ipk terlalu rendah")

        if kehadiran < 80:
            print("tidak memenuhi beasiswa, abkibat kehadiran terlalu rendah")