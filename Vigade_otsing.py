import math # removed "* from"
print("Ruudu karakteristikud")
a=int(input('Sisesta ruudu külje pikkus => ')) # add int() to input
S=a**2
print("Ruudu pindala", S)
P=4*a
print("Ruudu ümbermõõt", P) # fix quetes '' to "
di=a*math.sqrt(2) # added t to sqrt
print("Ruudu diagonaal", round(di,2))
print()
print("Ristküliku karakteristikud") # removed exrea )
b=float(input("Sisesta ristküliku 1. külje pikkus => ")) # add int() to input
c=float(input("Sisesta ristküliku 2. külje pikkus => ")) # add int() to input
S=b*c
print('Ristküliku pindala', S) # added ' after print(
P=2*(b+c) #added multplier after 2
print("Ristküliku ümbermõõt", P)
di=math.sqrt(b**2+c**2) # switched * to **
print("Ristküliku diagonaal", round(di,1)) #added ,1) after var di
print()
print("Ringi karakteristikud")
r=float(input('Sisesta ringi raadiusi pikkus => ')) # removed the first and last extra ' and add float() to input
d=2*r # added multplier
print("Ringi läbimõõt", d) # added "," before var d
S=math.pi*r**2 # added math. to pi and removed () from pi
print("Ringi pindala", round(S,2)) # added  ",2" after var S
C=2*math.pi*r #added multplier after 2 and math. to pi and removed () from pi
print("Ringjoone pikkus", round(C,2)) ## added ",2)" after var C