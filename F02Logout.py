def logout(current_login):
    if current_login == -1:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else:
        print("\nLogout berhasil!")
    return(-1)

"""
current_login = -1
current_login = logout(current_login)
"""