# Pertemuan 11 - Dictionary/Map
Nama: Rian Subekti  
NIM: 2225250096  
Kelas: 3F  

## Tujuan
Memodelkan data pendidikan menggunakan dictionary dan pasangan key-value.

## Struktur Data
Menggunakan NIM (contoh: "A001", "A002", dst.) sebagai key utama. Value dari setiap key utama berupa dictionary bersarang yang memuat atribut:
- `nama` (string)
- `kelas` (string)
- `nilai` (integer)

## Cara Menjalankan
python3 praktik/data_mahasiswa.py

## Test Case
| Input/Aksi | Hasil yang Diharapkan | Hasil Aktual | Status |
| :--- | :--- | :--- | :--- |
| **A003** (Pencarian tersedia) | Data Citra ditampilkan | Data Citra ditampilkan dengan benar | Lulus |
| **A999** (Pencarian tidak tersedia) | Pesan 'Data tidak ditemukan' | Pesan 'Data tidak ditemukan' tampil dengan aman | Lulus |
| **A002** diubah nilainya menjadi `82` | Nilai A002 berubah menjadi 82 | Nilai A002 berhasil diperbarui menjadi 82 | Lulus |
| **A006** (Penambahan data) | Key A006 tersedia setelah ditambahkan | Key A006 berhasil dimasukkan ke dalam dictionary | Lulus |
| `items()` (Rekap) | Semua NIM dan data tampil | Seluruh data mahasiswa dan rata-rata tampil | Lulus |

## Refleksi
Kesalahan akses key yang sempat ditemukan adalah terjadinya `SyntaxError` akibat penulisan variabel penampung input yang mengandung spasi (`hasil_ cari`). Hal ini diperbaiki dengan menghapus spasi menjadi `hasil_cari` agar sesuai dengan kaidah penulisan sintaks Python. Selain itu, penggunaan method `.get()` sangat membantu untuk menghindari error `KeyError` apabila key yang dicari tidak tersedia di dalam dictionary.

## Sumber
Bahan_Ajar_Pertemuan_11_Dictionary_Map_VSCode_GitHub (1)