def CekSize(users): # mengembalikan nilai banyaknya jin di users
    # KAMUS
    # cnt : integer
    cnt = 0 # inisiasi variable untuk menghitung
    for i in range(102):
        if users[i][2] == "jin_pengumpul" or users[i][2] == "jin_pembangun": # cek jika user ke i adalah jin
            cnt = cnt + 1 # tambah nilainya
    return cnt 

def CekUser(users, nama_jin):
    for i in range(2,102):
        if users[i][0] == nama_jin and (users[i][2] == "jin_pembangun" or users[i][2] == "jin_pengumpul"):
            # cek nama jin di users, apakah sudah ada jin yang memiliki username yang sama atau tidak
            # jika ada maka return true
            return True
    return False # jika tidak ada maka return false

def Summon(users, current_login): # fungsi untuk mensummon jin
    if current_login == 0: # cek jika yang sekarang login adalah bandung bondowoso
        # KAMUS
        # current_jin : array of string
        # mark : integer
        # jenis : string
        # exist, valid_password : boolean
        current_jin = ["", "", ""]
        mark = CekSize(users)
        if mark == 100: # cek apakah total jin sudah sampai 100, jika iya maka tidak bisa mensummon
            print(f'Jumlah jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
            return users 

        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi\n")
        jenis = "" # inisiasi nilai jenis
        while jenis != "1" and jenis != "2": # selama belum valid maka akan meminta input sampai input antara 1 atau 2
            jenis = input("Masukkan nomor jenis jin yang ingin dipanggil: ")
            print("")
            if jenis != "1" and jenis != "2":
                print(f'Tidak ada jenis jin bernomor "{jenis}"!\n')
        
        if jenis == "1": # jika jenis == "1" maka yang disummon jin pengumpul
            print(f'Memilih jin "Pengumpul".')
            current_jin[2] = "jin_pengumpul"
        else: # selain itu berarti dia jin pembangun
            print(f'Memilih jin "Pembangun".')
            current_jin[2] = "jin_pembangun"
        print('')


        exist = True
        while exist: # selama username telah dipakai maka akan selalu minta username yang unique
            nama_jin = input("Masukkan username jin: ")
            exist = CekUser(users,nama_jin)
            if exist: # jika masih ada maka akan terus meminta
                print(f'Username "{nama_jin}" sudah diambil!\n')
            else:
                current_jin[0] = nama_jin

        valid_password = False 
        while not valid_password: # selama belum valid maka akan selalu meminta password yang valid
            password = input("Masukkan password jin: ")
            # password yang valid memiliki panjang char 5 - 25
            valid_password = 5 <= len(password) and len(password) <= 25
            if not valid_password:
                print(f'Password panjangnya harus 5-25 karakter!\n')
            else:
                current_jin[1] = password

        # melakukan ritual pemanggilan
        print("\nMengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...\n")
        print(f"Jin {current_jin[0]} berhasil dipanggil!")
        
        for i in range (102):
            if users[i][0]=="": # jika user sekarang kosong maka isi dengan jin yang barusan disummon
                users[i] = current_jin
                break
        return users
    else: # jika yang login sekarang bukan bandung bondowoso maka tidak bisa mensummon
        print("Command “summonjin” hanya bisa dipanggil oleh Bandung Bondowoso!")
        return users