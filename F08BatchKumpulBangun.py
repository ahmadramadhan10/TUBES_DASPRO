# Program Batch Kumpul/Bangun
# Mengumpulkan Bahan dan Membuat Candi berdasarkan Bahan Yang Ada

from random import randint

def BatchKumpulBangun (perintah, users, jumlahusers, bahan, candi, jumlahcandi, current_login):
    if (perintah == "batchkumpul"):
        if current_login != 0:
            "Command “batchkumpul” hanya bisa dipanggil oleh Bandung Bondowoso!"
            return(bahan, candi)
        jumlahJin, bahan, pasir, batu, air = batchKumpul(users, jumlahusers, bahan)
        if (jumlahJin > 0):
            print(f"Mengerahkan {jumlahJin} jin untuk mengumpulkan bahan.")
            print(f"Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air.")
        else:
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    elif (perintah == "batchbangun"):
        if current_login != 0:
            "Command “batchbangun” hanya bisa dipanggil oleh Bandung Bondowoso!"
            return(bahan, candi)
        jumlahJin, pasir, batu, air, candi, KurangPasir, KurangBatu, KurangAir = batchBangun(users, jumlahusers, candi, jumlahcandi, bahan)

        if (jumlahJin > 0):
            print (f"Mengerahkan {jumlahJin} jin untuk membangun candi dengan total bahan {bahan[0]} pasir, {bahan[1]} batu, dan {bahan[2]} air.")

            if (KurangPasir <= 0) and (KurangBatu <= 0) and (KurangAir <= 0):
                bahan[0] -= pasir
                bahan[1] -= batu
                bahan[2] -= air
                print ("Jin berhasil membangun total " + str(jumlahJin) + " candi.")
            else:
                print(f"Bangun gagal. Kurang ", end="")
                if KurangPasir > 0 and KurangBatu > 0 and KurangPasir > 0:
                    print(f"{KurangPasir} pasir, {KurangBatu} batu, dan {KurangAir} air.")
                elif KurangPasir > 0 and KurangBatu > 0:
                    print(f"{KurangPasir} pasir, dan {KurangBatu} batu.")
                elif KurangPasir > 0 and KurangBatu > 0:
                    print(f"{KurangPasir} pasir, dan {KurangBatu} batu.")
                elif KurangBatu > 0 and KurangAir > 0:
                    print(f"{KurangBatu} batu, dan {KurangAir} air.")
                elif KurangBatu > 0:
                    print(f"{KurangBatu} batu.")
                elif KurangPasir > 0:
                    print(f"{KurangPasir} pasir.")
                else:
                    print(f"{KurangAir} air.")
        else:
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    return(bahan, candi)

def batchKumpul(users, jumlahusers, bahan):
    jumlahJin = 0
    pasir = 0
    batu = 0
    air = 0
    for i in range(2,jumlahusers):
        if users[i][2] == "jin_pengumpul":
            jumlahJin += 1
            pasir += randint(0,5)
            batu += randint(0,5)
            air += randint(0,5)
    bahan[0] += pasir
    bahan[1] += batu
    bahan[2] += air
    return(jumlahJin, bahan, pasir, batu, air)

def batchBangun (users, jumlahusers, candi, jumlahcandi, bahan):

    candireverse= [["",0,0,0]for j in range(100)]

    for i in range (jumlahcandi):
        for j in range(4):
            candireverse[i][j] = candi[i][j]

    jumlahJin = 0
    totalpasir = 0
    totalbatu = 0
    totalair = 0
    for i in range(2,jumlahusers):
        if users[i][2] == "jin_pembangun":
            jumlahJin += 1
            pasir = randint(1,5)
            batu = randint(1,5)
            air = randint(1,5)
            print(pasir,batu,air)
            for j in range (jumlahcandi):
                if candi[j][0] == "":
                    candi [j][0] = users[i][0]
                    candi [j][1] = pasir
                    candi [j][2] = batu
                    candi [j][3] = air
                    break
            totalpasir += pasir
            totalbatu += batu
            totalair += air
    KurangPasir = totalpasir - bahan[0]
    KurangBatu = totalbatu - bahan[1]
    KurangAir = totalair - bahan[2]
    if (KurangPasir <= 0) and (KurangBatu <= 0) and (KurangAir <= 0):
        return(jumlahJin, totalpasir, totalbatu, totalair, candi, KurangPasir, KurangBatu, KurangAir)
    else:
        return(jumlahJin, totalpasir, totalbatu, totalair, candireverse, KurangPasir, KurangBatu, KurangAir)

    

users = [["" for i in range(3)]for j in range(5)]
users[0] = ["bandung","cintaroro","bandung_bondowoso"]
users[1] = ["roro","gasukabondo","roro_jonggrang"]
users[2] = ["test","test","jin_pengumpul"]
users[3] = ["test2","test2","jin_pembangun"]
users[4] = ["test3","test3","jin_pembangun"]

jumlahusers = 5

bahan = [10,10,10]

perintah = "batchbangun"

jumlahcandi = 100

candi = [["",0,0,0]for j in range(jumlahcandi)]

candi[0] = ["ada",1,1,1]
candi [2] = ["ada",1,1,1]

current_login = 0

bahan, candi = BatchKumpulBangun(perintah, users, jumlahusers, bahan, candi, jumlahcandi, current_login)

print(bahan)
print(candi)