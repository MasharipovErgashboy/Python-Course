mahsulot_narxi = int(input("Mahsulot narxi: "))
chegirma_foizi = int(input("Chegirma foizi: "))
chegirma = mahsulot_narxi * (chegirma_foizi / 100)
yangi_narx = mahsulot_narxi - chegirma
print("Chegirma: " + str(chegirma))
print("Yangi narx: " + str(yangi_narx))


a = int(input("Tomon a: "))
b = int(input("Tomon b: "))
c = int(input("Tomon c: "))
perimetr = a + b + c
s = perimetr / 2
yuza = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print("Perimetr: " + str(perimetr))
print("Yuza: " + str(yuza))


kredit_miqdori = int(input("Kredit miqdori: "))
foiz_stavkasi = int(input("Yillik foiz stavkasi: "))
kredit_muddati = int(input("Kredit muddati (yil): "))
yillik_foiz = kredit_miqdori * (foiz_stavkasi / 100)
umumiy_qarz = kredit_miqdori + (yillik_foiz * kredit_muddati)
print("Yillik foiz: " + str(yillik_foiz))
print("Umumiy qarz miqdori: " + str(umumiy_qarz))

