from F01Login import login
from F02Logout import logout
from F03SummonJin import Summon
from F04HilangkanJin import hilangkanJin
from F05UbahTipeJin import ubahTipeJin
from F06JinPembangun import bangun
from F07JinPengumpul import jinPengumpul
from F08BatchKumpulBangun import BatchKumpulBangun
from F09AmbilLaporanJin import ambilLaporanJin
from F10LaporanCandi import laporanCandi
from F11HancurkanCandi import hancurkan
from F12AyamBerkokok import ayamberkokok
from F13Load import loadFolder
from F14Save import save
from F15Help import help
from F16Exit import exit

# Program Permainan100Candi
# Spesifikasi Program : Permainan dengan tema cerita rakyat Roro Jonggrang dengan Bandung Bondowoso 

# KAMUS
# jumlahusers, jumlahcandi, i, j, current_login : integer
# kondisi : boolean
# command : string
# users : matriks of integer
# candi : matriks of integer and string
# bahan : array of integer 

# ALGORITMA
jumlahusers = 102 # jumlahusers maksimal yang mungkin ada dalam program adalah 102 (termasuk Bandung Bondowoso, Roro Jonggrang, dan Jin)
jumlahcandi = 100 # jumlahcandi maksimal yang mungkin dibangun adalah 100

users = [["" for i in range (3)]for j in range(jumlahusers)] # Matriks users dengan jumlah baris <= jumlahusers-1
candi = [["",0,0,0]for j in range(jumlahcandi)] # Matriks candi dengan jumlah baris <= jumlahcandi-1
bahan = [0 for i in range (3)] # Matriks bahan

users, candi, bahan, kondisi = loadFolder(users, candi, bahan) # Melakukan load file sesuai dengan input user di terminal

current_login = -1 # id yang login sekarang, jika -1 maka user belum melakukan login

while kondisi == True: # Selama program belum harus berhenti maka kondisi akan selalu == True
    command = input("\n>>> ") # Perintah yang dituliskan oleh user
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
    elif command == "laporanjin":
        ambilLaporanJin(jumlahusers, users, bahan, candi, current_login, jumlahcandi)
    elif command == "laporancandi":
        laporanCandi(jumlahcandi, candi, current_login)
    elif command == "hancurkancandi":
        candi = hancurkan(candi, current_login)
    elif command == "ayamberkokok":
        kondisi = ayamberkokok(candi, current_login, jumlahcandi)
    elif command == "save":
        save(jumlahusers, users, jumlahcandi, candi, bahan)
    elif command == "help":
        help(current_login, users)
    elif command == "exit":
        exit(jumlahusers, users, jumlahcandi, candi, bahan)
        kondisi = False # Apabila user ingin menghentikan program (ketika user memasukkan perintah exit maka otomatis program akan pasti berhenti)
    else: # Apabila command yang dimasukkan user salah
        print("Command yang diinput salah, ketik “help” untuk melihat command yang bisa diinput!")