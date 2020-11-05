#This is a simple bank application 
#Authors:Halil,Taha,Alp
#Date:2020 October

def işlemyap(tercih2,kullanıcıhesap):
    if tercih2 == "1":

        miktar = float(input("çekmek istediğiniz miktarı girin:"))

        if miktar < kullanıcıhesap:

            kullanıcıhesap -= miktar 

            print("kalan bakiyeniz ",kullanıcıhesap," $ dır.")

        elif miktar > kullanıcıhesap:

            print("yeterli bakiyeniz yok !!")

    elif tercih2 == "2":

        miktar = float(input("yüklemek istediğiniz miktarı girin:"))

        kullanıcıhesap += miktar

        print("hesap bakiyeniz ",kullanıcıhesap, " $ dır.")
    
    elif tercih2 == "3":

        print("tekrar bekleriz")
        
    else:
        print("bir işlem seçtiğinizden emin olun !!")

def karşılamayap(kullanıcıadı,kullanıcıhesap):

    print("hoşgeldin ",kullanıcıadı)
    print("bakiyeniz: ",kullanıcıhesap," $ dır")
    tercih = input("1:para çekmek için\n2:para yüklemek için\n3:çıkmak için\n")

    return tercih

def context():
    
    text = open("C:\\Users\\Halil\\OneDrive\\Masaüstü\\Python With HAT\\kullanıcılar.txt","r",encoding="utf-8")
    obj=text.readlines()
    i = 0
    kullancı=list()

    while i < 3:
        veri = obj[i].split(",")
        kullancı.append(veri)
        i+=1
    return kullancı

def uptadeContext():
        #burada dosya güncelleme işlemi yapılacak kişinin hangi satırda olduğunun bilinmessi için id eklenecek
        #ve id okunarak o satır silinip tekrar güncellenecek

    pass

def girişkontrol(username,password):
    kullanıcı = context()
    for i in kullanıcı:

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
        veri = girişkontrol(username,password)
        if veri != None:
            
            kullanıcı = veri[0]
            hesap = veri[2]
            hesap = float(hesap[:4])

            tercih = karşılamayap(kullanıcı,hesap)
        
            işlemyap(tercih,hesap)

            yenidenişlemkontrol = input("başka bir işlem yapmak ister misin (evet/hayır):")

            if yenidenişlemkontrol == "evet":
                control = True
            elif yenidenişlemkontrol == "hayır":
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


















