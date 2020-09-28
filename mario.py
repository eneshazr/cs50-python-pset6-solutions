import cs50

while True:

    satir = cs50.get_int("Yukseklik: ")
    if satir <= 0 or satir > 23:
        continue

    else:   
        for i in range(satir):
            print(' '*(satir-i-1) + '#'*(1*i+1))
        break