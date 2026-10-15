"""
    Sana: 26-09-2026
    Mavzu:
        - matnlar bilan
        - o'zgaruvchilar bilan ishlash
        
    methods:
        - count, index, find, replace, join, split, strip, rstrip, lstrip
"""

# t1 = "assalomu alaykum"
# l_count = t1.count("l")

# print(t1.count("l"))
# print(l_count)
# .count() - berilagan harf yoki so'z nechta marta
#            ishtikor etganini aniqlab beradi

# t2 = "i love python."
# print( t2.index("l") )
# print( t2.index("w") )
# .index() - berilgan belgi yoki so'z qaysi
#            indeksda joylashganini ko'rsatadi,
#            topolmasa xatolik qaytaradi

# t2 = "i love python."
# print( t2.find("w") )
# .find() - berilgan belgi yoki so'z qaysi
#           indeksda joylashganini ko'rsatadi,
#           topolmasa -1 qaytaradi


# t3 = "Assalomu alaykuk, #####"
# t3 = t3.replace("#####", "Jamshid.") 
# print(t3)
# .replace() - matnni boshqa bir matnga almashtiradi,
#              als matnni o'zgartirmaydi

# t4 = "          Hello world         "
# t4 = t4.strip()
# print(t4)
# .strip() - matni boshidagi va oxiridagi
#            ortiqcha bo'shliqlarni olib tashlaydi.


# t5 = "          Hello world         "
# print( t5.lstrip() )
# print( t5.rstrip() )
# .rstrip() - o'ng tomondagi boshliqlarni olib tashlaydi
# .lstrip() - chap tomondagi boshliqlarni olib tashlaydi

# products = ["sabzi", "guruch", "go'sht", "piyoz"]
# text1 = "Men olishim kerak bo'lgan mahsulotlar: "
# text2 = ", ".join(products)

# text = text1 + text2 + "."
# print(text)

# text = "1,2,3,4,5,6,7,8,9,10"
# numbers = text.split(",")
# print(numbers)

