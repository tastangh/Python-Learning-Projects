""""Dik Üçgen ALAN VE HİPOTENÜS BULMA"""
""""
  |.
a |  .  h
  |_    . 
  |_|_____.
      b
Hipotenüs Formülü: a^2 + b^2 = c^2
Alan Formülü : a*b/2
"""
print("-------------Dik Üçgen ALAN VE HİPOTENÜS BULMA-------------")
print("  |.\na |  .  h\n  |_    . \n  |_|_____.\n      b\n")
a = int(input("a: "))
b = int(input("b :"))
h= (a ** 2 + b ** 2) ** 0.5
alan=a*b/2
print("Hipotenüs = ",h)
print("Alan =",alan)
