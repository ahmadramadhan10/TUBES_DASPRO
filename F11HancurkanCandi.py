def CekCandi(candi):
    return True


def hancurkan(candi):
    id = int(input("Masukkan ID candi: "))
    exist = CekCandi(candi)
    if exist:
        decision = input("Apakah anda yakin ingin menghancurkan candi ID: 5 (Y/N)? ")
        if decision == "Y":
            for i in range(1):
                if id == candi[i][0]:
                    candi[i][0] = [0,"",0,0,0]
            print("\nCandi telah berhasil dihancurkan\n")
    else:
        print("\nTidak ada candi dengan ID tersebut.")

"""
test case
candi = [[1,"infokan", 5, 5, 5]]
hancurkan(candi)
"""