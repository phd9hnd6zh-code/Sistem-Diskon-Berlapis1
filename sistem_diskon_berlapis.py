# Program: Sistem Diskon Berlapis
# Nama: Berliani Reshalia
# NIM: 2410017514002
# Kelas: TRKJ 24

# Input total belanja dan status member
total_belanja = float(input("Masukkan total belanja (Rp): "))
status_member = input("Apakah Anda member? (Ya/Tidak): ")

# Inisialisasi variabel diskon
diskon = 0

# Logika dengan nested if
if status_member.lower() == "ya":  # jika pelanggan adalah member
    if total_belanja > 1000000:
        diskon = 0.15  # diskon 15%
    elif total_belanja > 500000:
        diskon = 0.10  # diskon 10%
    else:
        diskon = 0     # tidak ada diskon
else:  # jika bukan member
    if total_belanja > 500000:
        diskon = 0.05  # diskon 5%
    else:
        diskon = 0     # tidak ada diskon

# Hitung total setelah diskon
potongan = total_belanja * diskon
total_bayar = total_belanja - potongan

# Tampilkan hasil
print("\n===== STRUK PEMBAYARAN =====")
print(f"Status Member     : {status_member}")
print(f"Total Belanja     : Rp{total_belanja:,.0f}")
print(f"Diskon            : {diskon * 100:.0f}%")
print(f"Potongan Harga    : Rp{potongan:,.0f}")
print(f"Total yang Dibayar: Rp{total_bayar:,.0f}")
print("=============================")
