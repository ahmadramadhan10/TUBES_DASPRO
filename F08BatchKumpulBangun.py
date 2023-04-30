# Program Batch Kumpul/Bangun
# I.S. = Bandung Bondowoso memnanggil jin pengumpul atau jin pembangun
# F.S. = Jin melakukan sesuai dengan perintah, entah itu mengumpulkan bahan secara random atau membangun candi

# KAMUS LOKAL
# pasir, batu, air, KurangPasir, KurangBatu, KurangAir, jumlahJin: integer 
# totalpasir, totalbatu, totalair : integer
# perintah : string
# Candireverse: matriks of Candi Reverse

# random berguna untuk me-random banyaknya pasir, air, batu
from random import randint 

# Fungsi BatchKumpulBangun berguna untuk Bandung Bondowoso apakah jin akan mengumpulkan atau membangun
def BatchKumpulBangun (perintah, users, jumlahusers, bahan, candi, jumlahcandi, current_login):
    if (perintah == "batchkumpul"): # Jika yang dipanggil Jin Pengumpul
        if current_login != 0: # Pemanggilan jin hanya bisa diakses oleh Bandung Bondowoso
            print("Command “batchkumpul” hanya bisa dipanggil oleh Bandung Bondowoso!")
            return(bahan, candi)
        
        # Pemanggilan fungsi batchkumpul untuk mengumpulkan batu, air, dan pasir secara random
        # Kemudian dimasukan ke dalam variabel
        jumlahJin, bahan, pasir, batu, air = batchKumpul(users, jumlahusers, bahan)

        if (jumlahJin > 0): # Jika jumlah jin lebih dari 0, fungsi baru bisa berjalan
            print(f"Mengerahkan {jumlahJin} jin untuk mengumpulkan bahan.")
            print(f"Jin menemukan total {pasir} pasir, {batu} batu, dan {air} air.")
        else: # Jin kurang atau sama dengan 0, fungsi gagal dijalankan
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")

    elif (perintah == "batchbangun"): # Jika yang dipanggil adalah jin pembangun
        if current_login != 0: # Pemanggilan jin hanya bisa dipanggil oleh Bandung Bondowoso
            print("Command “batchbangun” hanya bisa dipanggil oleh Bandung Bondowoso!")
            return(bahan, candi)
        
        # Pemanggilan fungsi batchbangun untuk mengetahui batu, air, dan pasir yang dibutuhkan untuk membangun candi (total bahan)
        jumlahJin, pasir, batu, air, candi, KurangPasir, KurangBatu, KurangAir = batchBangun(users, jumlahusers, candi, jumlahcandi, bahan)

        if (jumlahJin > 0): # Jika jumlah jin lebih dari 0, fungsi baru bisa berjalan
            print (f"Mengerahkan {jumlahJin} jin untuk membangun candi dengan total bahan {bahan[0]} pasir, {bahan[1]} batu, dan {bahan[2]} air.")

            # Jika tidak ada bahan yang kurang fungsi baru bisa dijalankan
            if (KurangPasir <= 0) and (KurangBatu <= 0) and (KurangAir <= 0):
                bahan[0] -= pasir
                bahan[1] -= batu
                bahan[2] -= air
                print ("Jin berhasil membangun total " + str(jumlahJin) + " candi.")
            else: # Jika bahan yang tersedia kurang dari seharusnya
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
        else: # Jika jin yang dipanggil kurang dari 0, fungsi tidak dapat berjalan
            print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    return(bahan, candi)

# Fungsi untuk memanggil jin pengumpul
def batchKumpul(users, jumlahusers, bahan):
    # Inisiasi jumlah awal jin, pasir, batu, dan air 
    jumlahJin = 0
    pasir = 0
    batu = 0
    air = 0
    # Menggunakan loop untuk mencari tau berapa jumlah jin dan bahan total
    for i in range(2,jumlahusers):
        if users[i][2] == "jin_pengumpul":
            jumlahJin += 1
            pasir += randint(0,5)
            batu += randint(0,5)
            air += randint(0,5)

    # Kemudian semua bahan yang ada dimasukan kedalam sebuah matriks
    bahan[0] += pasir
    bahan[1] += batu
    bahan[2] += air
    return(jumlahJin, bahan, pasir, batu, air)

# Fungsi untuk memanggil jin pembangun
def batchBangun (users, jumlahusers, candi, jumlahcandi, bahan):
    # Inisiasi awal bentuk dan panjang matriks
    candireverse= [["",0,0,0]for j in range(100)]

    for i in range (jumlahcandi):
        for j in range(4):
            candireverse[i][j] = candi[i][j]

    # Inisiasi awal jumlah jin, pasir, batu, dan air
    jumlahJin = 0
    totalpasir = 0
    totalbatu = 0
    totalair = 0
    # Menggunakan loop untuk mencari tau jumlah jin dan jumlah bahan yang diperlukan
    for i in range(2,jumlahusers):
        if users[i][2] == "jin_pembangun":
            jumlahJin += 1
            pasir = randint(1,5)
            batu = randint(1,5)
            air = randint(1,5)
            # Kemudian jin, pasir, batu, air dimasukan ke dalam matriks candi
            # Satu baris j candi membutuhkan berapa pasir, batu, dan air
            for j in range (jumlahcandi):
                if candi[j][0] == "":
                    candi [j][0] = users[i][0]
                    candi [j][1] = pasir
                    candi [j][2] = batu
                    candi [j][3] = air
                    break
            # Menghitung total pasir yang dibutuhkan
            totalpasir += pasir
            totalbatu += batu
            totalair += air
    # Menghitung kekurangan bahan untuk membangun candi
    KurangPasir = totalpasir - bahan[0]
    KurangBatu = totalbatu - bahan[1]
    KurangAir = totalair - bahan[2]

    if (KurangPasir <= 0) and (KurangBatu <= 0) and (KurangAir <= 0): # Jika tidak ada yang kurang
        return(jumlahJin, totalpasir, totalbatu, totalair, candi, KurangPasir, KurangBatu, KurangAir)
    else: # Jika bahan kurang
        return(jumlahJin, totalpasir, totalbatu, totalair, candireverse, KurangPasir, KurangBatu, KurangAir)