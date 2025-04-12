def tarozi():
    tanlov = input("agar kg->pound ni tanlamoqchi bosangiz a ni bosing"
                   "pound-> kg ni tanlash uchun b ni kiriting: ")
    if tanlov == "a":
        kg = float(input("vazn(kg): "))
        print(f'{kg} kg = {kg * 2.20462} pounds')
    elif tanlov == "b":
        pound = float(input("vazn(pound): "))
        print(f'{pound} kg = {pound / 2.20462} pounds')
    else:
        print("Faqat a yoki b ni kiriting!: ")

def termometr():
    tanlov = input("agar selsius->fahreineit ni tanlamoqchi bolsangiz a ni bosing"
                   "fahreneit->selsius ni tanlash uchun b ni kiriting: ")
    if tanlov == "a":
        celsius = float(input("harorat(celsius): "))
        print(f"{celsius} C = {(celsius * 9/5 + 32)} F")
    elif tanlov == "b":
        fahreneit = float(input("harorat(fahreneit): "))
        print(f"{fahreneit} F = {(fahreneit - 32) * 5/9} C")
    else:
        print("Faqat a yoki b ni kiriting!: ")
def main():
    tanlov = input("tarozi uchun a ni kiriting termometr uchun b ni kiriting: ")
    if tanlov == "a":
        tarozi()
    elif tanlov == "b":
        termometr()
    else:
        print("Faqat a yoki b ni kiriting!: ")

# Script run bo'lishi uchun main() qilib function call qilib qo'yish kerak bo'ladi.
# Feedback: Good!
