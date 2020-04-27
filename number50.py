#függvények
def toSecundum(ms, min, hour):
    return ms + min*60 + hour*3600

def disIsOkay():
    while True:
        dis = input("Kérem az útszakasz hosszát: ")
        if dis == "" or int(dis) < 1:
            print("Hibás bemenet!")
            continue
        return int(dis)

def limIsOkay():
    while True:
        lim = input("Kérem a sebességkorlátot (km/h): ")
        if lim == "" or int(lim) < 0:
            print("Hibás bemenet!")
            continue
        return int(lim)

def timeIsOkay(sec, min, hour):
    try:
        sec = int(sec)
        min = int(min)
        hour = int(hour)
        if hour == 24 and (sec != 0 or min != 0):
            return False
        return sec >= 0 and sec < 60 and min >= 0 and min < 60 and hour >= 0 and hour < 25
    except ValueError:
        print("Hibás időpont!")

#main
distance = disIsOkay()
limit = limIsOkay()

ruleBreakers = []
r = ""

while r != "end":
    r = input("Beolvasás befejezéséhez írjon 'end'-et! ")
    if r == "end":
        break
    try:
        ora1, perc1, ms1, ora2, perc2, ms2, rendszam = r.split((" "))
    except ValueError:
        print("Hibás bemenet!")
        continue

    if timeIsOkay(ms1, perc1, ora1) and timeIsOkay(ms2, perc2, ora2):
        sec1 = toSecundum(int(ms1), int(perc1), int(ora1))
        sec2 = toSecundum(int(ms2), int(perc2), int(ora2))
    else:
        print("Hibás időpont!")
        continue

    ido = int(sec2)-int(sec1)
    if ido <= 0:
        print("Hibás időpont!")
        continue

    kisTav = distance/ido
    nagyTav = kisTav * 3.6
    nagyTav = round(nagyTav, 2)

    f = nagyTav - int(nagyTav)
    if f == 0:
        nagyTav = int(nagyTav)
    else:
        nagyTav = round(nagyTav, 2)

    if nagyTav > limit:
        ruleBreakers.append(rendszam + " " + str(nagyTav) + "km/h")

if len(ruleBreakers) == 0:
    print("Senki nem lépte át a sebességhatárt!")
else:
    for i in ruleBreakers:
        print(i)