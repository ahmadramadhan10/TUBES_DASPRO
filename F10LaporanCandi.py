# procedure laporanCandi (input jumlahcandi : integer, input candi : matrikscandi, input current_login : integer)
# I.S. Terdapat jumlahcandi, candi, dan current_login yang sudah terdefinisi
# F.S. Menampilkan data berupa total candi, total pasir yang digunakan, total batu yang digunakan, total air yang digunakan, id candi termahal, dan id candi termurah pada layar.         

def laporanCandi(jumlahcandi, candi, current_login):
    # KAMUS LOKAL
    # totalcandi, totalpasir, totalbatu, totalair, hargacanditermurah, hargacanditermahal, idcanditermurah, idcanditermahal, i : integer
    # candipunyaisi : boolean
    # function hargacandi (pasir : integer, batu : integer, air : integer) -> integer
    #    { Function hargacandi akan mengembalikan total harga candi berdasarkan masukan pasir, batu, dan air yang digunakan untuk membuat candi tersebut }
    # function pengubahformatharga (harga : integer) -> string
    #    { Function pengubahformatharga akan mengubah masukan harga menjadi string harga dengan menambahkan Rp dan “.” apabila diperlukan }

    # ALGORITMA
    if current_login == 0: # Mengecek apakah user yang memangil prosedur ini memiliki role sebagai Bandung Bondowoso
        totalcandi = 0 # Merepresentasikan total candi yang sudah dibuat
        totalpasir = 0 # Merepresentasikan total pasir yang digunakan untuk membuat seluruh candi
        totalbatu = 0 # Merepresentasikan total batu yang digunakan untuk membuat seluruh candi
        totalair = 0 # Merepresentasikan total air yang digunakan untuk membuat seluruh candi
        hargacanditermurah = hargacandi(candi[0][1],candi[0][2],candi[0][3]) # Inisialisasi harga candi yang paling murah dengan candi pertama yang ada di data candi
        hargacanditermahal = hargacandi(candi[0][1],candi[0][2],candi[0][3]) # Inisialisasi harga candi yang paling mahal dengan candi pertama yang ada di data candi
        idcanditermurah = 0 # Inisialisasi candi termurah dengan candi pertama yang ada di data candi
        idcanditermahal = 0 # Inisialisasi candi termahal dengan candi pertama yang ada di data candi

        candipunyaisi = False # Menganggap data candi kosong

        for i in range (jumlahcandi): # Mengecek isi data candi
            if candi[i][0] != "": # Apabila candi ada (tidak kosong, ditandai dengan data yang != string kosong)
                candipunyaisi = True # Candi yang sudah dibuat >= 1
                totalcandi += 1 
                totalpasir += candi[i][1] 
                totalbatu  += candi[i][2]
                totalair   += candi [i][3]
                if hargacandi(candi[i][1],candi[i][2],candi[i][3]) > hargacanditermahal: # Apabila harga candi termahal saat iterasi < harga candi yang sedang dicek
                    hargacanditermahal = hargacandi(candi[i][1],candi[i][2],candi[i][3]) # Mengubah harga candi termahal dengan harga candi yang sedang dicek
                    idcanditermahal = str(i) # Mengubah indeks candi termahal dengan pencacah
                if hargacandi(candi[i][1],candi[i][2],candi[i][3]) < hargacanditermurah: # Apabila harga candi termurah saat iterasi > harga candi yang sedang dicek
                    hargacanditermurah = hargacandi(candi[i][1],candi[i][2],candi[i][3]) # Mengubah harga candi termurah dengan harga candi yang sedang dicek
                    idcanditermurah = str(i) # Mengubah indeks candi termurah dengan pencacah

        print("> Total Candi:", totalcandi)
        print("> Total Pasir yang digunakan:", totalpasir)
        print("> Total Batu yang digunakan:", totalbatu)
        print("> Total Air yang digunakan:", totalair)

        if candipunyaisi == False: # Apabila tidak ada candi yang sudah dibuat
            print("> ID Candi Termahal: -")
            print("> ID Candi Termurah: -")
        else: # Apabila candi yang sudah dibuat >= 1
            print("> ID Candi Termahal:", idcanditermahal, "(Rp",pengubahformatharga(hargacanditermahal) + ")")
            print("> ID Candi Termurah:", idcanditermurah, "(Rp",pengubahformatharga(hargacanditermurah) + ")")
    else: # Apabila prosedur ini dipanggil oleh user yang tidak memiliki role sebagai Bandung Bondowoso
        print("Command “laporancandi” hanya bisa dipanggil oleh Bandung Bondowoso!")


# function hargacandi (pasir : integer, batu : integer, air : integer) -> integer
#    { Function hargacandi akan mengembalikan total harga candi berdasarkan masukan pasir, batu, dan air yang digunakan untuk membuat candi tersebut }

def hargacandi(pasir, batu, air):
    # KAMUS LOKAL

    # ALGORITMA
    return(int(pasir)*10000 + int(batu)*15000 + int(air)*7500) # Mengembalikan total harga candi


# function pengubahformatharga (harga : integer) -> string
#    { Function pengubahformatharga akan mengubah masukan harga menjadi string harga dengan menambahkan Rp dan “.” apabila diperlukan }

def pengubahformatharga(harga):
    # KAMUS LOKAL
    # stringharga, formatharga : string
    # angka, a, i : integer
    # function len (kata : string) -> string
    #     { Function len menghitung berapa berapa banyak huruf atau character pada kata }
    # function str (angka : integer) -> string
    #     { Function str mengubah masukan integer menjadi sebuah string}

    # ALGORITMA
    stringharga = str(harga) # Mengubah type data integer menjadi string
    angka = len(stringharga) # Menghitung panjang string
    formatharga = "" # Inisialisasi formatharga dengan string kosong (formatharga adalah keluaran yang diinginkan)
    a = 1 # Menunjukkan sudah berapa kali melakukan iterasi
    for i in range (angka-1,-1,-1): # Mencacah dari belakang
        formatharga = str(stringharga[i]) + formatharga # Menambahkan angka demi angka ke string formatharga
        if a % 3 == 0 and i != 0: # Apabila iterasi kelipatan 3
            formatharga = "." + formatharga # Menambahkan titik
        a+=1
    return(formatharga) # Mengembalikan string formatharga yang sudah sesuai dengan format keluargan yang diinginkan