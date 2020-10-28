

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


taha = "taha" 
tahap="123"
tahah = 58.0

halil = "halil"
halilp = "456"
halilh = 42.0

alp = "alp"
alpp = "789"
alph = 100.0


control = True
username = input("kullanıcı adını giriniz:")
password = input("parolanızı girin:")
while control:

    if username == taha and password == tahap:
        print("hoşgeldin taha !!")
        print("bakiyeniz: ",tahah," $ dır")
        tercih = input("1:para çekmek için\n2:para yüklemek için\n3:çıkmak için\n")
        işlemyap(tercih,tahah)

        yenidenişlemkontrol = input("başka bir işlem yapmak ister misin (evet/hayır):")

        if yenidenişlemkontrol == "evet":
            control = True
        elif yenidenişlemkontrol == "hayır":
            control = False

    elif username == halil and password == halilp:
        print("hoşgeldin halil !!")
        print("bakiyeniz: ",halilh," $ dır")
        tercih = input("1:para çekmek için\n2:para yüklemek için\n3:çıkmak için\n")
        işlemyap(tercih,halilh)

        yenidenişlemkontrol = input("başka bir işlem yapmak ister misin (evet/hayır):")

        if yenidenişlemkontrol == "evet":
            control = True
        elif yenidenişlemkontrol == "hayır":
            control = False


    elif username == alp and password == alpp:
        print("hoşgeldin alp !!")
        print("bakiyeniz: ",alph," $ dır")
        tercih = input("1:para çekmek için\n2:para yüklemek için\n3:çıkmak için\n")
        işlemyap(tercih,alph)
        
        yenidenişlemkontrol = input("başka bir işlem yapmak ister misin (evet/hayır):")

        if yenidenişlemkontrol == "evet":
            control = True
        elif yenidenişlemkontrol == "hayır":
            control = False

    else:
        print("kullanıcı adı ya da parola hatalı !!")


