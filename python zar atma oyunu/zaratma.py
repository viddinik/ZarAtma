import random

min = 1
max = 6

zar = "evet"
hata_sayisi = 0

while zar.lower() in ["evet", "e"]:
    print("Zarlar Atılıyor...")
    zar1 = random.randint(min, max)
    zar2 = random.randint(min, max)
    sonuc = zar1 + zar2

    print(f" 1. Atılan Zar: {zar1}")
    print(f" 2. Atılan Zar: {zar2}")

    zar = input("Bir kez daha zar atmak ister misiniz? ")

    while zar.lower() not in ["evet", "e"]:
        if zar.lower() == "hayir" or zar.lower() == "h":
            print("Oyun sonlandırıldı. İyi günler!")
            exit()
        else:
            hata_sayisi += 1
            if hata_sayisi >= 4:
                print("3 kere art arda yanlış giriş yaptınız. Oyun sonlandırıldı.")
                exit()
            zar = input(f"Yanlış bir kelime veya harf girdiniz. Tekrar oynamak için 'evet' veya 'e', oyunu sonlandırmak için 'hayir' veya 'h' girin: ")
else:
    print("İyi günler :)")
