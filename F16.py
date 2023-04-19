def exit():
    masukan = ("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if masukan == "y" or masukan == "Y":
        return 1
    elif masukan == "n" or masukan == "N":
        return 0
    else:
        return -1