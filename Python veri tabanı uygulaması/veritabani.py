import sqlite3
import time
from functools import reduce

class Sarkı():
    def __init__(self,isim,sanatci,album,sirket,sure):
        self.isim=isim
        self.sanatci=sanatci
        self.album=album
        self.sirket=sirket
        self.sure=sure
    def __str__(self):
        return "Şarkı: {}\nSanatçı: {}\nAlbüm: {}\nProdüksyon Şirketi: {}\nŞarkı Süresi: {}".format(self.isim,self.sanatci,self.album,self.sirket,self.sure)


class Sarkılar():
    def __init__(self):
        self.baglanti_olustur()
    
    def baglanti_olustur(self):
        self.baglanti=sqlite3.connect("C:/Users/okand/Desktop/github/Python-SQL/veri tabanı uygulaması/muzik.db")
        self.cursor=self.baglanti.cursor()
        sorgu="create table if not exists sarkılar(isim TEXT,sanatçı TEXT,albüm TEXT,şirket TEXT,süre INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()
    
    def baglanti_kes(self):
        self.baglanti.close()

    def sarkilari_goster(self):
        sorgu="select * from sarkılar"
        self.cursor.execute(sorgu)
        sarkilar=self.cursor.fetchall()
        if (len(sarkilar)==0):
            print("Veri tabanında şarkı bulunmuyor")
        else:
            for i in sarkilar:
                sarki=Sarkı(i[0],i[1],i[2],i[3],i[4])
                print(sarki)

    def sarki_ekle(self,sarki):
        sorgu="insert into sarkılar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(sarki.isim,sarki.sanatci,sarki.album,sarki.sirket,sarki.sure))
        self.baglanti.commit()

    def sarki_sil(self,sarki):
        sorgu="delete from sarkılar where isim=?"
        self.cursor.execute(sorgu,(sarki,))
        self.baglanti.commit()
    
    def sarki_sorgula(self,sarki):
        sorgu="select*from sarkılar where isim=?"
        self.cursor.execute(sorgu,(sarki,))
        sarkilar=self.cursor.fetchall()

        if (len(sarkilar)==0):
            print("Böyle bir şarkı bulunmuyor..")
        else:
            sarki=Sarkı(sarkilar[0][0],sarkilar[0][1],sarkilar[0][2],sarkilar[0][3],sarkilar[0][4])
            print(sarki)
    
    def toplam_sure(self):
        sorgu="select süre from sarkılar"
        self.cursor.execute(sorgu)
        sureler=self.cursor.fetchall()
        toplam=0
        for i in sureler:
            i=str(i)
            i=i.strip("(")
            i=i.strip(")")
            i=i.strip(",")
            i=int(i)
            toplam+=i

        
        print("Kayıtlı şarkıların toplam süresi: {}".format(toplam))

    def sirket_guncelle(self,yeni_sirket,eski_sirket):
        sorgu="update sarkılar set şirket=? where şirket=?"
        self.cursor.execute(sorgu,(yeni_sirket,eski_sirket))
        self.baglanti.commit()