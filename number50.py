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