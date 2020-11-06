#This is a simple bank application 
#Authors:Halil,Taha,Alp
#Date:2020 October

def islemyap(tercih2,kullanıcıhesap):
    if tercih2 == "1":

        miktar = float(input("çekmek istediğiniz miktarı girin:"))

        if miktar < kullanicihesap:

            kullanicihesap -= miktar 

            print("kalan bakiyeniz ",kullanicihesap," $ dır.")

        elif miktar > kullanicihesap:

            print("yeterli bakiyeniz yok !!")

    elif tercih2 == "2":

        miktar = float(input("yüklemek istediğiniz miktarı girin:"))

        kullanicihesap += miktar

        print("hesap bakiyeniz ",kullanicihesap, " $ dır.")
    
    elif tercih2 == "3":

        print("tekrar bekleriz")
        
    else:
        print("bir işlem seçtiğinizden emin olun !!")

def karsilamayap(kullaniciadi,kullanicihesap):

    print("hoşgeldin ",kullaniciadi)
    print("bakiyeniz: ",kullanicihesap," $ dır")
    tercih = input("1:para çekmek için\n2:para yüklemek için\n3:çıkmak için\n")

    return tercih

def context():
    
    text = open("C:\\Users\\Halil\\OneDrive\\Masaüstü\\Python With HAT\\kullanıcılar.txt","r",encoding="utf-8")
    obj=text.readlines()
    i = 0
    kullanci=list()

    while i < 3:
        veri = obj[i].split(",")
        kullanci.append(veri)
        i+=1
    return kullanci

def uptadeContext():
        #burada dosya güncelleme işlemi yapılacak kişinin hangi satırda olduğunun bilinmessi için id eklenecek
        #ve id okunarak o satır silinip tekrar güncellenecek

    pass

def giriskontrol(username,password):
    kullanici = context()
    for i in kullanici:

        if username == i[0] and password == i[1]:
            return i
        else:
            continue
    return None
    
def main():
    
    username = input("kullanıcı adını giriniz:")
    password = input("parolanızı girin:")

    control = True

    while control:
        veri = giriskontrol(username,password)
        if veri != None:
            
            kullanici = veri[0]
            hesap = veri[2]
            hesap = float(hesap[:4])

            tercih = karsilamayap(kullanici,hesap)
        
            islemyap(tercih,hesap)

            yenidenislemkontrol = input("başka bir işlem yapmak ister misin (evet/hayır):")

            if yenidenislemkontrol == "evet":
                control = True
            elif yenidenislemkontrol == "hayır":
                control = False
            else:
                print("bir sorun oluştu")
                control = False
        elif veri == None:
            print("böyle bir kullanıcı yok")
            control = False
        else:
            print("bir hata oluştu")
            control=False

main()


















