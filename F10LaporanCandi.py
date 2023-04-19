def laporanCandi(jumlahcandi, candi, current_login):
    if current_login == 0:
        totalcandi = 0
        totalpasir = 0
        totalbatu = 0
        totalair = 0
        hargacanditermurah = hargacandi(candi[0][1],candi[0][2],candi[0][3])
        hargacanditermahal = hargacandi(candi[0][1],candi[0][2],candi[0][3])
        idcanditermurah = 0
        idcanditermahal = 0

        for i in range (jumlahcandi):
            if candi[i][0] != "":
                totalcandi += 1
                totalpasir += candi[i][1]
                totalbatu  += candi[i][2]
                totalair   += candi [i][3]
                if hargacandi(candi[i][1],candi[i][2],candi[i][3]) > hargacanditermahal:
                    hargacanditermahal = hargacandi(candi[i][1],candi[i][2],candi[i][3])
                    idcanditermahal = i
                if hargacandi(candi[i][1],candi[i][2],candi[i][3]) < hargacanditermurah:
                    hargacanditermurah = hargacandi(candi[i][1],candi[i][2],candi[i][3])
                    idcanditermurah = i

        print("> Total Candi:", totalcandi)
        print("> Total Pasir yang digunakan:", totalpasir)
        print("> Total Batu yang digunakan:", totalbatu)
        print("> Total Air yang digunakan:", totalair)
        print("> ID Candi Termahal:", idcanditermahal, "(Rp",pengubahformatharga(hargacanditermahal) + ")")
        print("> ID Candi Termurah:", idcanditermurah, "(Rp",pengubahformatharga(hargacanditermurah) + ")")
    else:
        print("Command “laporancandi” hanya bisa dipanggil oleh Bandung Bondowoso!")

def hargacandi(pasir, batu, air):
    return(int(pasir)*10000 + int(batu)*15000 + int(air)*7500)

def pengubahformatharga(harga):
    # Asumsi harga tidak lebih dari Rp16.250.000 (maksimal jumlah candi 100)
    if harga < 1000:
        return(harga)
    elif harga < 1000000:
        return str(harga // 1000) + "." + str(harga%1000)
    else:
        return str(harga // 1000000) + "." + str((harga//1000)%1000) + "." + str(harga % 1000)

"""
candi = [["jinb1",0,0,1],["jinb2",1,2,1]]
jumlahcandi = 2
current_login = 0

laporanCandi(jumlahcandi, candi, current_login)
"""