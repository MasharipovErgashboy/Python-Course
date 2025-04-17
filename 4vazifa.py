# son = int(input("Sonni kiriting: "))
# if son > 0:
#     print("Musbat son.")
# elif son < 0:
#     print("Manfiy son.")
# else:
#     print("Son nolga teng.")



# baho = int(input("Bahoni kiriting: "))

# if baho >= 90:
#     print("A'lo")
# elif 75 <= baho <= 89:
#     print("Yaxshi")
# elif 50 <= baho <= 74:
#     print("Qoniqarli")
# else:
#     print("Qoniqarsiz")



a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))

if a >= b and a >= c:
    print(f"Eng katta son: {a}")
elif b >= a and b >= c:
    print(f"Eng katta son: {b}")
else:
    print(f"Eng katta son: {c}")
