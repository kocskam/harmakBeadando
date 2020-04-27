input = input("Kérem a kódolt szöveget!")

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