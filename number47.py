#Hogyan tároljam ezeket?

while True:
    try:
        n = int(input("Hány sort kell beolvasnom? "))
        if n < 0:
            raise ValueError
        if n == 0:
            break
    except ValueError:
        print("Hibás bemenet!")
        continue
    break
dict = {}
while n != 0:
    sor = input("A(z) " + str(n) +". sor: ")

    try:
        number, hour, minute, text = sor.split(" ")
        #textnél elszökik
    except ValueError:
        print("Hibás bemenet!")
        continue

    n -= 1

    time = hour + ":" + minute
    ready = time + " " + text
    number = int(number)
    ready = str(ready)

    dict[number] = ready

print(dict)
find = 123

for key, value in dict.items():
    if key == find:
        print("Na ez?", value)

# x = sum(i == 123 for i in dict)
# print(x)