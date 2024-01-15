import random
import time

print("""*******************************

SAYI TAHMİN OYUNU


1 ile 40 arasında sayı tahmin edin.



*******************************""")


rastgele_sayı = random.randint(1,40)

tahmin_hakki= 7



while True:

    tahmin = int(input("Bir sayı giriniz:"))

    if (tahmin < rastgele_sayı):
        print("Bilgileriniz sorgulanıyor...")
        time.sleep(1)
        print("Tahmininiz sayıdan düşük.")

        tahmin_hakki -=1

    elif (tahmin > rastgele_sayı):
        print("Bilgileriniz sorgulanıyor...")
        time.sleep(1)

        print("Tahmininiz sayıdan yüksek.")
        tahmin_hakki -=1

    else:
        print("Bilgileriniz sorgulanıyor..")
        time.sleep(1)

        print("Tebrikler doğru cevap..")
        break


    if (tahmin_hakki ==0):
        print("Tahmin hakkınız bitti.")
        print("Sayımız:",rastgele_sayı)
        break


























