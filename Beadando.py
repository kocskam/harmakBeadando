#29  Megoldást találni arra, hogy a belső []-t végezze el először.

# input = "2[b3[a]]"
# output = ""
#
# flag = 0
# for i in range(len(input)):
#
#     if input[i].isdigit():
#         flag = 0
#
#         k = input[i]
#         i += 2
#         repeatThisText = ""
#         numberOfSteps = 0
#
#         while input[i] != "]":
#             repeatThisText += input[i]
#             numberOfSteps += 1
#             i += 1
#
#         for j in range(int(k)):
#             output += repeatThisText
#
#         flag = i
#
#     else:
#         if i > flag:
#             output += input[i]
#
# print(output)

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
lawBreakers = []
distance = int(input("Kérem az útszakasz hosszát: "))
limit = int(input("Kérem a sebességkorlátot: "))

r = ""
while r != "end":

    r = input("Beolvasás befejezéséhez írjon 'end'-et! ")
    if r == "end":
        break
    ora1, perc1, ms1, ora2, perc2, ms2, rendszam = r.split((" "))
    #                                                                                                                      ellenőrizni, hogy a perc pl nem e több 60-nál
    # ido2 = ora2 + ":" + perc2 + ":" + ms2

    sec1 = int(ms1) + int(perc1)*60 + int(ora1)*3600
    sec2 = int(ms2) + int(perc2)*60 + int(ora2)*3600

    ido = int(sec2)-int(sec1)

    kisTav = distance/ido
    nagyTav = kisTav * 3.6

    print(nagyTav)

    #   itt a kerekítést javítani
    # if isinstance(nagyTav, float):
    #     print("dsadasdsada")
    #     nagyTav = round(nagyTav, 2)
    # else:
    #     print("ds")
    #     nagyTav = int(nagyTav)


    if nagyTav > limit:
        lawBreakers.append(rendszam + " " + str(round(nagyTav, 2)) + "km/h")
#                                                                                                                          üres tömböt lekezelni, kiírni szépen
print(lawBreakers)