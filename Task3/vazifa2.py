print("=== Maxsus kalkulyator ===")
a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))

print("\nNatijalar:")

# 1. Qo‘shish
print("1. Qo‘shish:", a + b)

# 2. Ayirish
print("2. Ayirma (a - b):", a - b)

# 3. Ko‘paytirish
print("3. Ko‘paytma:", a * b)

# 4. Bo‘lish (a/b)
if b != 0:
    print("4. Bo‘linma (a / b):", a / b)
else:
    print("4. Bo‘linma: Nolinchi bo‘lish mumkin emas!")

# 5. Qoldiq
if b != 0:
    print("5. Qoldiq (a % b):", a % b)
else:
    print("5. Qoldiq: Nolinchi bo‘lish mumkin emas!")

# 6. Butun bo‘linma
if b != 0:
    print("6. Butun qism (a // b):", a // b)
else:
    print("6. Butun qism: Nolinchi bo‘lish mumkin emas!")

# 7. Kvadratlar
print("7. Kvadratlar: a^2 =", a**2, ", b^2 =", b**2)

# 8. Daraja (a^b)
print("8. Daraja (a^b):", a ** b)

# 9. Ko‘paytma va yig‘indini solishtirish
kopaytma = a * b
yigindi = a + b
solishtirish = kopaytma > yigindi
print("9. Ko‘paytma yig‘indidan katta (a*b > a+b):", solishtirish)
