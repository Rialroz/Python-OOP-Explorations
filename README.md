# Python-OOP-Explorations
Repositori ini adalah dokumentasi proyek eksplorasi saat mempelajari fundamental Object-Oriented Programming (OOP) menggunakan Python. Alih-alih hanya menyerap materi secara pasif, konsep OOP di sini langsung diterapkan ke dalam program Command Line Interface (CLI) sederhana.

**Konsep Arsitektur yang Diterapkan**
Fokus utama dari proyek ini bukanlah pada kerumitan fitur antarmuka, melainkan pada kebersihan dan skalabilitas arsitektur kode. Beberapa implementasi teknis di dalamnya meliputi:

Inheritance & Encapsulation: Memisahkan entitas ke dalam Class spesifik (Kendaraan, Elektronik, Tanah/Bangunan) yang mewarisi sifat dari Class induk.

Polymorphism: Menyederhanakan fitur pencarian dan pembaruan data tanpa tumpukan logika if-else yang panjang. Setiap objek tahu cara menampilkan dan memperbarui datanya sendiri.

Factory Method: Menggunakan dekorator @classmethod untuk mengatasi paradoks instansiasi dan mendelegasikan tugas pengumpulan data ke masing-masing kelas.

Custom Exception Handling: Memusatkan logika validasi tipe data (integer, string) ke dalam satu fungsi pelindung untuk menjaga program dari input error pengguna.
