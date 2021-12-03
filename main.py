#Uzrakstit programmu, kas pieprasa no lietotaja ievadit tris lenkus un ar funkcijas palidzibu parbauda, vai sie lenki ir derigi trisstura veidosanai
def lenkuParbaude(len1,len2,len3):
  rezultats = False
  if len1+len2+len3==180:
    rezultats = True
  return rezultats

len1 = int(input("Ievadiet 1.leņķi: "))
len2 = int(input("Ievadiet 2.leņķi: "))
len3 = int(input("Ievadiet 3.leņķi: "))
rez = lenkuParbaude(len1,len2,len3)
if rez:
  print("Trisstūris eksistē!")
else:
  print("Trisstūris neeksistē!")
