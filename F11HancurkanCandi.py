
def hancurkan(candi, current_login):
    if current_login == 1:
        id = int(input("Masukkan ID candi: "))
        if candi[id][0] != "":
            decision = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id} (Y/N)? ")
            if decision == "Y":
                candi[id] = ["",0,0,0]
                print("\nCandi telah berhasil dihancurkan")
            else:
                print("\nCandi tidak jadi dihancurkan")
        else:
            print("\nTidak ada candi dengan ID tersebut.")
    else:
        print("\nCommand “hancurkancandi” hanya bisa dipanggil oleh Roro Jonggrang!")

    return(candi)

#test case
# candi = [["", 0, 0, 0]]*102
# candi[0] = ["infokan", 5, 5, 5] 
# candi[1] = ["",0,0,0]
# candi = hancurkan(candi)
# print(candi)
#"""