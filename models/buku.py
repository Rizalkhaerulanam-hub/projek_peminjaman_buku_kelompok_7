class Buku:
    """Data buku. Validasi stok dilakukan di class ini (encapsulation)."""

    def __init__(self, id_buku, judul, penulis, stok):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")
        self.__id_buku = id_buku
        self.__judul = judul
        self.__penulis = penulis
        self.__stok = stok

    def get_id(self):
        return self.__id_buku

    def get_judul(self):
        return self.__judul

    def get_penulis(self):
        return self.__penulis

    def get_stok(self):
        return self.__stok

    def tersedia(self):
        return self.__stok > 0

    def kurangi_stok(self):
        if not self.tersedia():
            raise ValueError("Stok buku habis")
        self.__stok -= 1

    def tambah_stok(self):
        self.__stok += 1

    def ubah_data(self, judul, penulis, stok):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")
        self.__judul = judul
        self.__penulis = penulis
        self.__stok = stok

    def tampilkan_info(self):
        print(f"[{self.__id_buku}] {self.__judul} - {self.__penulis} (stok: {self.__stok})")
