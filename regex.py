import re

text = """Merhaba. Ben Aktan Gültekin. 22 yaşındayım. Öğrenciyim. Ankara'da oturuyorum.
Doğum tarihim 05.04.2002"""

isim = r"Ben\s\w+\s\w+"   #isim adlı pattern ile isim soyisim alındı.
yas = r"\d+ yaşındayım."  #yas adlı pattern ile konuşmadaki yaş bilgisi elde edildi.
yasadigiYer = r"[A-İ]+'de|[A-İ]+'da" #yasadigiYer adlı pattern ile konuşmada kişinin yaşadığı yer bilgisi elde edildi.
tarih = r"[0-3][0-9].[0-1][0-9].[0-9]{4}" #tarih adlı pattern ile konuşmada kişinin doğum tarihi elde edildi.

x = re.findall(isim, text)
print(x)
isimSoyisim = x[0][4:] # Slicing yöntemi "Ben John Doe" kalıbıyla verildiği için 4: olarak kullanıldı.
print(isimSoyisim)# İsim ve soyisime ulaşıldı.

print("\n")

x= re.findall(yas, text)
print(x)
yas = x[0] # Yaş verisi listeden çıkarıldı.
yas = yas.split() # Veri, içerdiği boşluk karakteriyle ayrıldı. Bu sayede yaş verisi salt haliyle elde edildi.
print(yas) #Kümede gözüken hali
yas = yas[0]#yas degiskenine yas verisi verildi.
print(yas)#Yaşa ulaşıldı.

print("\n")

x = re.findall(yasadigiYer, text)
print(x)
yasadigiYer = str(x[0]) #Şehir verisi alındı.
print(yasadigiYer)
yasadigiYer, b, c = yasadigiYer.partition("'") #Şehir verisinde bulunan ek silindi.
print(yasadigiYer)#Yaşanılan yere ulaşıldı.

print("\n")

x = re.findall(tarih, text)
print(x)
dogumTarihi = x[0] #Doğum tarihi verisinin kümede gözüken hali
print(dogumTarihi)#Doğum Tarihine ulaşıldı.

print("\n")

print("""Konuşmadaki kişinin ismi ve soyismi: {}, 
yaşı: {}, yaşadığı yer: {}, doğum tarihi: {} """.format(isimSoyisim, yas, yasadigiYer, dogumTarihi))

