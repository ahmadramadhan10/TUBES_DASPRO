# Program Ayam Berkokok
# I.S. = Roro Jonggrang memanggil fungsi ayam berkokok saat candi sedang dibangun
# F.s. = Jumlah akhir candi saat ayam berkokok akan menentukan apakah Roro Jonggrang kalah atau menang

# KAMUS LOKAL
# total candi: integer

# Fungsi yang dipanggil Roro Jonggrang untuk membuat ayam berkokok
def ayamberkokok (candi, current_login, jumlahcandi):
    if current_login == 1: # Fungsi hanya bisa diakses oleh Roro Jonggrang
        totalcandi = 0 # Inisiasi total awal candi
        for i in range(jumlahcandi): # Menghitung banyaknya candi yang sudah dibangun saat ini
            if (candi[i][0] != ""): 
                totalcandi  += 1
        
        print ("Kukuruyuk.. Kukuruyuk..")
        print ("Jumlah Candi:", str(totalcandi))

        if (totalcandi == 100): # Jika jumlah candi = 100, Bandung Bondowoso menang
            print("Yah, Bandung Bondowoso memenangkan permainan!\n")
        else: # Jika kurang dari 100, Roro Jonggrang menang
            print("Selamat, Roro Jonggrang memenangkan permainan!\n")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.\n")
        return(False)
    else: # Jika fungsi dipanggil selain oleh Roro Jonggrang
        print("Command “ayamberkokok” hanya bisa dipanggil oleh Roro Jonggrang!")
        return(True)





