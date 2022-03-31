#ders başarı hesaplama programı
#10.11.2020

v1=eval(input("Vize 1 notunu giriniz(0-100):"))
if v1<0 or v1>100:
    print("lütfen 0-100 aralığında giriniz!")
    v1=eval(input("Vize 1 notunu giriniz(0-100):"))

v2=eval(input("Vize 2 notunu giriniz(0-100):"))
if v2<0 or v2>100:
    print("lütfen 0-100 aralığında giriniz!")
    v2=eval(input("Vize 2 notunu giriniz(0-100):"))
f=eval(input("Final notunu giriniz(0-100):"))
if f<0 or f>100:
    print("lütfen 0-100 aralığında giriniz!")
    f=eval(input("Final notunu giriniz(0-100):"))
    
#evaluate çalıştırmak gibi bir anlamı var 

#ortalama hesabı
#örnek olarak,
#vize1 %20
#vize2 %30
#final %50
#etki oranına sahip olsun
ortalama =(v1*0.2)+(v2*0.3)+(f*0.5)

print("bu dersteki ortalamanız:",ortalama)

#iften sonra yapmamız gereken şey bir koşul
#if bütün dillerde kullanılır faklat başka dillerde farklılıkları var

if ortalama>=50:
    print("TEBRİKLER!")
    print("dersi başardınız")

#else koysaydık buraya yine çalışırdı . (eğer üsteki sağlanırsa üstteki aksi taktirde alttaki çalışır )
#farklı bir yol:
#if ortalama>=50:
  #  print("TEBRİKLER!")
  #  print("dersi başardınız")
#else eğer 50 den çüküse alttaki çalşışır.
   # print("üzgünüm....")
   # print("başarlı olamadınız.")
if ortalama<50:
    print("üzgünüm....")
    print("başarlı olamadınız.")



print("***program sonlandı***")

 #[80-100]   --> A
#[60-80)-->B
#[50-60)-->C
#[30-50)-->D
#[0-30)-->F

if ortalama >=80 and ortalama<=100:
    print("DERS BAŞARI NOTU:A")

elif ortalama >=60 and ortalama<80:
    print("DERS BAŞARI NOTU:B")

elif ortalama >=50 and ortalama<60:
    print("DERS BAŞARI NOTU:C")

elif ortalama >=30 and ortalama<50:
    print("DERS BAŞARI NOTU:D")

elif ortalama >=0 and ortalama<30:
    print("DERS BAŞARI NOTU:F")
else:
    print("ortalama hatalı (0-100) dışında değer giremezsiniz")

#else if 'i pythın elif diye kısaltıyor. else:if diye yazman gerekir eğer ayrı yazmak istersen
    
    
