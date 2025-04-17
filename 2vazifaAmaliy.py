# print("Masharipov Ergashboy")

# fullName = "Masharipov Ergashboy"
# nickName = "I'm_Masharipov"
# age = 21
# salaryByMonth = 10.000

# print(type(fullName),fullName)
# print(type(age),age)
# print(type(salaryByMonth),salaryByMonth)


text = "Salom, dunyo!"
print(text.upper())  # Katta harflar bilan
print(text.lower())  # Kichik harflar bilan
print(text.capitalize())  # Birinchi harf katta, qolganlari kichik
print(text.title())  # Har so'zning birinchi harfi katta
print(text.split()) # So'zlarga ajratish
print(text.replace("Salom", "Salom, aziz"))  # Matnni almashtirish
print(text.find("dunyo"))  # Matndagi "dunyo" so'zining indeksi
print(text[7:13])
print(len(text))  # Matn uzunligi
print(text.count("o"))  # "o" harfi necha marta uchraydi
contact = 1212121222
yangiHarf = text[0:5] + '5'
print(yangiHarf)
print(text.isalpha())