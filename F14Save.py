import os

def save(jumlahusers, users, jumlahcandi, candi, bahan):
    folder = input("\nMasukkan nama folder: ")
    parentfolderpath = os.getcwd()
    print("\nSaving...")

    # cek folder spesifik : file_external
    if not (os.path.isdir("./file_eksternal/")):
        # kalo gada, dibikin
        os.mkdir("file_eksternal")
        print("\nMembuat folder file_eksternal...")

    # pindah ke dalem file external
    os.chdir("./file_eksternal/")

    folder1 = ""
    namafolder =""

    for i in range (len(folder)): 
        if folder[i] == "/" or folder[i] == "\\" or i == (len(folder)-1): 
            if folder[i] == "\\":
                namafolder += "/"
            else:
                namafolder += folder [i]
            
            if i == (len(folder)-1):
                    folder1 += folder[i] # Kasus khusus pada iterasi terakhir
            if not (os.path.isdir(folder1)): # Cek folder apakah ada
                print("\nMembuat folder file_eksternal/" + namafolder + "...")
                os.mkdir(folder1)
            
            os.chdir(folder1)
            folder1 = ""
        else:
            folder1 += folder[i]
            namafolder += folder [i]

    saveUsers(jumlahusers, users)
    saveCandi(jumlahcandi, candi)
    saveBahan(bahan)
    print("\nBerhasil menyimpan data di folder file_eksternal/" + namafolder + "!")    
    
    os.chdir(parentfolderpath)

def saveUsers(jumlahusers,users):
    file = open("users.csv","w")
    file.write("username;password;role")

    for i in range(jumlahusers):
        if users[i][0] != "":
            file.write("\n")
            file.write(users[i][0]+";"+users[i][1]+";"+users[i][2])

    file.close()

def saveCandi(jumlahcandi, candi):
    file = open("candi.csv","w")
    file.write("id;pembuat;pasir;batu;air")

    for i in range(jumlahcandi):
        if candi[i][0] != "":
            file.write("\n")
            file.write(str(i)+";"+candi[i][0]+";"+str(candi[i][1])+";"+str(candi[i][2])+";"+str(candi[i][3]))
    
    file.close()

def saveBahan(bahan):
    file = open("bahan_bangunan.csv","w")
    file.write("nama;deskripsi;jumlah\n")

    file.write("pasir;Material berbentuk butiran yang terdiri dari partikel batuan dan mineral yang terpecah halus;"+str(bahan[0])+"\n")
    file.write("batu;Material padatan yang tersusun atas kumpulan mineral penyusun kerak bumi;"+str(bahan[1])+"\n")
    file.write("air;Material cair yang dibentuk dari molekul H2O;"+str(bahan[2]))

    file.close()

# jumlahusers = 4
# users = [["test","test","jin_pembangun"],
#          ["test2","test2","jin_pengumpul"],
#          ["","",""],
#          ["test3","test3","jin_pembangun"]]

# jumlahcandi = 2
# candi = [["test",1,2,3],
#          ["test2",3,2,1]]

# bahan = [30,40,50]

# save(jumlahusers, users, jumlahcandi, candi, bahan)
