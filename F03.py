def SummonJin():
    jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
    print("")
    if jenis_jin == 1:
        pass
    elif jenis_jin == 2:
        pass
    else:
        print(f'Tidak ada jenis jin bernomor "{jenis_jin}"!\n')
        SummonJin()
