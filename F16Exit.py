from F14Save import save

def exit(jumlahusers, users, jumlahcandi, candi, bahan):
    konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    while konfirmasi != 'y' and konfirmasi != 'n':
        konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if konfirmasi == "y":
        save(jumlahusers, users, jumlahcandi, candi, bahan)
    print("Keluar dari program...")
    print("Berhasil keluar dari program!")

"""
jumlahusers = 2
users = [["test","test","jin_pembangun"],
         ["test2","test2","jin_pengumpul"]]

jumlahcandi = 2
candi = [["test",1,2,3],
         ["test2",3,2,1]]

bahan = [30,40,50]

exit(jumlahusers, users, jumlahcandi, candi, bahan)
"""