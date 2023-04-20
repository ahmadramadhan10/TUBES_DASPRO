import random

def bangun(bahan, sisa_candi):
    if sisa_candi == 0:
        print("Candi berhasil dibangun.")
        print("Sisa candi yang perlu dibangun: {sisa_candi}")
        return (bahan, sisa_candi)

    pasir = int(random.uniform(1,5))
    batu = int(random.uniform(1,5))
    air = int(random.uniform(1,5))
    if bahan[0] >= pasir and bahan[1] >= batu and bahan[2] >= air:
        bahan[0] = bahan[0] - pasir
        bahan[1] = bahan[1] - batu
        bahan[2] = bahan[2] - air
        sisa_candi = sisa_candi - 1
        print(f'Candi berhasil dibangun.')
        print(f'Sisa candi yang perlu dibangun: {sisa_candi}.')
    else:
        print("Bahan bangunan tidak mencukupi.")
        print("Candi tidak bisa dibangun!")
    return (bahan,sisa_candi)


# test case
bahan = [100, 100, 100]
sisa_candi = 100
"""
t = 5
for i in range(t):
    print(bangun(bahan,100))
"""
bahan, sisa_candi = bangun(bahan, sisa_candi)
print(bahan, sisa_candi)