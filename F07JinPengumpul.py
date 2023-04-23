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