#Plaadid
import math

print("Tere, mis on teie plaadi küljepikkus sentimeetrites ?")
a = int(input())
print("Mis on teie seina laius sentimeetrites ?")
b = int(input())
print("Mis on teie seina pikkus sentimeetrites ?")
c = int(input())

seinplaat = int(a**2)
sein = int(b * c)
vaja = sein / seinplaat
vaja2 = (math.ceil(vaja))

print("Teil läheb vaja " + str(vaja2) + " seinaplaati.")
      