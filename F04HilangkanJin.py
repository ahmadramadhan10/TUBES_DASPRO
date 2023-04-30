#function hilangkanJin (jumlahusers : integer, users : matriksusers, jumlahcandi : integer, candi : matrikscandi, current_login : integer)-> matriksusers, matrikscandi
#Mengecek nilai current_login, kemudian menghapus jin dengan username yang diinputkan beserta candi yang dibuat, lalu mengembalikan matriksusers dan matrikscandi yang baru

def hilangkanJin (jumlahusers, users, jumlahcandi, candi, current_login):
    # KAMUS LOKAL
    # username, konfirmasi : string
    # i : integer
    if current_login == 0: # Jika yang emmanggil fungsi ini adalah Bandung Bondowoso
        username = input('Masukkan username jin: ') # Meminta username jin dari user
        for i in range (jumlahusers): # Melakukan looping sebanyak jumlah user
            if username == users [i] [0]: # Jika username jin valid
                print(f'Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ',end="") # Diminta konfirmasi
                konfirmasi = input() # Input konfirmasi
                if konfirmasi == 'Y': # Jika konfirmasi (Y) yaitu ingin menghapus
                    users [i] [0] = '' # Data jin yang dihapus menjadi kosong
                    users [i] [1] = ''
                    users [i] [2] = ''
                    for i in range (jumlahcandi):
                        if candi [i] [0] == username: # Mengecek username jin pada data candi
                            candi [i] [0] = ''  # Data candi dari jin yang ber-username tersebut menjadi kosong
                            candi [i] [1] = ''
                            candi [i] [2] = ''
                            candi [i] [3] = ''
                    print('\nJin telah berhasil dihapus dari alam gaib.') # Jin telah terhapus
                    return(users, candi)
                else: #Konfirmasi N
                    print('\nJin tidak jadi dihapus')
                    return(users, candi)
        print('\nTidak ada jin dengan username tersebut') # Apabila username jin tidak valid (tidak ada)
        return(users, candi)
    else:
        print("Command “hapusjin” hanya bisa dipanggil oleh Bandung Bondowoso!") # Apabila yang memanggil fungsi bukan Bandung Bondowoso
        return(users, candi)