import random

def bangun(bahan, candi, jumlahcandi, current_login, users):
    if users[current_login][2] == "jin_pembangun":
        sisa_candi = sisa(candi, jumlahcandi) # mencari sisa candi yang ada
        pasir = int(random.uniform(1,5)) # mengenerate pasir
        batu = int(random.uniform(1,5)) # mengenerate batu
        air = int(random.uniform(1,5)) # mengenerate air
        if bahan[0] >= pasir and bahan[1] >= batu and bahan[2] >= air: # cek apakah cukup bahan
            bahan[0] = bahan[0] - pasir
            bahan[1] = bahan[1] - batu
            bahan[2] = bahan[2] - air
            if sisa_candi != 0: # jika candi yang dibangun sudah 100 atau lebih
                sisa_candi = sisa_candi - 1
            for i in range(jumlahcandi): # mencari slot kosong pada array candi
                if candi[i][0] == "":
                    candi[i][0] = users[current_login][0]
                    candi[i][1] = pasir
                    candi[i][2] = batu
                    candi[i][3] = air
                    break
            print('Candi berhasil dibangun.')
            print(f'Sisa candi yang perlu dibangun: {sisa_candi}.')
        else: # jika bahan tidak cukup candi tidak dibangun
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
    else: # user yang login sekarang bukan jin pembangun
        print("Command “bangun” hanya bisa dipanggil oleh user dengan role Jin Pembangun!")
    return (bahan, candi) # mengembalikan nilai bahan dan candi

def sisa (candi,jumlahcandi):
    sisacandi = 0 # inisiasi nilai sisacandi
    for i in range(jumlahcandi):
        if candi[i][0] == "": # jika sekarang candi kosong, maka ditambah
            sisacandi += 1
    return(sisacandi) # kembalikan nilai candi