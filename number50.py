#függvények
def toSecundum(ms, min, hour):
    return ms + min*60 + hour*3600

def disIsOkay():
    while True:
        dis = input("Kérem az útszakasz hosszát: ")
        if dis == "" or int(dis) < 1:
            continue
        return int(dis)

def limIsOkay():
    while True:
        lim = input("Kérem a sebességkorlátot: ")
        if limit == "" or int(lim) < 0:
            continue
        return int(lim)

#program
distance = disIsOkay()
limit = limIsOkay()

lawBreakers = []
r = ""
while r != "end":
    r = input("Beolvasás befejezéséhez írjon 'end'-et! ")
    if r == "end":
        break
    ora1, perc1, ms1, ora2, perc2, ms2, rendszam = r.split((" "))
    #                                                                                                                      ellenőrizni, hogy a perc pl nem e több 60-nál
    # ido2 = ora2 + ":" + perc2 + ":" + ms2

    sec1 = toSecundum(int(ms1), int(perc1), int(ora1))
    sec2 = toSecundum(int(ms2), int(perc2), int(ora2))

    ido = int(sec2)-int(sec1)

    kisTav = distance/ido
    nagyTav = kisTav * 3.6

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