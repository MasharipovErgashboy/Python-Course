matn = "dasturlash juda yaxshi dasturlash"
sozlar = matn.split()
lugat = {}
for soz in sozlar:
    if soz in lugat:  
        lugat[soz] += 1  
    else:  
        lugat[soz] = 1  
print(lugat)
