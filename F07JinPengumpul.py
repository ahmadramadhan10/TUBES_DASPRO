# function jinPengumpul (users : matriksusers, bahan : matriksbahan, current_login : integer) -> matriksbahan
# Mengecek nilai current_login, kemudian menampilkan banyaknya bahan yang berhasil dikumpulkan secara random, lalu mengembalikan matriksbahan yang sudah ditambahkan dengan bahan-bahan yang baru dikumpulkan

from random import randint # Import random from library
def jinPengumpul (users, bahan, current_login):
    # KAMUS LOKAL
    # pasir, batu, air : integer
    if users[current_login][2] == "jin_pengumpul": # Jika yang memanggil fungsi ini memiliki role sebagai jin pengumpul
        pasir = randint(0,5) # Mengumpulkan bahandengan menggunakan angka random
        batu = randint(0,5)
        air = randint(0,5)
        bahan[0] += pasir # Jumlah bahan pada matriks ditambahkan dengan bahan yang sudah dikumpulkan
        bahan[1] += batu
        bahan[2] += air
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.") # Mengeluarkan output berapa bahan yang dikumpulkan jin
    else:
        print("Command “kumpul” hanya bisa dipanggil oleh user dengan role Jin Pengumpul!") # Jika yang memanggil fungsi bukan jin pengumpuls
    return(bahan)