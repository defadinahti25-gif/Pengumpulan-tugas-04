def main():
    print("="*45)
    print(" PROGRAM PENYELESAIAN OPERATOR PYTHON ".center(45))
    print("="*45)

    # 1. OPERATOR ARITMATIKA
    print("\n[1] Operator Aritmatika")
    apel, teman = 12, 4
    print(f">> Apel yang diterima setiap teman: {apel // teman} buah")
    print(f">> Total apel setelah ditambah 8  : {apel + 8} buah")


    # 2. OPERATOR PERBANDINGAN
    print("\n[2] Operator Perbandingan")
    tinggi_siti, tinggi_andi = 160, 165
    print(f">> Apakah Andi lebih tinggi dari Siti? {tinggi_andi > tinggi_siti}")


    # 3. OPERATOR LOGIKA
    print("\n[3] Operator Logika")
    cuaca_cerah, pr_selesai = True, True
    print(f">> Budi bisa bermain di luar? {cuaca_cerah and pr_selesai}")


    # 4. OPERATOR BITWISE
    print("\n[4] Operator Bitwise")
    a, b = 6, 3
    # :04b untuk memformat hasil langsung menjadi biner 4-bit
    print(f">> AND (6 & 3): {a & b} (Biner: {a & b:04b})")
    print(f">> OR  (6 | 3): {a | b} (Biner: {a | b:04b})")
    print(f">> XOR (6 ^ 3): {a ^ b} (Biner: {a ^ b:04b})")


    # 5. OPERATOR PENUGASAN
    print("\n[5] Operator Penugasan")
    saldo = 50_000  # Menggunakan underscore agar mudah dibaca
    saldo += 20_000
    saldo -= 30_000

    print(f">> Sisa saldo pulsa: Rp{saldo:,}".replace(',', '.'))


    # 6. OPERATOR KEANGGOTAAN
    print("\n[6] Operator Keanggotaan")
    peserta = ["Andi", "Budi", "Citra", "Dewi"]
    kalimat = "Saya suka belajar Python"
    print(f">> 'Eka' terdaftar sebagai peserta? {'Eka' in peserta}")
    print(f">> Kata 'Python' ada dalam kalimat? {'Python' in kalimat}")


    # 7. OPERATOR IDENTITAS
    print("\n[7] Operator Identitas")
    x = y = 100
    list1, list2 = [1, 2, 3], [1, 2, 3]

    print(f">> x dan y merujuk ke memori yang sama? {x is y}")
    print(f">> list1 dan list2 merujuk ke memori yang sama? {list1 is list2}")


    # 8. OPERATOR TERNARY
    print("\n[8] Operator Ternary")
    angka, nilai_ujian = 150, 85

    cek_angka = "Lebih besar dari 100" if angka > 100 else "Tidak lebih besar"
    cek_lulus = "Lulus" if nilai_ujian > 70 else "Tidak Lulus"
    
    print(f">> Cek angka {angka}: {cek_angka}")
    print(f">> Status nilai {nilai_ujian}: {cek_lulus}")
    print("\n" + "="*45)



if __name__ == "__main__":
    main()