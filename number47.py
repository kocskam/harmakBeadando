#Hogyan tároljam ezeket?

while True:
    try:
        n = int(input("Hány sort kell beolvasnom? "))
    except ValueError:
        print("Hibás bemenet!")
        continue
    if n <= 0:
        print("Hibás bemenet!")
        continue
    break

print("Sorok beolvasása:")
while n != 0:
    sor = input("A(z) " + str(n) +". sor: ")
    n -= 1
    number, hour, minute, text = sor.split(" ")
    time = hour + ":" + minute
    ready = time + " " + text