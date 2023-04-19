def logout(current_login, can_access): 
    if current_login == -1:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    return -1