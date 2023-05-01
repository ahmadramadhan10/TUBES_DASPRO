import argparse
import os

def loadFolder(users, candi, bahan):
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", help= "mencari nama folder", nargs = '?', default = "")
    arg = parser.parse_args()
    folder = arg.nama_folder
    parentfolderpath = os.getcwd() # Mengambil direktori dari working folder saat ini

    print("")

    if not(os.path.isdir("./file_eksternal/")): # Mencari apakah direktori parent folder ada atau tidak (folder file_eksternal)
        print("File parent file_eksternal tidak ditemukan")
        return(users, candi, bahan, False)

    os.chdir("./file_eksternal/") # Masuk (membuka) ke folder file_eksternal
    # KAMUS
    # folder, folder1, namafolder : string


    if folder == "": # cek apakah input nama folder kosong
        print("Tidak ada nama folder yang diberikan!")
        print("\nUsage: python main.py <nama_folder>")
        return(users, candi, bahan, False)
    else: # jika input <nama_folder> ada
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
                    os.chdir(folder1) # Apabila folder sudah ada masuk ke dalam folder
                folder1 = ""
            
                if folder[i] == "\\":
                    namafolder += "/"
                else:
                    namafolder += folder [i]
            
            else:
                # membentuk nama folder
                folder1 += folder[i] 
                namafolder += folder [i]
    
    if x == False: # nama folder tidak ada
        print(f'Folder “{namafolder}” tidak ditemukan.')
        return(users, candi, bahan, False) # mengembalikan array
    else: # jika nama folder ada di file_eksternal maka load semua file user, candi, dan bahan
        print("Loading...")
        users = loadFileUsers(users) # memuat file users
        candi = loadFileCandi(candi) # memuat file candi
        bahan = loadFileBahan(bahan) # memuat file bahan
        print("Selamat datang di program “Manajerial Candi”")
        print("Silakan login atau masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        os.chdir(parentfolderpath) # Kembali ke folder main.py
        return(users, candi, bahan, True) # mengembalikan array yang telah memuat file
    
def loadFileUsers(users):
    # KAMUS

    # current_index, current_column : integer
    # current_string, row : string
    # current_user : array[1..3] of string

    file = open("users.csv","r") # open dan assign file 

    row = file.readline() # membaca nama column
    row = file.readline() # membaca data pertama
    current_index = 0
    while row != "": # jika sekarang berisi string maka proses
        current_user = ["","",""] 
        current_column = 0
        current_string = ""
        for i in range(len(row)):
            if row[i] == ";": # cek apakah string pada column sudah berakhir
                current_user[current_column] = current_string
                current_string = ""
                current_column = current_column + 1
            elif row[i] != "\n": # cek jika bukan akhir file
                current_string = current_string + row[i]
            else: # jika suda akhir file
                break

        current_user[current_column] = current_string 
        users[current_index] = current_user
        current_index = current_index + 1
        row = file.readline()
    
    file.close() # menutup file
    return(users) # mengembalikan file yang telah dimuat

def loadFileCandi(candi):
    # KAMUS

    # current_index, current_column : integer
    # current_string, row : string
    # current_candi : array[1..4] of string

    file = open("candi.csv","r")

    row = file.readline()
    row = file.readline()
    current_index = 0

    while row != "": # jika sekarang berisi string maka proses
        current_candi = ["","","",""]
        current_column = 0
        current_string = "0"

        for i in range(len(row)): 
            if row[i] == ";": # cek apakah string pada column sudah berakhir
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

        current_candi[current_column-1] = int(current_string) # menjadikan int
        candi[current_index] = current_candi
        current_index = current_index + 1
        row = file.readline() # membaca baris selanjutnya
    
    file.close()
    return(candi)

def loadFileBahan(bahan):
    # KAMUS

    # current_string, row : string
    file = open("bahan_bangunan.csv","r")

    row = file.readline()
    row = file.readline()

    for j in range(3):
        current_string=""

        for i in range(len(row)):
            if row[i] == ";": # jika sudah akhir column
                if current_string == "pasir": # cek apakah string sekarang adalah pasir
                    bahan[0] = cariJumlahBahan(row) 
                elif current_string == "batu": # cek apakah string sekarang adalah batu
                    bahan[1] = cariJumlahBahan(row)
                elif current_string == "air": # cek apakah string sekarang adalah air
                    bahan[2] = cariJumlahBahan(row)
            else:
                current_string = current_string + row[i] # string ditambah
        
        row = file.readline()
    
    file.close()
    return(bahan)

def cariJumlahBahan(row):
    # KAMUS

    # current_string : string
    # i : Integer
    current_string=""
    i = len(row)-1
    while True: 
        if row[i] == ";": # jika sudah akhir dari column 
            jumlah = int(current_string) # jadikan integer
            return(jumlah) # balikan nilai
        else:
            current_string = row[i] + current_string # stringnya ditambah
        i -= 1 # melakukan decreament pada index