
def hancurkan(candi, current_login):
    if current_login == 1: # cek apakah user login yang sekarang adalah roro jonggrang
        # KAMUS
        # id : Integer
        # decision : string
        id = int(input("Masukkan ID candi: ")) # memasukkan input ID
        if candi[id][0] != "": # cek ID
            decision = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ") # menanyakan ulang apakah ingin menghapus candi atau tidak
            if decision == "Y": # jika yakin, maka hapus candi
                candi[id] = ["",0,0,0]
                print("\nCandi telah berhasil dihancurkan")
            else: # tidak jadi dihancurkan
                print("\nCandi tidak jadi dihancurkan")
        else: # ID-nya tidak ada
            print("\nTidak ada candi dengan ID tersebut.")
    else: # role yang login sekarang bukan roro jonggrang
        print("Command “hancurkancandi” hanya bisa dipanggil oleh Roro Jonggrang!")
    return(candi) # mengembalikan array candi