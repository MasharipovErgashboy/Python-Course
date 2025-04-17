matn = input("Matn kiriting: ")
print("Uzunligi:", len(matn))
print("Katta harflar:", matn.upper())
print("Kichik harflar:", matn.lower())


ism = input("Ismingiz: ")
fam = input("Familiyangiz: ")
tyil = int(input("Tug‘ilgan yilingiz: "))
yosh = 2025 - tyil
print("\nProfil:")
print("Ism:", ism)
print("Familiya:", fam)
print("Yosh:", yosh)


gap = input("Bir gap yozing: ")
sozlar = gap.split()
print("So‘zlar soni:", len(sozlar))
uzun_soz = max(sozlar, key=len)
print("Eng uzun so‘z:", uzun_soz)
print("Uning uzunligi:", len(uzun_soz))
