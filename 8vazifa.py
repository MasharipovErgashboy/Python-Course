def qoshish(a, b):
    return a + b
a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
natija = qoshish(a, b)
print("Natija:", natija)




def is_palindrome(matn):
    return matn == matn[::-1]
matn = input("Matn kiriting (palindromligini tekshirish uchun): ")
natija = is_palindrome(matn)
print("Palindrome:", natija)





def faktorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)
n = int(input("Faktorialini hisoblash uchun son kiriting: "))
natija = faktorial(n)
print(f"{n}! = {natija}")



