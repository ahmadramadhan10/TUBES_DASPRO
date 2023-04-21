def ambilLaporanJin(jumlahusers, users, bahan, candi, current_login, jumlahcandi):
    if current_login == 0:
        #untuk total jin
        cntJin = 0
        cntPengumpul = 0
        cntPembangun = 0
        for i in range(jumlahusers):
            if users[i][2] == 'jin_pengumpul':
                cntJin += 1
                cntPengumpul += 1
            elif users[i][2] == 'jin_pembangun':
                cntJin += 1
                cntPembangun += 1
        #untuk jin terajin, termalas
        dataJin = [["",0]for i in range(jumlahcandi)]
        x = 0
        for i in range(jumlahcandi):
            if candi[i][0] != "":
                dataJin[i-x][0] = candi[i][0] 
                dataJin[i-x][1] = 1
                for j in range (jumlahcandi-(jumlahcandi-i-1),jumlahcandi):
                    if candi[j][0] == dataJin[i-x][0]:
                        dataJin[i-x][1] += 1
                        candi[j][0] = ''
                        candi[j][1] = 0
                        candi[j][2] = 0
                        candi[j][3] = 0
            else:
                x += 1
        maxcandi = dataJin[0][1]
        mincandi = dataJin[0][1]
        terajin = dataJin[0][0]
        termalas = dataJin[0][0]
        for i in range(1,jumlahcandi):
            if dataJin[i][0] == "":
                break
            else:
                if dataJin[i][1] > maxcandi:
                    if (dataJin[i][1] == maxcandi and dataJin[i][0] > terajin) or dataJin[i][1] > maxcandi:
                        maxcandi = dataJin[i][1]
                        terajin = dataJin[i][0]
                if dataJin[i][1] <= mincandi:
                    if (dataJin[i][1] == mincandi and dataJin[i][0] < termalas) or dataJin[i][1] < mincandi:
                        mincandi = dataJin[i][1]
                        termalas = dataJin[i][0]
                            
        #untuk bahan
        pasir = bahan[0]
        batu = bahan[1]
        air = bahan[2]
        print(f'> Total Jin: {cntJin}')
        print(f'> Total Jin Pengumpul: {cntPengumpul}')
        print(f'> Total Jin Pembangun: {cntPembangun}')
        if dataJin[0][0] == "":
            print(f'> Jin Terajin : -')
            print(f'> Jin Termalas: -')
        else:
            print(f'> Jin Terajin : {terajin}')
            print(f'> Jin Termalas: {termalas}')
        print(f'> Jumlah Pasir: {pasir} unit')
        print(f'> Jumlah Batu: {batu} unit')
        print(f'> Jumlah Air: {air} unit')
    else:
        print('\nCommand “laporanjin” hanya bisa dipanggil oleh Bandung Bondowoso!')
        
# jumlahusers = 2
# current_login = 1
# jumlahcandi = 11
# current_login = 0

# users = [["test","test","jin_pengumpul"],["jinb2","1","jin_pembangun"]]
# bahan = [['pasir', 'apakek', 50], ['batu', 'terserah', 30], ['air', 'cair', 29]]
# candi = [['Aku',1,2,3],
#          ['Aku',1,2,3],
#          ['Aku',1,2,3],
#          ['saya',1,2,3],
#          ['saya',1,2,3],
#          ['saya',1,2,3],
#          ['guwe',1,2,3],
#          ['aku',1,2,3],
#          ['aku',1,2,3],
#          ['aku',1,2,3],
#          ['ak',1,2,3]]

# ambilLaporanJin(jumlahusers, users, bahan, candi, current_login, jumlahcandi)




