from F02Logout import logout
from F05UbahTipeJin import ubahTipeJin
from F10LaporanCandi import laporanCandi
from F13Load import loadFolder, LoadFile
from F14Save import save
from F15Help import help
from F16Exit import exit

jumlahusers = 102
jumlahcandi = 100

users = [["" for i in range (3)]for j in range(jumlahusers)]
candi = [["",0,0,0]for j in range(jumlahcandi)]
bahan = [0 for i in range (3)]

users, candi, bahan = loadFolder(users, candi, bahan)
# saran ku sebelum nge load cek dlu file nya ada atau tidak 

current_login = -1 # id yang login sekarang, jika -1 maka tidak yang login

def main():

    # saranku disini buat if condition
    # cek jika file tidak ada atau nama file input tidak dikasih langsung return aja / keluar program
    # soalnya dispesifikasi langsung disuruh keluar program kalau load filenya salah
    # file = LoadFile()
    # if not file:
    #    return

    while True:
        command = input(">>> ")
        if command == "logout":
            current_login = logout(current_login)
        elif command == "ubahjin":
            users = ubahTipeJin(jumlahusers, users, current_login)
        elif command == "laporancandi":
            laporanCandi(jumlahcandi, candi, current_login)
        elif command == "save":
            save(jumlahusers, users, jumlahcandi, candi, bahan)
        elif command == "help":
            help(current_login, users)
        elif command == "exit":
            exit(jumlahusers, users, jumlahcandi, candi, bahan)
            break

main()