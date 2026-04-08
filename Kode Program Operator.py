# 1. Operator Aritmatika
print("1. Operator Aritmatika ")
apel_awal = 12
teman = 4

# pembagian bulat
apel_per_teman = apel_awal // teman 
print("Setiap teman menerima:", apel_per_teman, "apel")

# Budi dapat 8 apel
tambahan_apel = 8
total_apel = apel_awal + tambahan_apel
print("Total apel Budi sekarang:", total_apel, "apel\n")



# 2. Operator Perbandingan
print("2. Operator Perbandingan ")
tinggi_siti = 160
tinggi_andi = 165

if tinggi_andi > tinggi_siti:
    print("Andi lebih tinggi dari Siti.\n")
elif tinggi_siti > tinggi_andi:
    print("Siti lebih tinggi dari Andi.\n")
else:
    print("Tinggi mereka sama.\n")



# 3. Operator Logika
print("3. Operator Logika ")
cuaca_cerah = True
pr_selesai = True

bisa_bermain = cuaca_cerah and pr_selesai 
print("Apakah Budi bisa bermain di luar?", bisa_bermain, "\n")



# 4. Operator Bitwise
print("4. Operator Bitwise ")
angka1 = 6 
angka2 = 3 

print("6 AND 3 (6 & 3) =", angka1 & angka2) 
print("6 OR 3 (6 | 3)  =", angka1 | angka2) 
print("6 XOR 3 (6 ^ 3) =", angka1 ^ angka2, "\n") 



# 5. Operator Penugasan
print("5. Operator Penugasan ")
saldo = 50000
saldo += 20000 
saldo -= 30000 
print("Sisa saldo pulsa siswa adalah: Rp", saldo, "\n")



# 6. Operator Keanggotaan
print("6. Operator Keanggotaan ")
peserta = ["Andi", "Budi", "Citra", "Dewi"]
cek_eka = "Eka" in peserta
print("Apakah Eka terdaftar sebagai peserta?", cek_eka)

kalimat = "Saya suka belajar Python"
cek_python = "Python" in kalimat
print("Apakah kata 'Python' ada dalam kalimat?", cek_python, "\n")



# 7. Operator Identitas
print("7. Operator Identitas ")
x = 10
y = 10
print("Apakah x dan y merujuk ke objek yang sama?", x is y)

list_a = [1, 2, 3]
list_b = [1, 2, 3]
print("Apakah list_a dan list_b merujuk ke objek yang sama?", list_a is list_b, "\n")



# 8. Operator Ternary
print("8. Operator Ternary ")
angka_tes = 120
cek_angka = "Lebih besar dari 100" if angka_tes > 100 else "Tidak lebih besar dari 100"
print(f"Angka {angka_tes}: {cek_angka}")

nilai_ujian = 85
status_kelulusan = "Lulus" if nilai_ujian > 70 else "Tidak Lulus"
print(f"Nilai ujian {nilai_ujian}: {status_kelulusan}")