from datetime import date

from models.pengguna import Pengguna
from models.peminjaman import Peminjaman


class Anggota(Pengguna):
    """Pengguna yang meminjam dan mengembalikan buku."""

    BATAS_PINJAM = 3

    def __init__(self, id_pengguna, nama, no_telepon):
        super().__init__(id_pengguna, nama, no_telepon) 
        self.__jumlah_pinjam = 0                        

    def get_jumlah_pinjam(self):
        return self.__jumlah_pinjam

    def ubah_jumlah_pinjam(self, selisih):
        """Tambah/kurangi jumlah buku yang sedang dipinjam (mis. +1 / -1)."""
        baru = self.__jumlah_pinjam + selisih
        if baru < 0:
            raise ValueError("Jumlah pinjam tidak boleh kurang dari 0")
        if baru > self.BATAS_PINJAM:
            raise ValueError(f"Jumlah pinjam melebihi batas ({self.BATAS_PINJAM})")
        self.__jumlah_pinjam = baru

    def bisa_meminjam(self):
        """True jika jumlah_pinjam masih di bawah BATAS_PINJAM."""
        return self.__jumlah_pinjam < self.BATAS_PINJAM

    def lihat_daftar_buku(self, daftar_buku):
        if not daftar_buku:
            print("Belum ada buku.")
            return
        for buku in daftar_buku:
            buku.tampilkan_info()

    def cari_buku(self, daftar_buku, kata_kunci):
        """Cari buku berdasarkan kata kunci pada judul atau penulis."""
        kunci = kata_kunci.strip().lower()
        return [
            b for b in daftar_buku
            if kunci in b.get_judul().lower() or kunci in b.get_penulis().lower()
        ]

    def pinjam_buku(self, buku, id_peminjaman):
        """Validasi batas pinjam & stok, lalu buat dan proses Peminjaman."""
        if not self.bisa_meminjam():
            raise ValueError(
                f"{self.get_nama()} sudah mencapai batas pinjam ({self.BATAS_PINJAM} buku)"
            )
        if not buku.tersedia():
            raise ValueError(f"Stok buku '{buku.get_judul()}' habis")

        peminjaman = Peminjaman(id_peminjaman, self, buku, date.today())
        peminjaman.proses_pinjam()          
        self.ubah_jumlah_pinjam(1)
        return peminjaman

    def kembalikan_buku(self, peminjaman, tanggal_kembali=None):
        """Proses pengembalian; mengembalikan nilai denda (int, rupiah).

        tanggal_kembali opsional (default hari ini) agar mudah diuji.
        """
        if peminjaman.get_anggota() is not self:
            raise ValueError("Peminjaman ini bukan milik anggota tersebut")
        tanggal_kembali = tanggal_kembali or date.today()
        denda = peminjaman.proses_pengembalian(tanggal_kembali)
        self.ubah_jumlah_pinjam(-1)
        return denda

    def tampilkan_data(self):
        super().tampilkan_data()
        print(f"Peran        : Anggota")
        print(f"Sedang pinjam: {self.__jumlah_pinjam}/{self.BATAS_PINJAM} buku")
