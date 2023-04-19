import argparse, os

def load():
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", nargs="?")
    args = parser.parse_args()
    if not args.nama_folder: #nama folder tidak ada
        print("Tidak ada nama folder yang diberikan!")
        print("Usage: python main.py <nama_folder>")
        return False
    else:
        if os.path.exists(args.nama_folder): # cek apakah folder tersebut ada di path
            print("Loading...")
            print(f'Selamat datang di program "Manajerial Candi"')
            print(f'Silahkan masukkan username Anda')
            return True
            pass
        else:
            print(f'Folder "{args.nama_folder}" tidak ditemukan.')
            return False

def load_file():
    pass
