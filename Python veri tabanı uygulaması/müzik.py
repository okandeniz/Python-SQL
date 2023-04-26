from veritabani import *

print("""********************
Şarkı Programına Hoşgeldiniz.

İşlemler:

1-Şarkıları Göster

2-Şarkı Sorgulama

3-Şarkı Ekle

4-Şarkı Sil

5-Şarkı Şirketi Güncelle

6-Veri Tabanına Kayıtlı Şarkıların Toplam Süresi

Çıkmak için q'ya basın
********************
""")

sarki=Sarkılar()

while True:
    islem=input("Yapacağınız işlem: ")
    if (islem=="q"):
        print("Programdan çıkılıyor...")
        time.sleep(1)
        break
    elif (islem=="1"):
        sarki.sarkilari_goster()
    elif (islem=="2"):
        isim=input("Hangi şarkıyı istiyorsunuz? ")
        print("Şarkı sorgulanıyor...")
        time.sleep(2)
        sarki.sarki_sorgula(isim)
    elif (islem=="3"):
        isim=input("İsim: ")
        sanatci=input("Sanatçı: ")
        album=input("Albüm: ")
        sirket=input("Şirket: ")
        sure=int(input("Süre: "))
        yeni_sarki=Sarkı(isim,sanatci,album,sirket,sure)
        print("Şarkı ekleniyor...")
        time.sleep(2)
        sarki.sarki_ekle(yeni_sarki)
        print("Şarkı eklendi.")
    elif (islem=="4"):
        isim=input("Hangi şarkıyı silmek istiyorsunuz? ")
        cevap=input("Emin misiniz? (E/H)")
        if (cevap=="E"):
            print("Şarkı siliniyor..")
            time.sleep(2)
            sarki.sarki_sil(isim)
    elif (islem=="5"):
        isim_eski=input("Güncellenecek şirket ismini giriniz: ")
        isim_yeni=input("Yeni şirket ismi: ")
        print("Şirket ismi güncelleniyor..")
        time.sleep(2)
        sarki.sirket_guncelle(isim_yeni,isim_eski)
    elif (islem=="6"):
        sarki.toplam_sure()