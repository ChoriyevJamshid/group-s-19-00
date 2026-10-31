"""
    Sana: 22-10-2026
    Mavzu:
        - Shart operatori 
        - if, else, elif
        - is, None
"""

# boolean
# True, False


# text = "Siz maktabda o'qiysizmi ?"
# print(text)

# age = int( input( "Yoshizni kiriting: " ) )

# if age < 18:
#     answer = "Siz maktabda o'qiysiz."
#     print(answer)
# else:
#     answer = "Siz maktabda o'qimaysiz"
#     print(answer)


# print("Bugun parkga aylanishga borasizmi ?")

# condition = input("Bugungi havo holati: ")

# if condition == "yaxshi":
#     msg = "Ha, boraman"
# else:
#     msg = "Yoq, bormayman"

# print(msg)


# print("Matematik misol bajaramiz.")

# num1      = float(input("Birinchi son: "))
# num2      = float(input("Ikkinchi son: "))
# operation = input("Operatisiya tanlang (-, +): ")

# if operation == "+":
#     result = num1 + num2
# else:
#     result = num1 - num2

# print(f"Natija: {result}")


# text = (
#     "Parkga kirish bilet narxlari:"
#     "\n - 5 yoshdan kichiklar uchun bepul"
#     "\n - 5 yoshdan 18 yoshgacha 5.000 so'm"
#     "\n - 18 yoshdan katta yoki tenglar uchun 10.000 so'm"
# )
# print(text)

# age = int(input("Yoshizni kiriting: "))

# if age < 5:
#     price = "bepul"
# elif 5 <= age < 18:
#     price = "5.000 so'm"
# else:
#     price = "10.000 so'm"

# message = f"Siz uchun bilet narxi {price}."
# print(message)


text = (
    "Bir kg mahsulot narxi: 5.000 so'm"
    "\n1kg olsangiz skidga yoq"
    "\n2kg dan 5kg gacha olsangiz 5%"
    "\n5kg dan 20kg gacha olsangiz 10%"
    "\n20kg dan 50kg gacha olsangiz 15%\n"
)

print(text)

kg = int(input("Olmoqchi bolgan miqdordi kiriting (kg): "))

product_price = 5000
total_price = kg * product_price

if 1 < kg < 5:
    total_price = total_price * (1 - 0.05)
elif 4 < kg < 20:
    total_price = total_price * (1 - 0.1)
elif 19 < kg < 50:
    total_price = total_price * (1 - 0.15)

print(f"Umumiy narx: {total_price} so'm.")





