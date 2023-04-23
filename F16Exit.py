from F14Save import save

def exit(jumlahusers, users, jumlahcandi, candi, bahan):
    konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while konfirmasi != 'y' and konfirmasi != 'n':
        konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if konfirmasi == "y":
        save(jumlahusers, users, jumlahcandi, candi, bahan)
    print("Keluar dari program...")
    print("Berhasil keluar dari program!\n")