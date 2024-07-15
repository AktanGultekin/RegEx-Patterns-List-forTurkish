import re
import string

text = """Merhaba. ben Ahmet Bitik. 25 yaşındayım. İnşaat ustasıyım. Ankara'da oturuyorum. Doğum tarihim 05.04.2002"""

text2= """Merhaba, benim adım Aktan Gültekin. Ben 22 yaşındayım. Öğrencilik yapıyorum. İzmir'de ikamet etmekteyim. Doğum tarihim 02.03.1995"""
text3= """Selam, bana Akif Taşlı derler. Yaşım 48. İşçiyim. Tokat'da yaşıyorum. Doğum tarihim 07.08.1988"""
text4= """Selam, ben Veysel. Yaşım 35. İşçiyim. Tokat'da yaşıyorum. Doğum tarihim 07.08.1988"""
text5 = """Selam, ben Akman. Yaşım 58'dir. İşçiyim. Tokat'da yaşıyorum. Doğum tarihim 07.08.1988"""
text6 = """Selam, ben Hasan. 63 yaşındayım. İşçiyim. Tokat'da yaşıyorum. Doğum tarihim 07.08.1988"""
sample_text ="""Merhaba, ben Mehmet Kaya. 2015 yılında Sakarya Üniversitesi İnsan Kaynakları Yönetimi Bölümü’nden mezun oldum. 
Üniversite eğitimim boyunca Migros ve n11.com başta olmak üzere birçok kurumda staj yaptım. 
Stajyer pozisyonunda görev aldığım kurumlarda insan kaynakları planlaması, işe alım süreçleri ve bordrolama alanlarını öğrendim."""

texts = [text,text2,text3, text4, text5, text6, sample_text] # Ne zaman mikrofondan ses alınırsa bir metin değişkenine kaydedilip onu texts listesine eklenilecek.
#isim = r"Ben\s\w+\s\w+"   #isim adlı pattern ile isim soyisim alındı.
yas = r"\d+\syaş\w+"  #yas adlı pattern ile konuşmadaki yaş bilgisi elde edildi.
yasadigiYer = r"([A-İ]+'de|[A-İ]+'da (otur\w+|yaşıyor\w+))" #yasadigiYer adlı pattern ile konuşmada kişinin yaşadığı yer bilgisi elde edildi.
tarih = r"([0-3][0-9].[0-1][0-9].[0-9]{4}|[1-9]{0,2}\s\w+\s[1-9][0-9]{3})" #tarih adlı pattern ile konuşmada kişinin doğum tarihi elde edildi.

#Çoklu metinler için çoklu isim patternleri ve isim listeleri
multiAdPatterns = [r"[A|a]dım\s\w+\s\w+", r"[B|b]enim ismim\s\w+\s\w+", r"[B|b]ana\s\w+\s\w+", r"[B|b]en\s[a-zA-Z]+\s[a-zA-Z]+"]
singleAdPatterns = [r"ben\s[a-zA-Z]+\."]
isimList = []
isimler = [] # isimList ve isimler düzeltilmemiş isim listeleri
names = [] # names düzeltilmiş isim listesi

#Çoklu metinler için çoklu yaş patternleri ve yaş listeleri
yasPatterns = [r"\d+ yaşındayım", r"Yaşım \d+"]
yasList = []
yaslar = []
ages = []

# --- Çoklu ve birbirinden farklı metinlerde bulunan isimleri ayıklama fonksiyonu --- #

def isimAyiklama():
    for txt in texts:
        for pattern in multiAdPatterns:
            res = re.findall(pattern,txt)
            if len(res) == 0:
                continue
            else:
                #print(res)#Düzenlenmemiş isim listesi
                isimList.append(res)

    for pattern in singleAdPatterns:
        for txt in texts:
            res = re.findall(pattern, txt)
            if len(res) == 0:
                continue
            else:
                #print(res)#Düzenlenmemiş isim listesi
                isimList.append(res)

    for i in isimList:
        for j in i:
            isimler.append(j)
    #print(isimler)
    names = [y[4:] for y in isimler]


    for num in range(0,len(names)):
        names[num] = names[num].lstrip()
        if "." in names[num]:
            names[num] = names[num][:-1]
        #print(x)

    print(names)

isimAyiklama() #Çalışıyor
#<----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->
print("\n")
#<--- Çoklu ve birbirinden farklı metinlerde bulunan yaş bilgilerini ayıklama fonksiyonu --->#
def yasAyiklama():
    for txt in texts:
        for pattern in yasPatterns:
            res = re.findall(pattern, txt)
            if len(res) == 0:
                continue
            else:
                #print(res)
                yasList.append(res)

    """for i in yasList: #Kontrol
        print(i)"""

    for i in yasList:
        for y in i:
            yaslar.append(y)

    for i in yaslar:
        if i[0] not in string.ascii_letters:
            i = i[:2]
            ages.append(i)
            #print(i)
        else:
            i = i[6:]
            ages.append(i)
            #print(i)

    print(ages)

yasAyiklama()

#<----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------->





    



#Bu kısmın altı tekli metin ve patternler içindir. Üst kısım ise çoklu metin ve pattern için kullanılmıştır.


"""
x = re.findall(adPatterns[3], text)
print(x) # Slicing yöntemi "Ben John Doe" kalıbıyla verildiği için 4: olarak kullanıldı.
x[0] = x[0][4:]
print(x[0])


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

print("Konuşmadaki kişinin ismi ve soyismi: {}, yaşı: {},\nyaşadığı yer: {}, doğum tarihi: {} ".format(isimSoyisim, yas, yasadigiYer, dogumTarihi))"""
