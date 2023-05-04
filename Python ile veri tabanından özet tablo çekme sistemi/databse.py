import sqlite3
import time
import re
import pandas as pd
import numpy as np


class database():
    def __init__(self):
        self.dongu=True

    def program(self):
        secim=self.menu()
        if secim=="1":
            print("Satış Tablosu Hazırlanıyor..\n")
            time.sleep(3)
            self.satis_tablo()
        if secim=="2":
            print("Personel Başarısı Tablosu Hazırlanıyor..\n")
            time.sleep(3)
            self.personel_basari()
        if secim=="3":
            print("Tedarikçi Tablosu Hazırlanıyor..\n")
            time.sleep(3)
            self.tedarikci()
        if secim=="4":
            print("Kategorilere Göre Ortalama Ürün Fiyatları Tablosu Hazırlanıyor")
            time.sleep(3)
            self.kategori_fiyatlari()
        if secim=="5":
            print("Çıkış Yapılıyor..\n")
            time.sleep(3)
            self.cikis()

    def menu(self):
        def kontrol(secim):
            if re.search("[^1-5]",secim):
                raise Exception("Lütfen 1 ve 5 geçerli bir seçim yapınız.")
            elif len(secim)!=1:
                raise Exception("Lütfen 1 ve 5 geçerli bir seçim yapınız.")
        while True:
            try:
                secim=input("Merhabalar, Veri Tabanından Özet Tablolar Sunan Programa Hoşgeldiniz!\n\nLütfen yapmak istediğiniz işlemi seçiniz...\n\n[1]-Detaylı Sipariş Tablosu\n[2]-Şatış Personellerinin Performansları\n[3]-Tedarikçiden Alınan Ürünlerin Satış Performansı\n[4]-Kategori Başına Ortalama Ürün Fiyatı\n[5]-Çıkış\n\n")
                kontrol(secim)
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return secim
    
    def satis_tablo(self):
        while True:
            try:
                secme=input("""
                Lütfen seçimini yapınız:\n\n
                [1]- 5000 dolar üzeri satışlar gelsin.\n
                [2]- 10000 dolar üzeri satışlar gelsin.\n
                [3]- Tüm satışlar Gelsin\n\n""")

                if secme=="1":
                    conn=sqlite3.connect("C:/Users/okand/Desktop/projeler2/sql/vbo.db")
                    tablo=pd.read_sql("""select CustomerName as Musteri_Adı, Address as Musteri_Adresi, City as Musteri_Sehir,
                    Country as Musteri_Ulke, ProductName as Urun_Adi, CategoryName as Urun_Kategorisi, 
                    OrderDate as Siparis_Tarihi, Quantity as Miktar, Price as Fiyat, Quantity*Price as Toplam_Fiyat, 
                    ShipperName as Nakliye_firması  from Orders o 
                    left join OrderDetails od on o.OrderID=od.OrderID
                    left join Products p on od.ProductID=p.ProductID
                    left join Categories ca on p.CategoryID=ca.CategoryID 
                    left join Customers cu on o.CustomerID=cu.CustomerID 
                    left join Shippers sh on o.ShipperID=sh.ShipperID
                    where Toplam_Fiyat > 5000
                    order by Toplam_fiyat desc;""",conn)

                    print(tablo)

                    secme2=input("Tabloyu Bilgisayarınıza Excel Formatında Kaydetmek İster misiniz?\n[E/H]\n\n")
                    if secme2 == "E":
                        dizin=input("C:/Users/?: ? ile gösterilen bilgisayarınızın adını giriniz: \n\n")
                        dizin="C:/Users/"+dizin+"/Desktop/satis_tablo.xlsx"
                        dosya=tablo.to_excel(dizin,index=False)
                        conn.close()
                        self.menudon()
                    else:
                        conn.close()
                        self.menudon()
                
                if secme=="2":
                    conn=sqlite3.connect("C:/Users/okand/Desktop/projeler2/sql/vbo.db")
                    tablo=pd.read_sql("""select CustomerName as Musteri_Adı, Address as Musteri_Adresi, City as Musteri_Sehir,
                    Country as Musteri_Ulke, ProductName as Urun_Adi, CategoryName as Urun_Kategorisi, 
                    OrderDate as Siparis_Tarihi, Quantity as Miktar, Price as Fiyat, Quantity*Price as Toplam_Fiyat, 
                    ShipperName as Nakliye_firması  from Orders o 
                    left join OrderDetails od on o.OrderID=od.OrderID
                    left join Products p on od.ProductID=p.ProductID
                    left join Categories ca on p.CategoryID=ca.CategoryID 
                    left join Customers cu on o.CustomerID=cu.CustomerID 
                    left join Shippers sh on o.ShipperID=sh.ShipperID
                    where Toplam_Fiyat > 10000
                    order by Toplam_fiyat desc;""",conn)

                    print(tablo)

                    secme2=input("Tabloyu Bilgisayarınıza Excel Formatında Kaydetmek İster misiniz?\n[E/H]\n\n")
                    if secme2 == "E":
                        dizin=input("C:/Users/?: ? ile gösterilen bilgisayarınızın adını giriniz: \n\n")
                        dizin="C:/Users/"+dizin+"/Desktop/satis_tablo.xlsx"
                        dosya=tablo.to_excel(dizin,index=False)
                        conn.close()
                        self.menudon()
                    else:
                        conn.close()
                        self.menudon()
                
                if secme=="3":
                    conn=sqlite3.connect("C:/Users/okand/Desktop/projeler2/sql/vbo.db")
                    tablo=pd.read_sql("""select CustomerName as Musteri_Adı, Address as Musteri_Adresi, City as Musteri_Sehir,
                    Country as Musteri_Ulke, ProductName as Urun_Adi, CategoryName as Urun_Kategorisi, 
                    OrderDate as Siparis_Tarihi, Quantity as Miktar, Price as Fiyat, Quantity*Price as Toplam_Fiyat, 
                    ShipperName as Nakliye_firması  from Orders o 
                    left join OrderDetails od on o.OrderID=od.OrderID
                    left join Products p on od.ProductID=p.ProductID
                    left join Categories ca on p.CategoryID=ca.CategoryID 
                    left join Customers cu on o.CustomerID=cu.CustomerID 
                    left join Shippers sh on o.ShipperID=sh.ShipperID
                    order by Toplam_fiyat desc;""",conn)

                    print(tablo)

                    secme2=input("Tabloyu Bilgisayarınıza Excel Formatında Kaydetmek İster misiniz?\n[E/H]\n\n")
                    if secme2 == "E":
                        dizin=input("C:/Users/?: ? ile gösterilen bilgisayarınızın adını giriniz: \n\n")
                        dizin="C:/Users/"+dizin+"/Desktop/satis_tablo.xlsx"
                        dosya=tablo.to_excel(dizin,index=False)
                        conn.close()
                        self.menudon()
                    else:
                        conn.close()
                        self.menudon()
                
            except AttributeError:
                print("Hatalı Giriş Yaptınız")
                time.sleep(3)

    def personel_basari(self):
        while True:
            try:
                conn=sqlite3.connect("C:/Users/okand/Desktop/projeler2/sql/vbo.db")
                tablo=pd.read_sql("""Select FirstName as Personel_Ad, LastName as Personel_Soyad, 
                sum(Quantity*Price) as Toplam_Satış
                from Orders o 
                left join Employees e on o.EmployeeID=e.EmployeeID
                left join OrderDetails od on o.OrderID=od.OrderID
                left join Products p on od.ProductID=p.ProductID
                left join Categories ca on p.CategoryID=ca.CategoryID 
                left join Customers cu on o.CustomerID=cu.CustomerID  
                group by Personel_Ad
                order by Toplam_Satış desc;""",conn)

                print(tablo)

                secme=input("Tabloyu Bilgisayarınıza Excel Formatında Kaydetmek İster misiniz?\n[E/H]\n\n")
                if secme =="E":
                    dizin=input("C:/Users/?: ? ile gösterilen bilgisayarınızın adını giriniz: \n\n")
                    dizin="C:/Users/"+dizin+"/Desktop/basari_tablo.xlsx"
                    dosya=tablo.to_excel(dizin,index=False)
                    conn.close()
                    self.menudon()
                else:
                    conn.close()
                    self.menudon()
                
            except AttributeError:
                print("Hatalı Giriş Yaptınız")
                time.sleep(3)
    
    def tedarikci(self):
        while True:
            try:
                conn=sqlite3.connect("C:/Users/okand/Desktop/projeler2/sql/vbo.db")
                tablo=pd.read_sql("""Select SupplierName as Tedarikci, CategoryName as Urun_Kategorisi, 
                Quantity as Miktar, Price as Fiyat, Quantity*Price as Toplam_Satış 
                from Orders o 
                left join OrderDetails od on o.OrderID=od.OrderID
                left join Products p on od.ProductID=p.ProductID
                left join Suppliers su on p.SupplierID=su.SupplierID
                left join Categories ca on p.CategoryID=ca.CategoryID 
                left join Customers cu on o.CustomerID=cu.CustomerID 
                group by Tedarikci
                order by Toplam_Satış desc;""",conn)

                print(tablo)

                secme=input("Tabloyu Bilgisayarınıza Excel Formatında Kaydetmek İster misiniz?\n[E/H]\n\n")
                if secme =="E":
                    dizin=input("C:/Users/?: ? ile gösterilen bilgisayarınızın adını giriniz: \n\n")
                    dizin="C:/Users/"+dizin+"/Desktop/tedarikci_tablo.xlsx"
                    dosya=tablo.to_excel(dizin,index=False)
                    conn.close()
                    self.menudon()
                else:
                    conn.close()
                    self.menudon()
                
            except AttributeError:
                print("Hatalı Giriş Yaptınız")
                time.sleep(3)

    def kategori_fiyatlari(self):
        while True:
            try:
                conn=sqlite3.connect("C:/Users/okand/Desktop/projeler2/sql/vbo.db")
                tablo=pd.read_sql("""select CategoryName as Kategori_ismi, avg(Price) as ortalama_fiyat 
                from Products 
                left join Categories on Products.CategoryID=Categories.CategoryID 
                group by CategoryName 
                order by Price desc;""",conn)

                print(tablo)

                secme=input("Tabloyu Bilgisayarınıza Excel Formatında Kaydetmek İster misiniz?\n[E/H]\n\n")
                if secme =="E":
                    dizin=input("C:/Users/?: ? ile gösterilen bilgisayarınızın adını giriniz: \n\n")
                    dizin="C:/Users/"+dizin+"/Desktop/kategori_tablo.xlsx"
                    dosya=tablo.to_excel(dizin,index=False)
                    conn.close()
                    self.menudon()
                else:
                    conn.close()
                    self.menudon()
                
            except AttributeError:
                print("Hatalı Giriş Yaptınız")
                time.sleep(3)

    def cikis(self):
        self.dongu=False
        exit()
    
    def menudon(self):
        while True:
            x=input("Ana menüye dönmek için 7'ye, çıkmak için lütfen 6'ya basınız..: ")
            if x=="7":
                print("Ana menüye dönülüyor...")
                time.sleep(3)
                self.program()
                break
            elif x=="6":
                self.cikis()
                break
            else:
                print("Lütfen geçerli bir seçim yapınız...")




sistem=database()
while sistem.dongu:
    sistem.program()
        







