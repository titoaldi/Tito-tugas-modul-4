def jumlah_hari(bulan, tahun):
    hari_per_bulan = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0):
        hari_per_bulan[1] = 29
    return hari_per_bulan[bulan - 1]

bulan = 0
tahun = 0

while bulan < 1 or bulan > 12:
    try:
        bulan = int(input("Masukkan bulan: "))
    except ValueError:
        print("Error.")

while tahun <= 0:
    try:
        tahun = int(input("Masukkan tahun: "))
    except ValueError:
        print("Error.")

jumlah = jumlah_hari(bulan, tahun)

print(f"ada {jumlah} hari.")