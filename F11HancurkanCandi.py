def CekCandi(candi, id):
    for i in range(102):
        if candi[i][0] == id:
            return True 
    return False

def hancurkan(candi):
    id = int(input("Masukkan ID candi: "))
    exist = CekCandi(candi, id)
    if exist:
        decision = input("Apakah anda yakin ingin menghancurkan candi ID: 5 (Y/N)? ")
        if decision == "Y":
            for i in range(102):
                if id == candi[i][0]:
                    candi[i][0] = [0,"",0,0,0]
            print("\nCandi telah berhasil dihancurkan\n")
    else:
        print("\nTidak ada candi dengan ID tersebut.")

#"""
#test case
candi = [[0, "", 0, 0, 0]]*102
candi[0] = [1,"infokan", 5, 5, 5] 
hancurkan(candi)
#"""