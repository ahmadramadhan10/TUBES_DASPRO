def CekSize(users):
    cnt = 0
    found = False
    for i in range(102):
        if users[i] == ["","",""]:
            return cnt
        else:   
            cnt = cnt + 1
    return cnt

def CekUser(users, nama_jin):
    for i in range(100):
        if users[i][0] == nama_jin :
            return True
    return False

def Summon(users):
    current_jin = ["", "", ""]
    mark = CekSize(users)
    if mark == 100:
        print(f'Jumlah jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu')
        return users

    print("Jenis jin yang dapat dipanggil:")
    print(" (1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print(" (2) Pembangun - Bertugas membangun candi")
    print("")
    jenis = -1
    while jenis != 1 and jenis != 2:
        jenis = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        print("")
        if jenis != 1 and jenis != 2:
            print(f'Tidak ada jenis jin bernomor "{jenis}"!')
            print("")
    
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
            print(f'Username "{nama_jin}" sudah diambil!')
            print("")
        else:
            current_jin[0] = nama_jin

    valid_pass = False
    while not valid_pass:
        password = input("Masukkan password jin: ")
        valid_pass = 5 <= len(password) and len(password) <= 25
        if not valid_pass:
            print(f'Password panjangnya harus 5-25 karakter!')
            print("")
        else:
            current_jin[1] = password
    print("")
    print("Mengumpulkan sesajen...")
    print("Menyerahkan sesajen...")
    print("Membacakan mantra...")
    print("")
    print(f"Jin {current_jin[0]} berhasil dipanggil!")
    users[mark] = current_jin
    return users

users = [["","",""]]*102
users[0] = ["jin1", "jinsatu", "jin_pengumpul"]
users[1] = ["jin_kuli", "kulisejati", "jin_pembangun"]
users = Summon(users)
print(users[:CekSize(users)])