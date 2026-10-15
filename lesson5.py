"""
    Sana: 15-09-2026
    Mavzu: 
        - input(), int(), float(), str()
""" # Dokumentatsiya

# Ma'lumot: sonlar va matnlar

# O'zgaruvchilari orqali ma'lumot saqlaymiz
# O'zgaruvchida 3ta xususiyat:
# nomi, qiymati, tipi

a = 5    # int
b = "10" # str
c = 5.8  # float

# print( type(a) )
# print( type(b) )
# print( type(c) )

# print() - chiqarish operatori
# input() - kiritish operatori


# input( "Ism kiriting: " )
# input( "Yoshizni kiriting: " )
# input( "E-pochta kiriting: " )
# age = input( ">>>> " )
# print( age, " -- ", type(age) )

# yosh = input( "Yoshingiz nechada: " )
# yosh = int(yosh)
# t_yil = 2026 - yosh

# print("Tug'ilgan yil:", t_yil)


# b_date = input("T. yilni kiriting: ")
# b_date = int(b_date)

# yosh = 2026 - b_date
# print("Sizning yoshingiz:", yosh)


# num1 = 55    # int
# print(num1, " -- ", type(num1))

# # num1 = float(num1)
# num1 = str(num1)
# print(num1, " -- ", type(num1))

# num2 = 10.25 # float
# print(num2, " -- ", type(num2))

# num2 = str(num2)
# print(num2, " -- ", type(num2))

# int() -> ma'lumotni "int" qilib beradi
# float() -> ma'lumotni "float" qilib beradi
# str() -> ma'lumotni "str" qilib beradi 


############ Masalalar ############ 

# Masala #1

# a = input("Kvadrat tomoni: ") # str
# a = int(a)
# p = 4 * a
# print("Kvadrat perimetri:", p)

# Masala #2
a = input( "Kvadrat tomoni: " )
a = float(a)
s = a ** 2
print("Kvadrat yuzasi:", s)
