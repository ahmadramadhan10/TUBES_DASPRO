def CekSize(users):
    cnt = 0
    for i in range(102):
        if users[i][2] == "jin_pengumpul" or users[i][2] == "jin_pembangun":
            cnt = cnt + 1
    return cnt

def CekUser(users, nama_jin):
    for i in range(2,102):
        if users[i][0] == nama_jin and (users[i][2] == "jin_pembangun" or users[i][2] == "jin_pengumpul"):
            return True
    return False

def Summon(users, current_login):
    if current_login == 0:
        current_jin = ["", "", ""]
        mark = CekSize(users)
        if mark == 100:
            print(f'Jumlah jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
            return users

        print("Jenis jin yang dapat dipanggil:")
        print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print(" (2) Pembangun - Bertugas membangun candi\n")
        jenis = -1
        while jenis != 1 and jenis != 2:
            jenis = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            print("")
            if jenis != 1 and jenis != 2:
                print(f'Tidak ada jenis jin bernomor "{jenis}"!\n')
        
        if jenis == 1:
            print(f'Memilih jin "Pengumpul".')
            current_jin[2] = "jin_pengumpul"
        else:
            print(f'Memilih jin "Pembangun".')
            current_jin[2] = "jin_pembangun"
        print('')


        exist = True
        while exist: # cek jika ada
            nama_jin = input("Masukkan username jin: ")
            exist = CekUser(users,nama_jin)
            if exist:
                print(f'Username "{nama_jin}" sudah diambil!\n')
            else:
                current_jin[0] = nama_jin

        valid_password = False
        while not valid_password:
            password = input("Masukkan password jin: ")
            valid_password = 5 <= len(password) and len(password) <= 25
            if not valid_password:
                print(f'Password panjangnya harus 5-25 karakter!\n')
            else:
                current_jin[1] = password
        print("\nMengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...\n")
        print(f"Jin {current_jin[0]} berhasil dipanggil!")
        users[mark] = current_jin
        return users
    else:
        print("Command “summonjin” hanya bisa dipanggil oleh Bandung Bondowoso!")
        return users