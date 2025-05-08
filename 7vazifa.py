matn = "dasturlash juda yaxshi dasturlash"
sozlar = matn.split()
lugat = {}
for soz in sozlar:
    if soz in lugat:  
        lugat[soz] += 1  
    else:  
        lugat[soz] = 1  
print(lugat)



foydalanuvchi = {
    "ism": "Ali",
    "yosh": 20,
    "shahar": "Andijon"
    }
foydalanuvchi["yosh"] = 21
foydalanuvchi["shahar"] = "Toshkent"
del foydalanuvchi["ism"]
print(foydalanuvchi)


sonlar = [1, 2, 2, 3, 4, 4, 5]
noyob_sonlar = set(sonlar)
print(noyob_sonlar)
