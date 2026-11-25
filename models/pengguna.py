class Pengguna:
    """Menyimpan data identitas yang dimiliki semua pengguna sistem."""

    def __init__(self, id_pengguna, nama, no_telepon):
        self.__id_pengguna = id_pengguna
        self.__nama = nama
        self.__no_telepon = no_telepon

    def get_id(self):
        return self.__id_pengguna

    def get_nama(self):
        return self.__nama

    def get_no_telepon(self):
        return self.__no_telepon

    def tampilkan_data(self):
        print(f"ID        : {self.__id_pengguna}")
        print(f"Nama      : {self.__nama}")
        print(f"No Telepon: {self.__no_telepon}")
