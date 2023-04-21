default = ["",0,0,0]

def CekCandi(candi, id):
    # jika nilai candi[id] == default berarti candi dengan ID tertentu tidak ada
    return not (default == candi[id])

def hancurkan(candi):
    id = int(input("Masukkan ID candi: "))
    exist = CekCandi(candi, id)
    if exist:
        decision = input("Apakah anda yakin ingin menghancurkan candi ID: 5 (Y/N)? ")
        if decision == "Y":
            candi[id] = default
            print("\nCandi telah berhasil dihancurkan\n")
    else:
        print("\nTidak ada candi dengan ID tersebut.")

#"""
#test case
candi = [["", 0, 0, 0]]*102
candi[0] = ["infokan", 5, 5, 5] 
hancurkan(candi)
#"""