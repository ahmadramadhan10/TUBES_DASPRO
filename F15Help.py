def help(current_login, users):
    if current_login == 0:
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. hapusjin")
        print("   Untuk menghapus jin yang sudah dipanggil")
        print("4. ubahjin")
        print("   Untuk mengubah tipe jin")
        print("5. batchkumpul")
        print("   Untuk mengerahkan seluruh jin pengumpul untuk mengumpulkan bahan")
        print("6. batchbangun")
        print("   Untuk mengerahkan seluruh jin pembangun untuk membangun candi")
        print("7. laporanjin")
        print("   Untuk menampilkan laporan dari jin yang sudah dipanggil")
        print("8. laporancandi")
        print("   Untuk menampilkan laporan dari candi yang sudah dibuat")
        print("9. save")
        print("   Untuk menyimpan data saat ini pada suatu folder")
        print("10. exit")
        print("    Untuk keluar dari permainan")
    elif current_login == 1:
        print("=========== HELP ===========")
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi yang sudah dibuat")
        print("3. ayamberkokok")
        print("   Untuk menyelesaikan permainan dengan memalsukan pagi hari")
        print("4. save")
        print("   Untuk menyimpan data saat ini pada suatu folder")
        print("5. exit")
        print("   Untuk keluar dari permainan")
    elif current_login == -1:
        print("=========== HELP ===========")
        print("1. login")
        print("   Untuk masuk ke akun")
        print("2. exit")
        print("   Untuk keluar dari permainan")
    else:
        if users[current_login][2] == "jin_pengumpul":
            print("=========== HELP ===========")
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. kumpul")
            print("   Untuk mengumpulkan bahan bangunan")
            print("3. save")
            print("   Untuk menyimpan data saat ini pada suatu folder")
            print("4. exit")
            print("   Untuk keluar dari permainan")
        else:
            print("=========== HELP ===========")
            print("1. logout")
            print("   Untuk keluar dari akun yang digunakan sekarang")
            print("2. bangun")
            print("   Untuk membangun candi")
            print("3. save")
            print("   Untuk menyimpan data saat ini pada suatu folder")
            print("4. exit")
            print("   Untuk keluar dari permainan")

"""
users =[["test","test","jin_pengumpul"],["test","test","test"],
        ["test","test","jin_pengumpul"]]
current_login = 2

help(current_login, users)
"""
