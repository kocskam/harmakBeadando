
input = "2[b4[a]]"
output = ""

def stillNeedWorking(input):


def convertToMakeSense(input):
    # ha több van
    db = 0
    for i in input:
        if i == "[":
            db += 1

    for j in range(len(input)):
        if input[j] == "[":
            db -= 1
        if db == 0:
            break

    #ennyiszer kell ismételni
    k = input[j - 1]

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

    for j in range(int(k)):
        newOutput += repeatThisText

    for z in range(ind+1, len(input)):
        newOutput += input[z]

    print(newOutput)

convertToMakeSense(input)

