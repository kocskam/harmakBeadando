import operator

def timeIsOkay(hour, min):
    try:
        min = int(min)
        hour = int(hour)
        if hour == 24 and min != 0:
            return False
        return min >= 0 and min < 60 and hour >= 0 and hour < 25
    except ValueError:
        print("Hibás időpont!")

def showConsole(list):
    num = 1
    flag = 1
    for i in range(len(list)):

        if flag == 1:
            print(list[i][0])
        elif list[i-1][0] != list[i][0]:
            print(list[i][0])
            num = 1

        for j in range(2, len(list[0])):
            flag = 0
            print(f'{num:>8}. {list[i][1]:>1} {list[i][2]:>1}')
            num += 1

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

list = []

while n != 0:
    sor = input("A(z) " + str(n) +". sor: ")

    try:
        darabok = sor.split(" ")
        number = darabok[0]
        if timeIsOkay(darabok[1], darabok[2]):
            time = darabok[1] + ":" + darabok[2]
        else:
            print("Hibás időpont!")
            continue
        text = ""
        for i in range(3, len(darabok)):
            text += darabok[i]
            text += " "

    except ValueError:
        print("Hibás bemenet!")
        continue

    n -= 1

    ready = time + " " + text
    number = int(number)
    ready = str(ready)

    list.append((number, time, text))

list = sorted(list, key = operator.itemgetter(1, 2))

showConsole(list)
