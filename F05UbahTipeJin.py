def ubahTipeJin (jumlahusers, users, current_login):
    if current_login == 0:
        username = input("Masukkan username jin : ")
        for i in range(jumlahusers):
            if username == users[i][0]:
                if users [i][2] == "jin_pengumpul":
                    print("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ", end="")
                    konfirmasi = input()
                    if konfirmasi == "Y":
                        users[i][2] = "jin_pembangun"
                        print("\nJin telah berhasil diubah")
                    else:
                        print("\nJin tidak jadi diubah")
                    return(users)
                else:
                    print("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ", end="")
                    konfirmasi = input()
                    if konfirmasi == "Y":
                        users[i][2] = "jin_pengumpul"
                        print("\nJin telah berhasil diubah")
                    else:
                        print("\nJin tidak jadi diubah")
                    return(users)
        print("\nTidak ada jin dengan username tersebut.")
        return(users)
    else:
        print("\nCommand “ubahjin” hanya bisa dipanggil oleh Bandung Bondowoso!")
        return(users)

"""
users = [["test","test","jin_pengumpul"],["jinb2","1","jin_pembangun"]]
jumlahusers = 2
current_login = 0

ubahTipeJin(jumlahusers, users, current_login)

print(users)
"""