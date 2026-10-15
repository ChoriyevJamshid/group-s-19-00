"""
    Sana: 10-10-2026
"""

# 1, 2, 3, 0, -1, -2 -> int
# 5.7, -0.6, 89.34   -> float
# "salom", "sms"     -> str
# True, False        -> bool


# a = 5
# b = 9.4
# c = "Salom"
# d = True

# x = 10 > 5      # True
# y = 45 < 4 * 12 # True

# print(f"{x = }")
# print(f"{y = }")


# a = [ 1, 2, 3, 4, 5 ]
# b = [ "cobalt", "lacetti", "malibu" ]
# c = [True, False, True, True, False]

# print(a)
# print(b)
# print(c)


# yillar = [2000, 2001, 2002, 2003]
# mylist = [10, -8.9, True, "Hello", "Salom", True, False, 1]
# lst1   = []

# print( type(yillar) )

# int, float, str, bool, list

# Ro'yhat methodlari

"""
    append, insert, extend,
    copy, sort, reverse, index, clear, count
    remove, pop, 
"""


# lst = []
# print(lst)


# cars = ['cobalt', 'malibu', 'lacetti', 'captiva', 'nexia']
# a = cars[0]
# print(a)
# print(cars[4])

# print( cars[0:3] )
# print( cars[3:5] )

# meva = input("Meva kiriting: ")

# mevalar = []
# print( mevalar )

# mevalar.append('olma')
# mevalar.append('shaftoli')
# mevalar.append('banan')

# print(mevalar)


# mevalar = ['olma', 'shaftoli', 'banan']
# mevalar.append('apelsin')
# mevalar.insert(2, 'apelsin')
# print(mevalar)


# mevalar  = [ 'olma', 'anor', 'uzum' ]
# mevalar2 = [ 'apelsin', 'banan' ]
# mevalar.extend(mevalar2)
# print(mevalar)


markalar = [
    'bmw', 'chevrolet', 'mercedes', 'ferrari',
    'audi', 'nissan', 'audi', 'chevrolet'
]

print(markalar)

markalar.pop(3)
markalar.pop(0)
print(markalar)

markalar.remove('chevrolet')
markalar.remove('audi')
print(markalar)

# numbers = [ 1, 4, 2, 3, 4, 5,  ]
# numbers.remove(4)
# print(numbers)

