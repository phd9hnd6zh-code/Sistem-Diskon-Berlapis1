# Sistem-Diskon-Berlapis1
## Identitas
- Nama: [berliani reshalia]
- NIM: [2410017514002]
- Kelas: [A1]
## Studi Kasus
[Program ini merupakan simulasi sistem diskon toko dengan struktur kontrol percabangan bersarang (nested if).
Program akan meminta pengguna untuk memasukkan total belanja dan status member (Ya/Tidak).
Berdasarkan status dan jumlah total belanja, program akan menentukan diskon yang diperoleh dan menampilkan total pembayaran akhir.
Ketentuan Diskon:
Non-member
Belanja > Rp500.000 → Diskon 5%
Member
Belanja > Rp500.000 → Diskon 10%
Belanja > Rp1.000.000 → Diskon 15%]
## Fitur Program
- [Input total belanja dari pengguna]

- [Input status member (Ya/Tidak) ]

- [Logika nested if untuk menentukan besaran diskon]

- [Perhitungan total potongan harga dan total bayar]

- [Output hasil dalam format rapi seperti struk pembayaran]
## Teknik yang Digunakan
-  []Input

 - []While Loop

 - []Do-While Pattern

- []For Loop

- []Nesting If
## Screenshot Output
[<img width="648" height="322" alt="tugas" src="https://github.com/user-attachments/assets/e5c138e0-e318-4b65-a906-6b8e43220dd4" />]

## Cara Menjalankan
1. Download file [sistem_diskon_berlapis.py](https://github.com/user-attachments/files/23439050/sistem_diskon_berlapis.py)
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

2. Buka terminal atau command prompt
3. Jalankan perintah berikut: python sistem_diskon_berlapis.py
4. Masukkan total belanja dan status member sesuai instruksi di layar
