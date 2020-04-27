#29  Megoldást találni arra, hogy a belső []-t végezze el először.

input = "a1[b3[a]]"
#Kivételek: ha nem kell kódolni semmit, ha hibás az input(nincs szám a zárójel előtt, nem egyenlő a zárójelek száma), ha nem add meg egyáltalán semmit
# input = input("Kérem a kódolt szöveget!")

def inputIsWrong(input, db1):
    # db3 = sum(c == "[" for c in input)
    db2 = 0
    for i in range(len(input)):
        if input[i] == "[":
            db2 += 1
            if isinstance(input[i-1], int):
                return True
    numbers = sum(c.isdigit() for c in input)
    if db1 == db2 and numbers == db1:
        return False
    return True

def stillNeedWorking(final):
    if final.find("[") == -1:
        return False
    return True

def convertToMakeSense(input):
    # ha több van
    db = sum(i == "]" for i in input)
    if inputIsWrong(input, db):
        print("Hibás bemenet!")
        return

    if db == 0:
        return print("Mit kell itt dekódolni?")

    #pozícionálás
    for j in range(len(input)):
        if input[j] == "[":
            db -= 1
        if db == 0:
            break

    #ennyiszer kell ismételni
    numberOfRepeats = input[j - 1]

    newOutput = ""
    for x in range(j-1):
        newOutput += input[x]

    repeatThisText = ""
    numberOfSteps = 0

    #ezt kell ismételni
    ind = j+1
    while input[ind] != "]":
        repeatThisText += input[ind]
        numberOfSteps += 1
        ind += 1

    for j in range(int(numberOfRepeats)):
        newOutput += repeatThisText

    for j in range(ind+1, len(input)):
        newOutput += input[j]

    if stillNeedWorking(newOutput):
        convertToMakeSense(newOutput)
    else:
        print("A dekódolt szöveg: ",newOutput)

convertToMakeSense(input)

#47  Hogyan tároljam ezeket?


# n = int(input("Hány sort kell beolvasnom? "))
# print("Sorok beolvasása:")
# while n != 0:
#     sor = input("A(z) " + str(n) +". sor: ")
#     n -= 1
#     number, hour, minute, text = sor.split(" ")
#     time = hour + ":" + minute
#     ready = time + " " + text


#50
# lawBreakers = []
# distance = int(input("Kérem az útszakasz hosszát: "))
# limit = int(input("Kérem a sebességkorlátot: "))
#
# r = ""
# while r != "end":
#
#     r = input("Beolvasás befejezéséhez írjon 'end'-et! ")
#     if r == "end":
#         break
#     ora1, perc1, ms1, ora2, perc2, ms2, rendszam = r.split((" "))
#     #                                                                                                                      ellenőrizni, hogy a perc pl nem e több 60-nál
#     # ido2 = ora2 + ":" + perc2 + ":" + ms2
#
#     sec1 = int(ms1) + int(perc1)*60 + int(ora1)*3600
#     sec2 = int(ms2) + int(perc2)*60 + int(ora2)*3600
#
#     ido = int(sec2)-int(sec1)
#
#     kisTav = distance/ido
#     nagyTav = kisTav * 3.6
#
#     print(nagyTav)
#
#     #   itt a kerekítést javítani
#     # if isinstance(nagyTav, float):
#     #     print("dsadasdsada")
#     #     nagyTav = round(nagyTav, 2)
#     # else:
#     #     print("ds")
#     #     nagyTav = int(nagyTav)
#
#
#     if nagyTav > limit:
#         lawBreakers.append(rendszam + " " + str(round(nagyTav, 2)) + "km/h")
# #                                                                                                                          üres tömböt lekezelni, kiírni szépen
# print(lawBreakers)