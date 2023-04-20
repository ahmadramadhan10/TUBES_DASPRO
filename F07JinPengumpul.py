from random import randint
def jinPengumpul (users, bahan, current_login):
    if users[current_login][2] == "jin_pengumpul":
        pasir = randint(0,5)
        batu = randint(0,5)
        air = randint(0,5)
        bahan[0] += pasir
        bahan[1] += batu
        bahan[2] += air
        print(f"Jin menemukan {pasir} pasir, {batu} batu, dan {air} air.")
    else:
        print("Command “kumpul” hanya bisa dipanggil oleh user dengan role Jin Pengumpul!")
    return(bahan)


users = [["" for i in range(3)]for j in range(5)]
users[0] = ["bandung","cintaroro","bandung_bondowoso"]
users[1] = ["roro","gasukabondo","roro_jonggrang"]
users[2] = ["test","test","jin_pengumpul"]
users[3] = ["test2","test2","jin_pembangun"]
users[4] = ["test3","test3","jin_pembangun"]

bahan = [10,10,10]

current_login = 2

bahan = [1,2,3]
bahan = jinPengumpul(users, bahan, current_login)
print(bahan)