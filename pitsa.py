#Pitsa pindala diameetri jargi
from math import pi
import math




print("Tere, mis on teie pitsa diameeter sentimeetrites ?")
diam = int(input())
raad = diam * 0.5
pind = pi * raad * raad
pindlopp = (round(pind,2))
print("Teie pitsa on " + str(pindlopp) + " ruut cm!")
