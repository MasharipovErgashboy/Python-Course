mahsulot_narxi = float(input("Mahsulot narxi: "))
chegirma_foizi = float(input("Chegirma foizi: "))
chegirma = mahsulot_narxi * (chegirma_foizi / 100)
yangi_narx = mahsulot_narxi - chegirma
print(f"Chegirma: {chegirma}")
print(f"Yangi narx: {yangi_narx}")



a = float(input("Tomon a: "))
b = float(input("Tomon b: "))
c = float(input("Tomon c: "))
perimetr = a + b + c
s = perimetr / 2
yuza = (s * (s - a) * (s - b) * (s - c)) ** 0.5
print(f"Perimetr: {perimetr}")
print(f"Yuza: {yuza}")



kredit_miqdori = float(input("Kredit miqdori: "))
foiz_stavkasi = float(input("Yillik foiz stavkasi: "))
kredit_muddati = int(input("Kredit muddati (yil): "))
yillik_foiz = kredit_miqdori * (foiz_stavkasi / 100)
umumiy_qarz = kredit_miqdori + (yillik_foiz * kredit_muddati)
print(f"Yillik foiz: {yillik_foiz}")
print(f"Umumiy qarz miqdori: {umumiy_qarz}")
