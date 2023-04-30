# procedure ambilLaporanJin (input jumlahusers : integer, input users : matriksusers, input bahan : matriksbahan, input candi : matrikscandi, input current_login : integer, input jumlahcandi : integer
# I.S. = Terdapat jumlahusers, users, bahan, candi, current_login, dan jumlahcandi yang sudah terdefinisi }
# F.S. = Menampilkan data berupa total jin, total jin pengumpul, total jin pembangun, jin terajin, jin termalas, jumlah pasir yang tersedia, jumlah air yang tersedia, dan jumlah batu yang tersedia pada layar 

def ambilLaporanJin(jumlahusers, users, bahan, candi, current_login, jumlahcandi):
    # KAMUS LOKAL
    # cntJin, cntPengumpul, cntPembangun, maxcandi, mincandi,        pasir, air, batu, I : integer
    # dataJin : array [“ “,0] of array[1..jumlahcandi] of integer
    # terajin, termalas : string
    if current_login == 0: # Jika yang mengakses fungsi ini adalah Bandung Bondowoso
        # untuk total jin
        cntJin = 0 # Count awal untuk jumlah jin
        cntPengumpul = 0
        cntPembangun = 0
        for i in range(jumlahusers): # Melakukan looping sebanyak jumlah users
            if users[i][2] == 'jin_pengumpul': # Jika users memiliki role sebagai jin pengumpul
                cntJin += 1 # Counter jin bertambah 1
                cntPengumpul += 1 # Counter jin pengumpul bertambah 1
            elif users[i][2] == 'jin_pembangun': # Jika users memiliki role sebagai jin pembangun
                cntJin += 1 # Counter jin bertambah 1
                cntPembangun += 1 # Counter jin pembangun bertambah 1

        #untuk jin terajin, termalas
        dataJin = [["",0]for i in range(jumlahcandi)] # Membuat matriks baru untukmenghitung banyaknya candi yang telah dibuat oleh jin, dengan kolom pertama berisi username jin, dan kolom kedua berisi jumlah candi yang telah dibuat
        x = 0
        for i in range(jumlahcandi): # melakukan looping sebanyak jumlah candi
            if candi[i][0] != "": # jika data candi tidak kosong (sudah ada pembangunan candi)
                dataJin[i-x][0] = candi[i][0] # men-copy data pada data candi ke datajin
                dataJin[i-x][1] = 1 # jumlah candi yang dibuatnya 1
                for j in range (jumlahcandi-(jumlahcandi-i-1),jumlahcandi):
                    if candi[j][0] == dataJin[i-x][0]: # jika username jin pada data candi sudah ada pada datajin
                        dataJin[i-x][1] += 1 # datajin yang berisi username jin tersebut, jumlah candi yang dibuat bertambah 1
                        candi[j][0] = '' # data user jin tersebut dihapus dari data candi
                        candi[j][1] = 0
                        candi[j][2] = 0
                        candi[j][3] = 0
            else:
                x += 1
        maxcandi = dataJin[0][1] # Set nilai maksimum awal
        mincandi = dataJin[0][1] # Set nilai minimum awal
        terajin = dataJin[0][0] # Pembanding username jin terajin
        termalas = dataJin[0][0] # Pembanding username jin termalas
        for i in range(1,jumlahcandi): # Melakukan looping mulai dari baris kedua sebanyak jumlah candi
            if dataJin[i][0] == "": # Jika baris pada kolom username sudah kosong
                break # Loop berhenti
            else:
                if dataJin[i][1] > maxcandi: # Jika ada jumlah yang lebih besar dari maxcandi (yang sudah di set di awal)
                    if (dataJin[i][1] == maxcandi and dataJin[i][0] > terajin) or dataJin[i][1] > maxcandi: # jika jumlah candi pada baris ke i sama dengan nilai maxcandi dan leksikografis jin lebih besar dari set jin terajin
                        maxcandi = dataJin[i][1] # maxcandi bernilai sama
                        terajin = dataJin[i][0] # jin terajin yang urutan leksikografisnya lebih kecil
                if dataJin[i][1] <= mincandi: #  jika jumlah candi lebih sedikit dibandingkan dengan nilai yang sudah di set di awal
                    if (dataJin[i][1] == mincandi and dataJin[i][0] < termalas) or dataJin[i][1] < mincandi: # jika jumlah candi pada baris ke i sama dengan nilai mincandi dan memiliki urutan leksikografis lebih kecil dibanding dengan jintermalad yang sudah di set
                        mincandi = dataJin[i][1] # mincandi bernilai sama
                        termalas = dataJin[i][0] # jin termalas menjadi yang urutan leksikografisnya lebih besar
                            
        #untuk bahan
        pasir = bahan[0][2] # akses jumlah pasir dari matriks bahan baris 1
        batu = bahan[1][2] # akses jumlah batu dari matriks bahan baris 2
        air = bahan[2][2] # akses jumlah air dari matriks bahan baris 3
        print(f'> Total Jin: {cntJin}') # output countjin yang sudah terdefinisi di atas
        print(f'> Total Jin Pengumpul: {cntPengumpul}')
        print(f'> Total Jin Pembangun: {cntPembangun}')
        if dataJin[0][0] == "": # jika belum ada jin yang membangun candi
            print(f'> Jin Terajin : -') # tidak ada jin termalas dan terajin
            print(f'> Jin Termalas: -')
        else: # jika sudah ada yang membangun candi
            print(f'> Jin Terajin : {terajin}') # ada jin terajin dan termalas
            print(f'> Jin Termalas: {termalas}')
        print(f'> Jumlah Pasir: {pasir} unit') # output bahan-bahan
        print(f'> Jumlah Air: {air} unit')
        print(f'> Jumlah Batu: {batu} unit')
    else: # jika yang memanggil fungsi bukan Bandung Bondowoso
        print('Command “laporanjin” hanya bisa dipanggil oleh Bandung Bondowoso!') 




