print(5+5)
print(5-1)
print(5*2)
print(15//10)
print(15%10)

#2
print(2+3*4**2)

#3
print(5 == 5)
print(10 != 3)
print(4 > 8)
print(7 <= 7)

#4
a = True
b = False
print(a and b)  
print(not(a) or b)   
print(not b)    

#5
son = 43
birinchi_raqam = son // 10
ikkinchi_raqam = son % 10

yigindi = birinchi_raqam + ikkinchi_raqam
print(f"Natija: {birinchi_raqam} + {ikkinchi_raqam} = {yigindi}")

#6
son = 321
teskari_son = int(str(son)[::-1])

print(f"Natija: {teskari_son}")
