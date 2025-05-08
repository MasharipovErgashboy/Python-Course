def full_name(ism, familiya="Familiyasi yo'q"):
    print(f"{ism} {familiya}")
full_name("Ali")              
full_name("Ali", "Valiyev")       



def shape_area(shape, **kwargs):
    if shape == "kvadrat":
        a = kwargs.get("a")
        if a:
            return a * a
        else:
            return "Kvadrat uchun 'a' tomoni kerak"
    elif shape == "to'g'ri to'rtburchak":
        a = kwargs.get("a")
        b = kwargs.get("b")
        if a and b:
            return a * b
        else:
            return "To‘g‘ri to‘rtburchak uchun 'a' va 'b' tomonlari kerak"
    else:
        return "Noma'lum shakl"




def sum_to_n(n):
    if n == 1:
        return 1
    else:
        return n + sum_to_n(n - 1)
print(sum_to_n(10))






