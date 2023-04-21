# Program Ayam Berkokok

def ayamberkokok (candi, current_login, jumlahcandi):
    if current_login == 1:
        totalcandi = 0
        for i in range(jumlahcandi):
            if (candi[i][0] != ""):
                totalcandi  += 1
        
        print ("Kukuruyuk.. Kukuruyuk..")
        print ("Jumlah Candi:", str(totalcandi))

        if (totalcandi == 100):
            print("Yah, Bandung Bondowoso memenangkan permainan!")
        else:
            print("Selamat, Roro Jonggrang memenangkan permainan!\n")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.")
    else:
        print("\nCommand “ayamberkokok” hanya bisa dipanggil oleh Roro Jonggrang!")

# Candi = [["","","",""] for i in range(100)]
# Candi[0] = ["test", 1,2,3]
# Candi[1] = ["test2",3,2,1]
# Candi[2] = ["test3",2,4,4]
# totalcandi = 0

# ayamberkokok(totalcandi)





