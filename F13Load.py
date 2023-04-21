import argparse
import os

def loadFolder(users, candi, bahan):
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", help= "mencari nama folder", nargs = '?', default = "")
    arg = parser.parse_args()
    folder = arg.nama_folder
    parentfolderpath = os.getcwd()

    print("")

    if not(os.path.isdir("./file_eksternal/")):
        print("File parent file_eksternal tidak ditemukan")
        return(users, candi, bahan, False)

    os.chdir("./file_eksternal/")

    if folder == "": 
        print("Tidak ada nama folder yang diberikan!")
        print("\nUsage: python main.py <nama_folder>")
        return(users, candi, bahan, False)
    else:
        folder1 = ""
        namafolder = ""
        x = True
        for i in range (len(folder)): 
            if folder[i] == "/" or folder[i] == "\\" or i == (len(folder)-1): 
                if i == (len(folder)-1):
                    folder1 += folder[i] # Kasus khusus pada iterasi terakhir
                if not (os.path.isdir(folder1)): # Cek folder apakah ada
                    x = False
                else:
                    os.chdir(folder1)
                folder1 = ""
            
                if folder[i] == "\\":
                    namafolder += "/"
                else:
                    namafolder += folder [i]
            
            else:
                folder1 += folder[i]
                namafolder += folder [i]
    
    if x == False:
        print(f'Folder “{namafolder}” tidak ditemukan.')
        return(users, candi, bahan, False)
    else:
        print("Loading...")
        users = loadFileUsers(users)
        candi = loadFileCandi(candi)
        bahan = loadFileBahan(bahan)
        print("Selamat datang di program “Manajerial Candi”")
        print("Silakan login atau masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        os.chdir(parentfolderpath)
        return(users, candi, bahan, True)
    
def loadFileUsers(users):
    file = open("users.csv","r")

    row = file.readline()
    row = file.readline()
    current_index = 0

    while row != "":
        current_user = ["","",""]
        current_column = 0
        current_string = ""
        for i in range(len(row)):
            if row[i] == ";":
                current_user[current_column] = current_string
                current_string = ""
                current_column = current_column + 1
            elif row[i] != "\n":
                current_string = current_string + row[i]
            else:
                break

        current_user[current_column] = current_string
        users[current_index] = current_user
        current_index = current_index + 1
        row = file.readline()
    
    file.close()   
    return(users)

def loadFileCandi(candi):
    file = open("candi.csv","r")

    row = file.readline()
    row = file.readline()
    current_index = 0

    while row != "":
        current_candi = ["","","",""]
        current_column = 0
        current_string = "0"

        for i in range(len(row)): 
            if row[i] == ";":
                while current_column == 0 and int(current_string) != current_index:
                    current_index += 1             
                if current_column == 1:
                    current_candi[current_column-1] = current_string
                elif current_column > 1:
                    current_candi[current_column-1] = int(current_string)
                current_string = ""
                current_column = current_column + 1
            else:
                current_string = current_string + row[i]

        current_candi[current_column-1] = int(current_string)
        candi[current_index] = current_candi
        current_index = current_index + 1
        row = file.readline()
    
    file.close()
    return(candi)

def loadFileBahan(bahan):
    file = open("bahan_bangunan.csv","r")

    row = file.readline()
    row = file.readline()

    for i in range(3):
        current_string=""

        for i in range(len(row)):
            if row[i] == ";":
                if current_string == "pasir":
                    bahan[0] = cariJumlahBahan(row)
                elif current_string == "batu":
                    bahan[1] = cariJumlahBahan(row)
                elif current_string == "air":
                    bahan[2] = cariJumlahBahan(row)
            else:
                current_string = current_string + row[i]
        
        row = file.readline()
    
    file.close()
    return(bahan)

def cariJumlahBahan(row):
    current_string=""
    i = len(row)-1
    while True:
        if row[i] == ";":
            jumlah = int(current_string)
            return(jumlah)
        else:
            current_string = row[i] + current_string
        i -= 1



# users = [["" for i in range (3)]for j in range(5)]
# candi = [[0 for i in range (4)]for j in range(5)]
# bahan = [0 for i in range (3)]

# users, candi, bahan = loadFolder(users,candi,bahan)

# print(users)
# print(candi)
# print(bahan)
