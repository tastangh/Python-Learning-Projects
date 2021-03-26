"""
2. dereceden bir bilinmeyenli denklemin köklerini bulma

Denklem : ax^2 + bx + c

Deltayı Hesaplama:  b ** 2 -  4 * a * c

Birinci Kök : (-b - delta ** 0.5) / (2*a)
İkinci Kök : (-b + delta ** 0.5) / (2*a)

"""
""""Kullanıcıdan Denkelmin parametrelerini  Alma Bölümü """""
print("a değerini giriniz!(Denklem : ax^2 + bx + c)")
a = int(input("a:"))
print("b değerini giriniz!(Denklem : ax^2 + bx + c)")
b = int(input("b:"))
print("c değerini giriniz!(Denklem : ax^2 + bx + c)")
c = int(input("c:"))
print("Kökler Hesaplanıyor...")

""" Delta Hesaplama"""
delta = b ** 2 - 4 * a * c
x1 = (-b - delta ** 0.5) / (2*a)
x2 = (-b + delta ** 0.5) / (2*a)

""""Ekrana Sonuç Yazdırma """
print("Birinci Kök: {}\nİkinci Kök : {}\n".format(x1,x2))
print("Kökler Hesaplanmıştır!")
