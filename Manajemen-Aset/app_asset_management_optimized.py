class FormatAsetTidakValidError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message
    

def ambil_input(pesan, tipe_data): 
        #pesan diisi "Masukkan kode asset: " dan sejenisnya
        #tipe_data diisi int, str, float, dll. Jika tidak ditentukan harus diisi None, akan dianggap sebagai tipe data semua
        while True:
            try:
                jawaban_mentah = input(pesan)
                
                if tipe_data == int:
                    # Pemaksaan. Kalau user ketik huruf, fungsi int() meledak
                    # dan langsung terlempar ke blok 'except ValueError' di bawah.
                    angka_bersih = int(jawaban_mentah)
                    return angka_bersih
                
                elif tipe_data == float:
                    # Pemaksaan. Kalau user ketik huruf, fungsi float() meledak
                    # dan langsung terlempar ke blok 'except ValueError' di bawah.
                    angka_bersih = float(jawaban_mentah)
                    return angka_bersih
                    
                elif tipe_data == str:
                    # Kita buang spasi sementara, lalu interogasi apakah murni abjad
                    cek_huruf = jawaban_mentah.replace(" ", "")
                    if cek_huruf.isalpha():
                        return jawaban_mentah
                    else:
                        # Kalau ada angka/simbol, kita panggil alarm kustom secara manual
                        # tanpa harus memicu crash program
                        alarm = FormatAsetTidakValidError("Error: Input wajib huruf murni, tanpa angka/simbol!")
                        print(alarm)
                        continue # Ulangi pusaran dari awal
                else:
                    # Kalau tipe data tidak ditentukan, biarkan lolos apa adanya
                    return jawaban_mentah
                    
            except ValueError:
                # Tangkapan jaring khusus untuk fungsi int() yang gagal
                alarm = FormatAsetTidakValidError("Error: Input wajib berupa angka utuh!")
                print(alarm)

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

    @classmethod
    def buat_dari_input(cls):
        kode = ambil_input("Masukkan kode asset: ", str)
        nama = ambil_input("Masukkan nama asset: ", None)
        harga = ambil_input("Masukkan harga asset: ", int)
        stnk = ambil_input("Masukkan nomor STNK: ", int)
        tahun = ambil_input("Masukkan tahun pembuatan: ", int)

        return cls(kode, nama, harga, stnk, tahun)

    def tampilkan_info(self):
        print(f"Kode: {self.kode}")
        print(f"Nama: {self.nama}")
        print(f"Harga: {self.harga}")
        print(f"STNK: {self.stnk}")
        print(f"Tahun: {self.tahun}")
    def perbarui_data(self):
        self.nama = ambil_input("Masukkan nama asset: ", None)
        self.harga = ambil_input("Masukkan harga asset: ", int)
        self.stnk = ambil_input("Masukkan nomor STNK: ", int)
        self.tahun = ambil_input("Masukkan tahun pembuatan: ", int)
        

class AssetElektronik(Asset):
    def __init__ (self, kode, nama, harga, serial_number):
        super().__init__(kode, nama, harga)
        self.serial_number = serial_number

    @classmethod
    def buat_dari_input(cls):
        kode = ambil_input("Masukkan kode asset: ", str)
        nama = ambil_input("Masukkan nama asset: ", None)
        harga = ambil_input("Masukkan harga asset: ", int)
        serial_number = ambil_input("Masukkan nomor serial: ", int)

        return cls(kode, nama, harga, serial_number)

    def tampilkan_info(self):
        print(f"Kode: {self.kode}")
        print(f"Nama: {self.nama}")
        print(f"Harga: {self.harga}")
        print(f"Serial Number: {self.serial_number}")

    def perbarui_data(self):
        self.nama = ambil_input("Masukkan nama asset: ", None)
        self.harga = ambil_input("Masukkan harga asset: ", int)
        self.serial_number = ambil_input("Masukkan nomor serial: ", int)

class AssetTanahBangunan(Asset):
    def __init__ (self, kode, nama, harga, sertifikat, njop, luas):
        super().__init__(kode, nama, harga)
        self.sertifikat = sertifikat
        self.njop = njop
        self.luas = luas
    
    @classmethod
    def buat_dari_input(cls):
        kode = ambil_input("Masukkan kode asset: ", str)
        nama = ambil_input("Masukkan nama asset: ", None)
        harga = ambil_input("Masukkan harga asset: ", int)
        sertifikat = ambil_input("Masukkan nomor sertifikat: ", int)
        njop = ambil_input("Masukkan NJOP: ", int)
        luas = ambil_input("Masukkan luas tanah/bangunan: ", float)

        return cls(kode, nama, harga, sertifikat, njop, luas)


    def tampilkan_info(self):
        print(f"Kode: {self.kode}")
        print(f"Nama: {self.nama}")
        print(f"Harga: {self.harga}")
        print(f"Sertifikat: {self.sertifikat}")
        print(f"NJOP: {self.njop}")
        print(f"Luas: {self.luas}")

    def perbarui_data(self):
        self.nama = ambil_input("Masukkan nama asset: ", None)
        self.harga = ambil_input("Masukkan harga asset: ", int)
        self.sertifikat = ambil_input("Masukkan nomor sertifikat: ", int)
        self.njop = ambil_input("Masukkan NJOP: ", int)
        self.luas = ambil_input("Masukkan luas tanah/bangunan: ", float)


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
        for asset in self.daftar_asset:
            if asset.kode == kode:
                self.daftar_asset.remove(asset)
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
                
            elif pilih == "2":
                self.run_tambah_asset_elektronik()
                
            elif pilih == "3":
                self.run_tambah_asset_tanah_bangunan() 
                
            elif pilih == "4":
                break
            else:
                print("Input tidak valid")

    def run_tambah_asset_kendaraan(self):
        print("Tambah Asset Kendaraan")
        asset_baru = AssetKendaraan.buat_dari_input()
        self.daftar_asset.tambah_asset(asset_baru)

        print("Asset Kendaraan berhasil ditambahkan")   

    def run_tambah_asset_elektronik(self):
        print("Tambah Asset Elektronik")
        
        asset_baru = AssetElektronik.buat_dari_input()
        self.daftar_asset.tambah_asset(asset_baru)

        print("Asset Elektronik berhasil ditambahkan")


    def run_tambah_asset_tanah_bangunan(self):
        print("Tambah Asset Tanah Bangunan")
        
        asset_baru = AssetTanahBangunan.buat_dari_input()
        self.daftar_asset.tambah_asset(asset_baru)

        print("Asset Tanah Bangunan berhasil ditambahkan")


    def run_lihat_daftar_asset(self):
        print("Daftar Asset")
        for asset in self.daftar_asset.daftar_asset:
            asset.tampilkan_info()
            print()

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
            asset.perbarui_data()
            print(f"Asset dengan kode {kode} berhasil diubah")


                
    def run_hapus_asset(self):
        kode = input("Kode asset yang ingin dihapus: ")
        if self.daftar_asset.hapus_asset(kode):
            print(f"Asset dengan kode {kode} berhasil dihapus")
        else:
            print(f"Asset dengan kode {kode} tidak ditemukan")

    def run_search_asset(self):
        kode = input("Kode asset yang ingin dicari: ")
        asset = self.daftar_asset.ambil_asset(kode)

        if asset is None:
            print(f"Asset tidak ditemukan kode : {kode}")
        else:
            # Langsung panggil info dari objek tunggal yang ditemukan!
            asset.tampilkan_info()


if __name__ == "__main__":
    app = AplikasiAssetManagement()
    app.run()
    print("Terima kasih telah menggunakan aplikasi ini!")