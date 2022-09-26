x = 15000
y = 22500

jamkerja = int(input("masukkan jam kerja :"))

if jamkerja > 40:
    gaji = (40*x) + ((jamkerja-40) * y)
    print("Total gaji :", gaji)
    pengeluaran = int(input("masukkan pengeluaran :"))
    if gaji > pengeluaran:
        print("Bisa Menabung")
    elif gaji == pengeluaran:
        print("Tidak Bisa Menabung")
    elif gaji < pengeluaran:
        print("Cari Tambahan")
    else:
        print("Input Salah")
else:
    gaji = 40*x
    print("Total gaji :", gaji)
    pengeluaran = int(input("masukkan pengeluaran :"))
    if gaji > pengeluaran:
        print("Bisa Menabung")
    elif gaji == pengeluaran:
        print("Tidak Bisa Menabung")
    elif gaji < pengeluaran:
        print("Cari Tambahan")
    else:
        print("Input Salah")