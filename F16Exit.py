# procedure exit (input jumlahusers : integer, input users : matriksusers, input jumlahcandi : integer, input candi : matrikscandi, input bahan : matriksbahan
# I.S. = Masukan berupa jumlahusers, users, jumlahcandi,  candi, dan bahan yang sudah terdefinisi 
# F.S. = Program akan keluar dan jika konfirmasi y/Y program akan memanggil fungsi save dan akan menampilkan pesan bahwa telah berhasil keluar dari program 

from F14Save import save # Import fungsi save pada F14
def exit(jumlahusers, users, jumlahcandi, candi, bahan):
    # KAMUS LOKAL
    # konfirmasi : string
    konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ") # Meminta input konfirmasi apakah ingin disave tau tidak
    while konfirmasi != 'y' and konfirmasi != 'n': # Jika konfirmasi selain 
        konfirmasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if konfirmasi == "y":
        save(jumlahusers, users, jumlahcandi, candi, bahan)
    print("Keluar dari program...")
    print("Berhasil keluar dari program!\n")