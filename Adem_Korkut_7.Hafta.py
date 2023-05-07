## 7.Hafta: Dosyalarla Calisma ##
# 1.Soru Dosya Islemleri

dosya = input("Lütfen bir dosya uzantisi girin: ")

try:
    with open(dosya, 'r') as d:
        toplam = 0 # Satirlardaki sayilarin toplamini atayacagim degisken
        satir_sayisi = 0 # Satir sayisini atayacagim degisken
        
        for i in dosya: # Dosyadaki tum satirlari tek tek okumak icin for dongusu baslattim
            try:
                sayi = int(i) # Satirdaki rakamsal degeri sayiya donusturdum.
            except ValueError: # Satirdaki degeri sayi olmadigi durumlar icin.
                print(f"{i} sayi değil, atlandi.")
            else:
                toplam += sayi # Buldugum her sayiyi toplam degiskenine gonderdim.
                satir_sayisi += 1 # Her turda satir sayisini 1 arttirdim.
                
        if satir_sayisi > 0: 
            ortalama = toplam / satir_sayisi
            print(f"Toplam: {toplam}")
            print(f"Ortalama: {ortalama}")
        else:
            print("Dosyada sayi içeren hiçbir satir bulunamadi.") # Satirlarda sayi iceren bir ifade bulunamadigi durumlar icin.
except FileNotFoundError:
    print("Dosya bulunamadi. Lütfen doğru dosya uzantisi girin.") # Dosyanin bulunamadigi durum icin.
    ################################################################################

    # 2. Soru: Dosya Duzenleme

    dosya = input("Lütfen dosya uzantisi girin: ") # Dosya uzantisi istedim cunku sadece isim girildiginde hata aldigim durumlar oldu.

try:
    with open(dosya, 'r') as d:
        satirlar = d.readlines() # Dosyanin tum satirlarini satirlar adinda bir listede topladim.
except FileNotFoundError:
    print("Dosya bulunamadi. Lütfen doğru bir dosya uzantisi girin.")
else:
    with open(dosya, 'w') as d:
        for i, satir in enumerate(satirlar, start=1 ): # satir ifadesi satirlar degiskeninin her bir elemanini temsil eder. start parametresi ile kacinci indexten baslayacagini belirttim.
            d.write(f"{i}. {satir}")
    print("Dosya güncellendi.")
#####################################################################################

# 3. Soru: JSON Islemleri

import json
# Ogrenci bilgilerinin saklayacagim dosyayi olusturmak icin.
with open('students.json', 'r') as f:
    students = json.load(f)
while True: # Kullanici cikana kadar devam eden bir dongu olusturdum.
    # Kullaniciya secenekleri gosterdim
    print("\nSecenekler:")
    print("1 - Yeni ogrenci ekle")
    print("2 - Ogrenci listesini goruntule")
    print("3 - Programdan cik")
    # Kullanicinin secimini yaptigi durumlar
    secim = input("Seciminizi girin: ")
    if secim == '1':
        # Yeni ogrenci ekleme islemi
        ad = input("Ogrenci adi: ")
        soyad = input("Ogrenci soyadi: ")
        yas = int(input("Ogrenci yas: "))
        # Yeni ogrenci sozlugu olusturdum.
        yeni_ogrenci = {'ad': ad, 'soyad': soyad, 'yas': yas}
        # Ogrenci listesine yeni ogrenciyi ekle
        students.append(yeni_ogrenci)
        print("Ogrenci basariyla eklendi!")
    elif secim == '2':
        # Ogrenci listesini goruntuleme işlemi
        if len(students) == 0:
            print("Henuz ogrenci eklenmemis.")
        else:
            print("Ogrenci listesi:")
            for ogrenci in students:
                print(f"{ogrenci['ad']} {ogrenci['soyad']} ({ogrenci['yas']})") 
    elif secim == '3':
        # Programdan cıkis saglandi
        break 
    else:
        # Gecersiz secenek oldugu durumlar
        print("Gecersiz secenek. Lutfen tekrar deneyin.")
# Guncellenmis ogrenci listesini JSON dosyasina yazildi
with open('students.json', 'w') as f:
    json.dump(students, f)
print("Program sonlandirildi.")
