from F01Login import login
from F02Logout import logout
from F03SummonJin import Summon
from F04HilangkanJin import hilangkanJin
from F05UbahTipeJin import ubahTipeJin
from F06JinPembangun import bangun
from F07JinPengumpul import jinPengumpul
from F08BatchKumpulBangun import BatchKumpulBangun
from F10LaporanCandi import laporanCandi
from F11HancurkanCandi import hancurkan
from F12AyamBerkokok import ayamberkokok
from F13Load import loadFolder
from F14Save import save
from F15Help import help
from F16Exit import exit

jumlahusers = 102
jumlahcandi = 100

users = [["" for i in range (3)]for j in range(jumlahusers)]
candi = [["",0,0,0]for j in range(jumlahcandi)]
bahan = [0 for i in range (3)]

users, candi, bahan, kondisi = loadFolder(users, candi, bahan)

current_login = -1 # id yang login sekarang, jika -1 maka tidak yang login

while kondisi == True:
    command = input(">>> ")
    if command == "login":
        current_login = login(users, current_login)
    elif command == "logout":
        current_login = logout(current_login)
    elif command == "summonjin":
        users = Summon(users, current_login)
    elif command == "hapusjin":
        users, candi = hilangkanJin(jumlahusers, users, jumlahcandi, candi, current_login)
    elif command == "ubahjin":
        users = ubahTipeJin(jumlahusers, users, current_login)
    elif command == "bangun":
        bahan, candi = bangun(bahan, candi, jumlahcandi, current_login, users)
    elif command == "kumpul":
        bahan = jinPengumpul(users, bahan, current_login)
    elif command == "batchbangun" or command == "batchkumpul":
        bahan, candi = BatchKumpulBangun(command, users, jumlahusers, bahan, candi, jumlahcandi, current_login)
    elif command == "laporancandi":
        laporanCandi(jumlahcandi, candi, current_login)
    elif command == "hancurkancandi":
        candi = hancurkan(candi, current_login)
    elif command == "ayamberkokok":
        ayamberkokok(candi, current_login, jumlahcandi)
        break
    elif command == "save":
        save(jumlahusers, users, jumlahcandi, candi, bahan)
    elif command == "help":
        help(current_login, users)
    elif command == "exit":
        exit(jumlahusers, users, jumlahcandi, candi, bahan)
        break