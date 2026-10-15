"""
    Sana:   13-10-2026
    Mavzu:  
        - List (ro'yxat)lar bilan ishlash
        - index, slicing
        - List methodlari
"""

# a = 5
# b = 5.6
# c = "salom"
# d = True

# numbers = [ 1, 2, 3, 4, 5, 6 ]
# words = [ "salom", "alek", "hayrli mong", "hayrli kech" ]
# products = [ "apple", "carrot", "bread"]
# prices = [15000, 20000, 40000, 100000]
# cars = ["cobalt", "gentra", "malibu", "onix"]

# mylist = [ 100, "hello", True, -87.25, False, "@" ]
# mylist1 = []



# prices = [ 15_000, 20_000, 40_000, 100_000, 150_000 ]

# count = len(prices)
# print(f"Ro'yxat uzunligi: {count}")

# a1 = prices[2]
# print(f"{a1 = }")

# a2 = prices[4]
# print(f"{a2 = }")


# prices = [ 15_000, 20_000, 40_000, 100_000, 150_000 ]
# print("\n", prices, "\n")

# mevalar = [ "olma", "anor", "nok", "uzum", "behi", "anjir" ]

# m2 = mevalar[0:3] # start:stop:step
# m3 = mevalar[3:6] 

# print(f"{m2 = }")
# print(f"{m3 = }")

# m4 = mevalar[0:6:2]
# print(f"{m4 = }")


"""
    .append(element) - listga element qo'shib beradi
    .insert(index, element) - listga ko'rsatilga indexga element qo'shib beradi
"""


mylist = []

mylist.append( "nissan" )
mylist.append( "ferrari" )

mylist.append( "bmw" )
mylist.append( "mercedes" )
mylist.append( "audi" )

# mylist.insert(2, 'lamborgini')
mylist.insert(0, 'lamborgini')

print(f"\n {mylist = } \n")