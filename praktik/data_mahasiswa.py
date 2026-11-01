def cari_mahasiswa(data, nim):
    """Mencari data mahasiswa berdasarkan NIM dengan aman menggunakan get()."""
    return data.get(nim)

def rata_rata_nilai(data):
    """Menghitung rata-rata nilai dari seluruh mahasiswa dalam dictionary."""
    if len(data) == 0:
        return 0.0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)

# Inisialisasi Dictionary Data Mahasiswa Awal
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "3F", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "3F", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "3F", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "3F", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "3F", "nilai": 88}
}

if __name__ == "__main__":
    print("=== SISTEM DATA MAHASISWA INTERAKTIF ===\n")

    # 1. Test Case: Pencarian Tersedia (Otomatis & Interaktif)
    print("--- 1. Pengujian Pencarian Tersedia ---")
    cari_nim = input("Masukkan NIM yang ingin dicari (Contoh: A003): ").strip().upper()
    hasil_cari = cari_mahasiswa(data_mahasiswa, cari_nim)
    
    if hasil_cari is not None:
        print(f"Hasil: Data {cari_nim} ditemukan -> {hasil_cari}")
    else:
        print("Data tidak ditemukan")

    # 2. Test Case: Pencarian Tidak Tersedia (Contoh A999)
    print("\n--- 2. Pengujian Pencarian Tidak Tersedia ---")
    cari_invalid = input("Masukkan NIM fiktif untuk uji error (Contoh: A999): ").strip().upper()
    hasil_invalid = cari_mahasiswa(data_mahasiswa, cari_invalid)
    
    if hasil_invalid is not None:
        print(f"Hasil: {hasil_invalid}")
    else:
        print("Data tidak ditemukan")

    # 3. Test Case: Penambahan Data Baru Secara Interaktif
    print("\n--- 3. Penambahan Data Mahasiswa Baru ---")
    print("Silakan masukkan data untuk mahasiswa baru:")
    nim_baru = input("Masukkan NIM baru (Contoh: A006): ").strip().upper()
    nama_baru = input("Masukkan Nama: ").strip()
    kelas_baru = input("Masukkan Kelas: ").strip()
    
    # Validasi input angka untuk nilai
    try:
        nilai_baru = int(input("Masukkan Nilai (angka): "))
    except ValueError:
        nilai_baru = 0
        print("Input nilai tidak valid, diset ke 0.")

    data_mahasiswa[nim_baru] = {
        "nama": nama_baru,
        "kelas": kelas_baru,
        "nilai": nilai_baru
    }
    print(f"Status: Key {nim_baru} tersedia setelah ditambahkan: {nim_baru in data_mahasiswa}")

    # 4. Test Case: Pembaruan Nilai (Contoh: A002)
    print("\n--- 4. Pembaruan Nilai Mahasiswa (A002) ---")
    if "A002" in data_mahasiswa:
        print(f"Nilai A002 saat ini: {data_mahasiswa['A002']['nilai']}")
        try:
            update_nilai = int(input("Masukkan nilai baru untuk A002 (Contoh: 82): "))
            data_mahasiswa["A002"]["nilai"] = update_nilai
            print(f"Nilai A002 berhasil diubah menjadi: {data_mahasiswa['A002']['nilai']}")
        except ValueError:
            print("Input nilai tidak valid, pembaruan dibatalkan.")

    # 5. Test Case: Rekap Seluruh Data Menggunakan items()
    print("\n--- 5. Rekap Seluruh Data Mahasiswa (items()) ---")
    for nim, info in data_mahasiswa.items():
        print(f"NIM: {nim} | Nama: {info['nama']} | Kelas: {info['kelas']} | Nilai: {info['nilai']}")

    # Perhitungan Rata-rata Kelas
    rata_rata = rata_rata_nilai(data_mahasiswa)
    print(f"\nRata-rata nilai seluruh mahasiswa: {rata_rata:.2f}")