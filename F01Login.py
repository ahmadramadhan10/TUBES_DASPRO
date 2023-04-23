# Program Login Untuk Bandung Bondowoso, Roro Jongrang, dan Jin
# Menerima Input (Username, Password) dan memastikan tidak ada User yang sama

def login (users, current_login):
    if current_login != -1: # Bila sudah login
        print ("Login gagal!")
        print ("Anda telah login dengan username " + users[current_login][0] + ", silahkan lakukan “logout” sebelum melakukan login kembali.")
        return(current_login)

    Username = input("Username: ")
    Password = input("Password: ")
    print("")

    IdLogin = CheckWhoIsLogin(Username, users) # Mengecek indeks (baris users) yang ingin login
    
    if (IdLogin == 0): # Pengecekan untuk Bandung Bondowoso
        if (Password == "cintaroro"):
            print ("Selamat datang, Bandung!")
            print ("Masukkan command “help” untuk daftar command yang dapat kamu panggil")
            current_login = IdLogin
        else: # Password Salah
            print ("Password Salah!")
    elif (IdLogin == 1): # Pengecekan untuk Roro Jonggrang
        if (Password == "gasukabondo"):
            print ("Selamat datang, Roro!")
            print ("Masukkan command “help” untuk daftar command yang dapat kamu panggil")
            current_login = IdLogin
        else: # Password Salah
            print ("Password Salah")
    elif (IdLogin == -1): # Username salah
        print ("Username tidak terdaftar!")
    else: # Pengecekan untuk Jin
        if (Password == users[IdLogin][1]):
            print ("Selamat datang, " + Username)
            print ("Masukkan command “help” untuk daftar command yang dapat kamu panggil")
            current_login = IdLogin
        else:
            print("Password Salah!")
    
    return(current_login)
    
def CheckWhoIsLogin (Username,users):
    for i in range (102):
        if (Username == users[i][0]):
            return (i) # Username ada di list dengan indeks (baris) i
    return(-1) # Bila username tidak ada di list users