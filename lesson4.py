"""
    Sana: 10-09-2026
    Mavzu: Int va Float
"""

# print() - consolga natijani chiqaradi
# input() - consoldan qiymat kiritadi
# int() - malumot tipini "integer" qilib beradi
# type() - o'zgaruvchini (ma'lumotni) turi aniqlaymiz

# variable: o'zgaruvchi - dasturdagi ma'lumotlarni saqlaydigan joy

number = 10
# O'zgaruvchi nomi: number
# O'zgaruvchi qiymati: 10
# O'zgaruvchi type: int 

a = "salom"
# O'zgaruvchi nomi: a
# O'zgaruvchi qiymati: "salom"
# O'zgaruvchi type: str

number2 = 10.5
# O'zgaruvchi nomi: number2
# O'zgaruvchi qiymati: 10.5
# O'zgaruvchi type: float

"""
Sonlar ustidagi amallar:
    - Qo'shish: +
    - Ayirish: -
    - Ko'paytirish: *
    - Bo'lish: /
    - Qoldiqni olish: %
    - Darajaga ko'tarish: **
    - Butun bo'lish: //
"""


# print( 10, 5, 100, sep=",   ")

# Masala 1

kvadrat_tomoni = input("Qiymat kiriting (m): ")
kvadrat_tomoni = int(kvadrat_tomoni)

p = 4 * kvadrat_tomoni
print("Kvadratning perimetri:", p)

# Masala 2
"""       
          b
    |-----------|
   a|           |
    |-----------|
"""

a = input("a tomonni kiriting: ")
b = input("b tomonni kiriting: ")

a = int(a)
b = int(b)

p = 2 * ( a + b )
print("P =", p)


