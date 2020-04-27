import operator

def showConsole(list):

    # for i in range(len(list)):
    #     print(list[i])
    #     num = 1
    #     for j in list:
    #         print(num, ".", j[1], "", j[2])
    #         num += 1

    # print(list[0][0])
    # print(list[1])

    # for i in range(len(list)):
    #     print(list[i])
    #     num = 1
    #     for k in range(len(list)):
    #         # print(k)
    #         print(f'{num:>8}. {list[k][1]:>1} {list[k][2]:>1}')
    #         num += 1

    # print(len(list))
    # print(len(list[0]))
    #
    # for i in range(len(list)):
    #     print(list[i][0])
    #     for j in range(len(list[0])):
    #         print(list[j][1])
    #         print(list[j][2])

    # print(list[0][0])
    # print(list[0][1])
    # print(list[0][2])

    for i in range(len(list)):
        print(list[i][0])
        num = 1
        for j in range(2, len(list[0])):
            print(f'{num:>8}. {list[i][1]:>1} {list[i][2]:>1}')
            # print(list[i][1])
            # print(list[i][2])
            num += 1

    # num = 1
    #
    # for i in list:
    #     print(i[0])
    #     print(num,".", i[1], "", i[2])
    #     num += 1

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
        time = darabok[1] + ":" + darabok[2]
        text = ""
        for i in range(3, len(darabok)):
            text += darabok[i]
            text += " "

    except ValueError:
        print("Hibás bemenet!")
        continue

    n -= 1

    # time = hour + ":" + minute
    ready = time + " " + text
    number = int(number)
    ready = str(ready)

    list.append((number, time, text))

list = sorted(list, key = operator.itemgetter(1, 2))
print(list)

showConsole(list)
