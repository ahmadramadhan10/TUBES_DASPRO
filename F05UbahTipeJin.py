# function ubahTipeJin (jumlahusers : integer, users : matriksusers, current_login : integer) -> matriksusers
# Mengecek nilai current_login, kemudian mengubah tipe jin yang disimpan program sesuai dengan masukan user

def ubahTipeJin (jumlahusers, users, current_login):
    # KAMUS LOKAL
    # username, konfirmasi : string
    # i : integer

    # ALGORITMA
    if current_login == 0: # Validasi apakah user saat ini memiliki role sebagai Bandung Bondowoso
        username = input("Masukkan username jin : ") # Meminta username jin dari user
        for i in range(2,jumlahusers): # Mencari apakah username jin yang diinput oleh user valid
            if username == users[i][0]: # Apabila username yang diinput oleh user ada di database users
                if users [i][2] == "jin_pengumpul": # Mengecek role user dengan username yang diinput oleh user
                    print("Jin ini bertipe “Pengumpul”. Yakin ingin mengubah ke tipe “Pembangun” (Y/N)? ", end="")
                    konfirmasi = input() # Meminta konfirmasi untuk mengubah jin dari user
                    if konfirmasi == "Y": # Apabila dikonfirmasi oleh user
                        users[i][2] = "jin_pembangun" # role user tersebut akan diganti menjadi jin_pembangun
                        print("\nJin telah berhasil diubah")
                    else: # Apabila tidak dikonfirmasi oleh user (user memasukkan N atau huruf lainnya)
                        print("\nJin tidak jadi diubah") 
                    return(users) # Mengembalikan data users
                else: # apabila role user merupakan jin_pembangun
                    print("Jin ini bertipe “Pembangun”. Yakin ingin mengubah ke tipe “Pengumpul” (Y/N)? ", end="")
                    konfirmasi = input() # Meminta konfirmasi untuk mengubah jin dari user
                    if konfirmasi == "Y": # Apabila dikonfirmasi oleh user
                        users[i][2] = "jin_pengumpul" # role user tersebut akan diganti menjadi jin_pengumpul
                        print("\nJin telah berhasil diubah") 
                    else: # Apabila tidak dikonfirmasi oleh user (user memasukkan N atau huruf lainnya)
                        print("\nJin tidak jadi diubah")
                    return(users) # Mengembalikan data users
        print("\nTidak ada jin dengan username tersebut.") # Apabila setelah dicek pada seluruh data di database users, username yang diinput tidak ditemukan
        return(users)  # Mengembalikan data users yang tidak diubah
    else: # Pesan error apabila fungsi ini dipanggil oleh user yang tidak memiliki role sebagai Bandung Bondowoso
        print("Command “ubahjin” hanya bisa dipanggil oleh Bandung Bondowoso!")
        return(users) # Mengembalikan data users yang tidak diubah