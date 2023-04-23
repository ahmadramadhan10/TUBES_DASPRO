# function logout (current_login : integer) -> integer
# Mengecek nilai current_login, kemudian mengembalikan nilai -1
# untuk menandakan bahwa user sedang tidak login

def logout(current_login):
    # KAMUS LOKAL

    # ALGORITMA
    if current_login == -1: # Apabila user belum melakukan login
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else: # Apabila user sudah melakukan login
        print("Logout berhasil!")
    return(-1) # Mereturn current_login dengan hasil -1 (menandakan user belum login)