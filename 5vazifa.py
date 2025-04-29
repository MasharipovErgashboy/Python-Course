for son in range(10, 101, 2):
    print(son, end=", ")

son = int(input("Musbat son kiriting: "))
while son <= 0:
    print("Bu musbat son emas. Qayta kiriting")
    son = int(input("Musbat son kiriting: "))
print(f"Musbat son kiritildi: {son}")


for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end="\t")
    print()
