import time
import sys
import os

biodata = {
    "Nama Lengkap"   : "Whirit Wening Windar Shineta",
    "Nama Panggilan" : "Windar",
    "NIM"            : "1202407010",
    "Program Studi"  : "Informatika",
    "Fakultas"       : "Fakultas Sains dan Teknologi",
    "Universitas"    : "Universitas Muhammadiyah PKU Surakarta",
    "Jenis Kelamin"  : "Perempuan",
    "Tempat Lahir"   : "Gunungkidul",
    "Tanggal Lahir"  : "10 Juli 2005",
    "Alamat"         : "Duwet, Karangwuni, Rongkop, Gunungkidul, DIY.",
    "Agama"          : "Islam",
    "Kewarganegaraan": "Indonesia",
    "Idola"          : "Hong Pichetpong, Choi Beomgyu, William Jakrapatr, Nanon Korapat, Kim Sunoo, Jeon Jungkook, Park Jinyoung",
    "Grup Fav"       : "LYKN, Felizz, TXT, Enhypen, BTS, GOT7",
    "Hobi"           : "Membaca AU/novel, menulis cerita fiksi, mendengarkan musik",
    "Lagu favorit"   : "Trust Me, Just Friend, Spring Day, First Sight, Love Echo, Last Twilight, Not By The Moon",
    "Warna Favorit"  : "Biru dan merah muda",
    "Drama fav"      : "Lets Fight Ghost, Bad Buddy, Thamepo, A Tale of Thausand Stars, Who are you: School 2015, The Devil Jugde",
    "Cita-cita"      : "Menjadi seorang penulis",
    "Impian"         : "Bertemu idola, kuliah di Chulalongkorn University, bisa keliling dunia",
    "Motto Hidup"    : "Aku menulis seperti menulis kode — setiap kata adalah algoritma untuk menyihir hati dan pikiran"
}

def ketik(teks, delay=0.03):
    for huruf in teks:
        sys.stdout.write(huruf)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def tampilkan_biodata():
    os.system('cls' if os.name == 'nt' else 'clear')
    ketik("BIODATA WINDAR", 0.06)
    print()
    loading()

def loading(pesan="Memuat biodata Windar"):
    ketik(pesan, 0.05)
    for i in range(1, 21):
        bar = "█" * i + "-" * (20 - i)
        sys.stdout.write(f"\r[{bar}] {i*5}%")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n")

    for kunci, nilai in biodata.items():
        ketik(f"{kunci:<17}: {nilai}", 0.02)

    print()
    ketik("=" * 50, 0.01)
    ketik("Ingat kata phi Nnanon -Kalau kamu benar-benar mencintai sesuatu, lakukan sepenuh hati. Maka dunia akan ikut mendengarnya", 0.04)
    ketik("Terima kasih sudah membaca biodata windar ♡", 0.04)

if __name__ == "__main__":
    tampilkan_biodata()
