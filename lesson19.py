"""
    Sana: 31-10-2026
    Mavzu:
        - For sikli
        - continue, break
"""

# for i in range(10):
#     x = 10
#     print(f"Boshida: {x = }")
#     x += 5
#     print(f"Oxirida: {x = }")


# for i in range(10):
    # print(i)


# mevalar = [ 'olma', 'anor', 'olcha', 'ananas' ]

# for i in range(4): # start:stop:step
#     fruit = mevalar[i]
#     print(fruit)

# fruit = mevalar[0]
# print(fruit)

# fruit = mevalar[1]
# print(fruit)

# fruit = mevalar[2]
# print(fruit)

# fruit = mevalar[3]
# print(fruit)


# mevalar = [ 'olma', 'anor', 'olcha', 'ananas' ]
# for meva in mevalar:
#     print(meva)


# for i in range(11, 21): # start=1, stop=11
#     print(i)


# for x in range(1, 101, 2): # start, stop, step
#     print(x)


# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(f"{i = }")


# for i in range(1, 11):
#     if i % 2 == 1:
#         continue
#     print(f"{i = }")


# for i in range(100):
    
#     if i == 5:
#         break
    
#     print(f"{i = }")
#     input(">>> ")

# text = "Supermarketga xush kelibsiz:\n"
# print(text)

# basket = []

# for i in range(20):
    
#     product = input("Mahsulot kiriting (exit): ")
#     if product == "exit":
#         break
    
#     basket.append(product)
#     print(f"☑️ {product} savatga qo'shildi.")

# print(f"\n{basket = }")



print(f"Supermarketga xush kelibsiz:")

product_list = [
    "non", "go'sht", "qatiq", "kefir", 
    "guruch", "sabzi", "pepsi",
]

basket = []


for i in range(100):
    
    product = input("Mahsulot kiriting: ")
    
    if product == "exit":
        print(f"Haridingiz uchun raxmat!")
        break
    elif product not in product_list:
        print(f"❌ Bu mahsulot bizning ro'yhatda mavjud emas!")
        continue
    
    basket.append(product)
    print(f"✅ {product} savatga qo'shildi.")
    

for product in product_list:
    
    if product in basket:
        continue
    
    print(f"⚠️  {product} olinmagan.\n")




