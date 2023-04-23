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
            print("Yah, Bandung Bondowoso memenangkan permainan!\n")
        else:
            print("Selamat, Roro Jonggrang memenangkan permainan!\n")
            print("*Bandung Bondowoso angry noise*")
            print("Roro Jonggrang dikutuk menjadi candi.\n")
        return(False)
    else:
        print("Command “ayamberkokok” hanya bisa dipanggil oleh Roro Jonggrang!")
        return(True)





