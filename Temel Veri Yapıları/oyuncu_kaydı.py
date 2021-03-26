print("Oyuncu Kaydetme Programı")

ad =input("Oyuncunun Adı : ")
nick =input("Oyuncunun Nicki : ")
takım = input("Oyuncunun Tuttuğu Takım : ")

bilgiler = [ad,nick,takım]

print ("Bilgiler Sisteme Yükleniyor...")

print("Ad: {} \nNick: {} \nTakım: {}\n ".format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler Sisteme Yüklenmiştir!")