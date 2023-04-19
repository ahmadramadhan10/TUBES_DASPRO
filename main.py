
import F01, F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16
import B01, B02, B03, B04
import os

limit_user = 1000 # jadi kita mengasumsikan maksimal 1000 user
users = []*1000
candi = []*1000
can_access = [True]*1000
bahan_bangunan = []*1000

def main():

    #load data
    load_file = F13.load()
    if not load_file: # jika tidak bisa di load maka keluar dari program
        return
    len_users = limit_user
    game_over = False # Jika game over maka program keluar
    current_login = -1 # nilai default user login

    while not game_over: # permainan akan selalu jalan selama belum game over

        input_command = input(">>> ") # meminta masukan perintah
        
        if  input_command == "login":
            if current_login == -1: # jika belum ada yang login
                current_login = F01.login(users, len_users, current_login, can_access)
            else: # jika ada login maka gagal
                print("Login gagal!")
                print(f'Anda telah login dengan user name {users[current_login][0]}, silahkan lakukan "logout"')
                print(f'sebelum melakukan login kembali.')\
        
        elif input_command == "logout":
            current_login = F02.logout(current_login,can_access)

        elif input_command == "summonjin":
            print("Jenis jin yang dapat dipanggil:")
            print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
            print(" (2) Pembangun - Bertugas membangun candi\n")
            F03.SummonJin()
            pass

        elif input_command == "hapusjin":
            pass
        elif input_command == "ubajin":
            pass
        elif input_command == "bangun":
            pass
        elif input_command == "kumpul":
            pass
        elif input_command == "batchkumpul" or input_command == "batchbangun":
            pass
        elif input_command == "laporanjin":
            pass
        elif input_command == "laporancandi":
            pass
        elif input_command == "hancurkancandi":
            pass
        elif input_command == "ayamberkokok":
            pass
        elif input_command == "save":
            F14.save()
        elif input_command == "help":
            F15.help()
        elif input_command == "exit":
            pass

main()