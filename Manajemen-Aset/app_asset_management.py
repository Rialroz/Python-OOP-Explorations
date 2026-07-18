class FormatAssetTidakValid(Exception):
    def __init__(self, message):
        self.message = "Input tidak valid"

    def __str__(self):
        return self.message

class Asset:
    def __init__ (self, kode, nama, harga):
        self.kode = kode
        self.nama = nama
        self.harga = harga

class AssetKendaraan(Asset):
    def __init__ (self, kode, nama, harga, stnk, tahun):
        super().__init__(kode, nama, harga)
        self.stnk = stnk
        self.tahun = tahun

class AssetElektronik(Asset):
    def __init__ (self, kode, nama, harga, serial_number):
        super().__init__(kode, nama, harga)
        self.serial_number = serial_number

class AssetTanahBangunan(Asset):
    def __init__ (self, kode, nama, harga, sertifikat, njop, luas):
        super().__init__(kode, nama, harga)
        self.sertifikat = sertifikat
        self.njop = njop
        self.luas = luas

class DaftarAsset:
    def __init__ (self):
        self.daftar_asset = []

    def tambah_asset(self, asset):
        self.daftar_asset.append(asset)

    def ambil_asset(self, kode):
        for asset in self.daftar_asset:
            if asset.kode == kode:
                return asset
        return None
    
    def hapus_asset(self, kode):
        for i, asset in enumerate(self.daftar_asset):
            if asset.kode == kode:
                del self.daftar_asset[i]
                return True
        return False

class AplikasiAssetManagement:
    def __init__ (self):
        self.daftar_asset = DaftarAsset()

    def run(self):
        while True:
            print("1. Tambah Asset")
            print("2. Lihat Daftar Asset")
            print("3. Keluar")
            pilih = input("Pilih menu: ")

            if pilih == "1":
                self.run_tambah_asset()
            elif pilih == "2":
                self.run_lihat_daftar_asset()
            elif pilih == "3":
                break
            else:
                print("Input tidak valid")

    def run_tambah_asset(self):
        while True:
            print("1. Tambah Asset Kendaraan")
            print("2. Tambah Asset Elektronik")
            print("3. Tambah Asset Tanah Bangunan")
            print("4. Kembali")
            pilih = input("Pilih menu: ")

            if pilih == "1":
                self.run_tambah_asset_kendaraan()
                print("Asset Kendaraan berhasil ditambahkan")
            elif pilih == "2":
                self.run_tambah_asset_elektronik()
                print("Asset Elektronik berhasil ditambahkan")
            elif pilih == "3":
                self.run_tambah_asset_tanah_bangunan() 
                print("Asset Tanah Bangunan berhasil ditambahkan")
            elif pilih == "4":
                break
            else:
                print("Input tidak valid")

    def run_tambah_asset_kendaraan(self):
        print("Tambah Asset Kendaraan")
        kode = input("Kode: ")
        nama = input("Nama: ")
        harga = input("Harga: ")
        stnk = input("STNK: ")
        tahun = input("Tahun: ")

        asset_kendaraan = AssetKendaraan(kode, nama, harga, stnk, tahun)
        self.daftar_asset.tambah_asset(asset_kendaraan)

    def run_tambah_asset_elektronik(self):
        print("Tambah Asset Elektronik")
        kode = input("Kode: ")
        nama = input("Nama: ")
        harga = input("Harga: ")
        serial_number = input("Serial Number: ")

        asset_elektronik = AssetElektronik(kode, nama, harga, serial_number)
        self.daftar_asset.tambah_asset(asset_elektronik)


    def run_tambah_asset_tanah_bangunan(self):
        print("Tambah Asset Tanah Bangunan")
        kode = input("Kode: ")
        nama = input("Nama: ")
        harga = input("Harga: ")
        sertifikat = input("Sertifikat: ")
        njop = input("NJOP: ")
        luas = input("Luas: ")

        asset_tanah_bangunan = AssetTanahBangunan(kode, nama, harga, sertifikat, njop, luas)
        self.daftar_asset.tambah_asset(asset_tanah_bangunan)


    def run_lihat_daftar_asset(self):
        for asset in self.daftar_asset.daftar_asset:
            if isinstance(asset, AssetKendaraan):
                print(f"Kode: {asset.kode}, Nama: {asset.nama}, Harga: {asset.harga}, STNK: {asset.stnk}, Tahun: {asset.tahun}")
            elif isinstance(asset, AssetElektronik):
                print(f"Kode: {asset.kode}, Nama: {asset.nama}, Harga: {asset.harga}, Serial Number: {asset.serial_number}")
            elif isinstance(asset, AssetTanahBangunan):
                print(f"Kode: {asset.kode}, Nama: {asset.nama}, Harga: {asset.harga}, Sertifikat: {asset.sertifikat}, NJOP: {asset.njop}, Luas: {asset.luas}")
        
        print("Menu")
        print("1. Ubah Asset")
        print("2. Hapus Asset")
        print("3. Kembali")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            self.run_ubah_asset()
        elif pilih == "2":
            self.run_hapus_asset()
        elif pilih == "3":
            pass
        else:
            print("Input tidak valid")

    def run_ubah_asset(self):
        kode = input("Kode asset yang ingin diubah: ")
        asset = self.daftar_asset.ambil_asset(kode)

        if asset is None:
            print(f"Asset tidak ditemukan kode : {kode}")
            return

        else:
            if isinstance(asset, AssetKendaraan):
                nama = input("Nama: ")
                harga = input("Harga: ")
                stnk = input("STNK: ")
                tahun = input("Tahun: ")

                asset.nama = nama
                asset.harga = harga
                asset.stnk = stnk
                asset.tahun = tahun

                print("Asset berhasil diubah")

            elif isinstance(asset, AssetElektronik):
                nama = input("Nama: ") 
                harga = input("Harga: ")
                serial_number = input("Serial Number: ")

                asset.nama = nama
                asset.harga = harga
                asset.serial_number = serial_number

                print("Asset berhasil diubah")

            elif isinstance(asset, AssetTanahBangunan):
                nama = input("Nama: ")
                harga = input("Harga: ")
                sertifikat = input("Sertifikat: ")
                njop = input("NJOP: ")
                luas = input("Luas: ")

                asset.nama = nama
                asset.harga = harga
                asset.sertifikat = sertifikat
                asset.njop = njop
                asset.luas = luas

                print("Asset berhasil diubah")

    def run_hapus_asset(self):
        kode = input("Kode asset yang ingin dihapus: ")
        if self.daftar_asset.hapus_asset(kode):
            print(f"Asset dengan kode {kode} berhasil dihapus")
        else:
            print(f"Asset dengan kode {kode} tidak ditemukan")


if __name__ == "__main__":
    app = AplikasiAssetManagement()
    app.run()
    print("Terima kasih telah menggunakan aplikasi ini!")
