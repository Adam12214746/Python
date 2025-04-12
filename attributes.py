string = "sun'iy intellekt" #b
print (len(string))
print (string.upper())
print (string.lower())
print (string[3],string[5])
matn = input("matn kiriting: ")
if len(matn) < 5:
    print("matn 5ta harfdan kam")
elif len(matn) > 5:
   print("matn 5ta harfdan kop")
else:
   print("matn 5ta harfga teng")
matn = input("matn kiriting: ")
if "a" and "A" in matn :
   print("matnda <A>,<a> harflari bor")
elif "A" in matn :
   print("matnda <A> harfi bor")
elif "a" in matn :
   print("matnda <a> harfi bor")
else :
   print("matnda <A>,<a> harflari yoq")
raqam = float(input("raqam: "))
if raqam < 0:
   print(raqam, " musbat raqam")
elif raqam > 0:
   print(raqam, " manfiy raqam")
else
   print(raqam, " raqam nolga teng")
matn = input("matn yoki raqam kiriting: ")

reversed_matn = matn[::-1]

print("teskari natija:", reversed_matn)
ism = str(input("Ism : "))
familiya = str(input("Familiya : "))
if ism and familiya:
   print(ism[0].upper() + " " + familiya[0].upper())
import math
a = float(input("To'g'ri to'rtburchakning A tarafi: "))
b = float(input("To'g'ri to'rtburchakning B tarafi: "))
perimetr = (a + b) * 2
yuzi = a*b
print("perimetr = ", perimetr)
print("yuzi = ", yuzi)
string = str("StrIng")
yangi_string = string.replace("StrIng", "string")
print(yangi_string)
ism = str("Firdavs")
string = str("sun'iy intellekt")
print(f"{ism}  {string} ni yaxshi koradi")

Feedback: Good!
