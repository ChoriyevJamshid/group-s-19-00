"""
    Sana: 27-10-2026
    Mavzu:
        - if, else, elif (masalalar)
        - Loops (for), range()
"""

# Masala #1
# a = int(input("a = "))
# if a > 0:
#     a += 1
# print(f"{a = }")

# Masala #2
# a = int(input("a = "))

# if a > 0:
#     a += 1
# else:
#     a -= 2
# print(f"{a = }")


# Masala #3
# a = int(input("a = "))

# if a > 0:
#     a += 1
# elif a < 0:
#     a -= 2
# else:
#     a = 10

# print(f"{a = }")


# Masala #4
# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# counter = 0

# if a > 0:
#     counter += 1
# if b > 0:
#     counter += 1
# if c > 0:
#     counter += 1
    
# print(f"{counter = }")


# Masala #5

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# musbat, manfiy = 0, 0

# if a > 0: musbat += 1
# else: manfiy += 1

# if b > 0: musbat += 1
# else: manfiy += 1

# if c > 0: musbat += 1
# else: manfiy += 1
    
# print(f"{musbat = }")
# print(f"{manfiy = }")


# Masala #6
# a = int(input("a = "))
# b = int(input("b = "))

# if a > b:
#     print(f"Kattasi: {a = }")
# else:
#     print(f"Kattasi: {b = }")


# Masala #7
# a = int(input("a = ")) # 1
# b = int(input("b = ")) # 2

# if a < b:
#     print("Index = 1")
# else:
#     print("Index = 2")


# Masala #8
a = int(input("a = "))
b = int(input("b = "))

# if a > b:
#     print(a , b, sep=" => ")
# else:
#     print(b, a, sep=" => ")

if a < b:
    c = a + b
    a = c - a
    b = c - b

print(f"{a = }", f"{b = }", sep=" | ")



