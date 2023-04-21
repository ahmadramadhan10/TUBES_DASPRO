def hilangkanJin (jumlahusers, users, jumlahcandi, candi, current_login):
    if current_login == 0:
        username = input('Masukkan username jin: ')
        for i in range (jumlahusers):
            if username == users [i] [0]:
                print(f'Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ',end="")
                konfirmasi = input()
                if konfirmasi == 'Y':
                    users [i] [0] = ''
                    users [i] [1] = ''
                    users [i] [2] = ''
                    for i in range (jumlahcandi):
                        if candi [i] [0] == username:
                            candi [i] [0] = ''
                            candi [i] [1] = ''
                            candi [i] [2] = ''
                            candi [i] [3] = ''
                    print('\nJin telah berhasil dihapus dari alam gaib.')
                    return(users, candi)
                else: #Konfirmasi N
                    print('\nJin tidak jadi dihapus')
                    return(users, candi)
        print('\nTidak ada jin dengan username tersebut')
        return(users, candi)
    else:
        print("\nCommand “hapusjin” hanya bisa dipanggil oleh Bandung Bondowoso!")
        return(users, candi)

# users = [["test","test","jin_pengumpul"],["jinb2","1","jin_pembangun"]]
# candi = [["jinb2",1,2,3],["jinb2",3,2,1]]
# jumlahusers = 2
# jumlahcandi = 2
# current_login = 0

# users, candi = hilangkanJin(jumlahusers, users, jumlahcandi, candi, current_login)

# print(users)
# print(candi)