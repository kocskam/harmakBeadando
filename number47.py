#Hogyan tároljam ezeket?


n = int(input("Hány sort kell beolvasnom? "))
print("Sorok beolvasása:")
while n != 0:
    sor = input("A(z) " + str(n) +". sor: ")
    n -= 1
    number, hour, minute, text = sor.split(" ")
    time = hour + ":" + minute
    ready = time + " " + text