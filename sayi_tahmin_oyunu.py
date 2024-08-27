# 1-100 arasında rastgele sayı üretilir ve 5 hak verilir tahmin ettiğiniz sayi sayıdan büyukse aşağı küçükse yukarı diye yazar



import random

sayi = random.randint(1, 100)
hak = 5

while hak > 0:
    hak -= 1
    tahmin = int(input('tahmin: '))

    if sayi == tahmin:
        print('Tebrikler Bildiniz.')
        break
    elif sayi > tahmin:
        print('yukarı')
    else:
        print('aşağı')

if hak == 0:
    print(f'hakkınız bitti. Tutulan sayı: {sayi}')
