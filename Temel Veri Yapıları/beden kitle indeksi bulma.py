""""Vücut Kitle Endeksi Bulma"""""
print("############# VÜCUT KİTLE ENDEKSİ HESAPLAMA #############")
print("Boyunuzu Giriniz!")
a = int(input("Boy (cm) : "))
print("Kilonuzu Giriniz!")
b = int(input("Kilo (kg) : "))
print("Vücut Kitle Endeksi Hesaplanıyor...")
vc = b /((a/100) ** 2)
vc=round(vc,1)
print("Vucüt Kitle Endeksiniz : \t {} kg/m^2 ".format(vc))
if vc <= 18.9:
    print("Zayıfsınız!! Ekmek Yiyiniz :)")
elif vc <= 24.9:
    print("Normalsiniz!! Bu Ayarda Devam Edin :)")
elif vc <= 29.9:
    print("Hafif Şişmansınız!! Göbek Erkeğin Makyajıdır Yemeye Devam :)")
elif vc <= 34.9:
    print("Obezsiniz Sağlığınız Riskte!!")

else:
    print("Aşırı Obezsiniz Sağlık Açısından Çok Risklisiniz!!")
