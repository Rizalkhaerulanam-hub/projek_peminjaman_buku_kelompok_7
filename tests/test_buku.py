import io
import unittest
from contextlib import redirect_stdout

from models.buku import Buku


class TestBuku(unittest.TestCase):
    def setUp(self):
        self.buku = Buku("B001", "Pemrograman Python", "Andi", 2)

    def test_buat_buku(self):
        self.assertEqual(self.buku.get_id(), "B001")
        self.assertEqual(self.buku.get_judul(), "Pemrograman Python")
        self.assertEqual(self.buku.get_penulis(), "Andi")
        self.assertEqual(self.buku.get_stok(), 2)

    def test_stok_awal_negatif_ditolak(self):
        with self.assertRaises(ValueError):
            Buku("B002", "X", "Y", -1)

    def test_atribut_stok_private(self):
        self.assertFalse(hasattr(self.buku, "stok"))

    def test_tersedia(self):
        self.assertTrue(self.buku.tersedia())
        self.assertFalse(Buku("B003", "Habis", "Z", 0).tersedia())

    def test_kurangi_stok(self):
        self.buku.kurangi_stok()
        self.assertEqual(self.buku.get_stok(), 1)

    def test_kurangi_stok_saat_habis_ditolak(self):
        buku = Buku("B004", "Habis", "Z", 0)
        with self.assertRaises(ValueError):
            buku.kurangi_stok()
        self.assertEqual(buku.get_stok(), 0)

    def test_tambah_stok(self):
        self.buku.tambah_stok()
        self.assertEqual(self.buku.get_stok(), 3)

    def test_ubah_data(self):
        self.buku.ubah_data("Python Lanjut", "Budi", 10)
        self.assertEqual(self.buku.get_judul(), "Python Lanjut")
        self.assertEqual(self.buku.get_penulis(), "Budi")
        self.assertEqual(self.buku.get_stok(), 10)

    def test_ubah_data_stok_negatif_ditolak(self):
        with self.assertRaises(ValueError):
            self.buku.ubah_data("A", "B", -1)
        self.assertEqual(self.buku.get_stok(), 2)

    def test_tampilkan_info(self):
        out = io.StringIO()
        with redirect_stdout(out):
            self.buku.tampilkan_info()
        self.assertIn("Pemrograman Python", out.getvalue())


if __name__ == "__main__":
    unittest.main()
