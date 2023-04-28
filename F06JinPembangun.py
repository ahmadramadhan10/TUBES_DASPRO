import random

def bangun(bahan, candi, jumlahcandi, current_login, users):
    if users[current_login][2] == "jin_pembangun":
        sisa_candi = sisa(candi, jumlahcandi)
        pasir = int(random.uniform(1,5))
        batu = int(random.uniform(1,5))
        air = int(random.uniform(1,5))
        if bahan[0] >= pasir and bahan[1] >= batu and bahan[2] >= air:
            bahan[0] = bahan[0] - pasir
            bahan[1] = bahan[1] - batu
            bahan[2] = bahan[2] - air
            if sisa_candi != 0:
                sisa_candi = sisa_candi - 1
            for i in range(jumlahcandi):
                if candi[i][0] == "":
                    candi[i][0] = users[current_login][0]
                    candi[i][1] = pasir
                    candi[i][2] = batu
                    candi[i][3] = air
                    break
            print('Candi berhasil dibangun.')
            print(f'Sisa candi yang perlu dibangun: {sisa_candi}.')
        else:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
    else:
        print("Command “bangun” hanya bisa dipanggil oleh user dengan role Jin Pembangun!")
    return (bahan, candi)

def sisa (candi,jumlahcandi):
    sisacandi = 0
    for i in range(jumlahcandi):
        if candi[i][0] == "":
            sisacandi += 1
    return(sisacandi)