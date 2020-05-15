import random
from bubblesort import BubbleSort
numarr = []
numsfilled = []
allrows = []
allrowsfilled = []
allcols = []
allcolsfilled = []
alldiags = []
alldiagsfilled = []
cardnums = []
fiveboards = ''
oneboard = ''
winchances = []
bingoboardindex = ''
cont = True
bingo = False

def generatecard():
    #defines global variables
    global cardnums
    global numsfilled
    global winchances
    global numarr
    #user prompt
    prompt2 = input('How many possible numbers are there?\n')
    prompt2 = int(prompt2)
    newprompt = input('How many random boards do you want to optimize?\n')
    x=1
    while (x<=prompt2):
        numarr.append(x)
        x+=1
    for i in range(0, int(newprompt)):
        winchances.append([0, i])
        #creates boards and data for whether they are filled
        cardnums.append(random.sample(range(1,prompt2), 25))
        numsfilled.append([0]*25)
    #fills in free space
    for p in cardnums:
        p[12] = 'X'
    for q in numsfilled:
        q[12] = 1

def printcard(cardarr):
    numsinrow = 1
    nextline = False
    for subarr in cardarr:
        print("==============")
        for num in subarr:
            if (nextline == False):
                if (len(str(num)) == 1):
                    print(num, end='  ')
                else:
                    print(num, end=' ')
                
            else:
                print(num)
                nextline = False
            numsinrow+=1
            if (numsinrow == 5):
                nextline = True
                numsinrow = 0
    print("==============")

def printsinglecard(cardarr, ind):
    numsinrow = 1
    nextline = False
    print("==============")
    for num in cardarr[ind]:
        if (nextline == False):
            if (len(str(num)) == 1):
                print(num, end= '  ')
            else:
                print(num, end=' ')

        else:
            print(num)
            nextline = False
        numsinrow+=1
        if (numsinrow == 5):
            nextline = True
            numsinrow = 0
    print("==============")

def rowgen():
    global allrows
    global allrowsfilled
    allrows = []
    allrowsfilled = []
    for i in cardnums:
        rows = []
        currentrow = []
        ind = 0
        while (ind+1<=len(i)):
            currentrow.append(i[ind])
            if ((ind+1) % 5 == 0):
                rows.append(currentrow)
                currentrow = []
            ind+=1
        allrows.append(rows)
        
    for p in numsfilled:
        rowcovers = []
        currentrowcovers = []
        ind = 0
        while (ind+1<=len(p)):
            currentrowcovers.append(p[ind])
            if ((ind+1) % 5 == 0):
                rowcovers.append(currentrowcovers)
                currentrowcovers = []
            ind+=1
        allrowsfilled.append(rowcovers)

def colgen():
    global allcols
    global allcolsfilled
    allcols = []
    allcolsfilled = []
    for i in cardnums:
        cols = []
        currentcol = []
        ind = 0
        while (ind<=4):
            currentcol = i[ind::5]
            cols.append(currentcol)
            ind+=1
        allcols.append(cols)
        
    for p in numsfilled:
        colcovers = []
        currentcolcovers = []
        ind = 0
        while (ind <= 4):
            currentcolcovers = p[ind::5]
            colcovers.append(currentcolcovers)
            ind+=1
        allcolsfilled.append(colcovers)

def diaggen():
    global alldiags
    global alldiagsfilled
    alldiags = []
    alldiagsfilled = []
    for a in cardnums:
        diags = []
        diag1 = []
        diag2 = []
        for i in range(0, 5):
            diag1.append(a[i*6])
        for p in range(1, 6):
            diag2.append(a[p*4])
        diags.append(diag1)
        diags.append(diag2)
        alldiags.append(diags)
    
    for b in numsfilled:
        diagcovers = []
        diag1cov = []
        diag2cov = []
        for i in range(0, 5):
            diag1cov.append(b[i*6])
        for p in range(1, 6):
            diag2cov.append(b[p*4])
        diagcovers.append(diag1cov)
        diagcovers.append(diag2cov)
        alldiagsfilled.append(diagcovers)

def checkbingorow():
    rowgen()
    global bingo
    global bingoboardindex
    totalpossiblebingos = []
    for c in allrows:
        inarowmax = 0
        inarow = 0
        inarowmaxinds = []
        allpossiblebingos = []
        cind = allrows.index(c)
        b = allrowsfilled[cind]
        #checks horizontals
        for p in b:
            inarow = p.count(1)
            if (inarow > inarowmax):
                inarowmax = inarow
                inarowmaxinds.append(b.index(p))

        for i in c:
            iind = c.index(i)
            reali = b[iind]
            thesame = False
            inarow = reali.count(1)
            if (inarow == inarowmax):
                for a in inarowmaxinds:
                    if (c.index(i) == a):
                        thesame = True
                if (thesame == False):
                    inarowmaxinds.append(c.index(i))

        if (inarowmax == 5):
            bingo = True
            bingoboardindex = cind
        else:
            for q in inarowmaxinds:
                ind = 0
                row = b[q]
                unfilledinds = []
                for r in row:
                    if (r==0):                    
                        rind = 5*(q)+ind
                        currentcardnums = cardnums[cind]
                        unfilledinds.append(currentcardnums[rind])
                    ind+=1
                allpossiblebingos.append(unfilledinds)
        totalpossiblebingos.append(allpossiblebingos)
    return totalpossiblebingos

def checkbingocol():
    colgen()
    global bingo
    global bingoboardindex
    totalpossiblebingos = []
    for c in allcols:
        inarowmax = 0
        inarow = 0
        inarowmaxinds = []
        allpossiblebingos = []
        cind = allcols.index(c)
        b = allcolsfilled[cind]
        #checks verticals
        for p in b:
            inarow = p.count(1)
            if (inarow > inarowmax):
                inarowmax = inarow
                inarowmaxinds.append(b.index(p))

        for i in c:
            iind = c.index(i)
            reali = b[iind]
            thesame = False
            inarow = reali.count(1)
            if (inarow == inarowmax):
                for a in inarowmaxinds:
                    if (c.index(i) == a):
                        thesame = True
                if (thesame == False):
                    inarowmaxinds.append(c.index(i))

        if (inarowmax == 5):
            bingo = True
            bingoboardindex = cind

        else:
            for q in inarowmaxinds:
                ind = 0
                row = b[q]
                unfilledinds = []
                for r in row:
                    if (r==0):
                        currentcardnums = cardnums[cind]
                        rind = q+ind
                        unfilledinds.append(currentcardnums[rind])    
                    ind+=5            
                allpossiblebingos.append(unfilledinds)
        totalpossiblebingos.append(allpossiblebingos)
    
    return totalpossiblebingos

def checkbingodiag():
    diaggen()
    global bingo
    global bingoboardindex
    totalpossiblebingos = []
    for c in alldiags:
        inarowmax = 0
        inarow = 0
        inarowmaxinds = []
        allpossiblebingos = []
        cind = alldiags.index(c)
        b = alldiagsfilled[cind]
        #checks diagonals
        for p in b:
            inarow = p.count(1)
            if (inarow > inarowmax):
                inarowmax = inarow
                inarowmaxinds.append(b.index(p))

        for i in c:
            iind = c.index(i)
            reali = b[iind]
            thesame = False
            inarow = reali.count(1)
            if (inarow == inarowmax):
                for a in inarowmaxinds:
                    if (c.index(i) == a):
                        thesame = True
                if (thesame == False):
                    inarowmaxinds.append(c.index(i))
                else:
                    thesame = False

        if (inarowmax == 5):
            bingo = True
            bingoboardindex = cind
        else:
            for q in inarowmaxinds:
                ind = 0
                row = b[q]
                unfilledinds = []
                subarr = c[q]
                for r in row:
                    if (r==0):
                        currentcardnums = cardnums[cind]
                        rind = currentcardnums.index(subarr[ind])                  
                        unfilledinds.append(currentcardnums[rind])
                    ind+=1
                allpossiblebingos.append(unfilledinds)
        totalpossiblebingos.append(allpossiblebingos)
    
    return totalpossiblebingos

def findfastest(array):
    shortestmethod = [0] * 100
    shortestmethods = []
    for i in array:
        for p in i:
            if (len(p) <= len(shortestmethod)):
                shortestmethod = p
    for i in array:
        for p in i:
            if (len(p) == len(shortestmethod)):                   
                shortestmethods.append(p)

    return shortestmethods 

def startgame():
    global fiveboards
    global oneboard
    global cont
    generatecard()
    prompt = input('How many turns do you want until you reduce the number to 5?\n')
    prompt2 = input('How many turns do you want until you reduce the number to 1? (make sure that this is greater than the first one)\n')
    try:
        fiveboards = int(prompt)
        oneboard = int(prompt2)
        if (oneboard <= fiveboards):
            print('Make sure that the amount of turns till 1 is greater than the amount of turns till 5.')
            cont = False
    except ValueError:
        print("One of those wasn't a number.")

def checkbingomult():
    global winchances
    allbingorows = checkbingorow()
    allbingocols = checkbingocol()
    allbingodiags = checkbingodiag()
    for i in range(0, len(cardnums)):
        subbingos = []
        rowbingos = allbingorows[i]
        colbingos = allbingocols[i]
        diagbingos = allbingodiags[i]
        subbingos.append(rowbingos)
        subbingos.append(colbingos)
        subbingos.append(diagbingos)
        fastestsubbingos = findfastest(subbingos)
        for p in fastestsubbingos:
            shortestlen = len(p)
        subwinchance = 1
        numarrlen = len(numarr)
        for i in range(1, shortestlen+1):
            subwinchance = subwinchance/numarrlen
            numarrlen-=1
        totalsubwinchance = round(subwinchance*len(fastestsubbingos)*100, 7)
        specwinchance = winchances[i]
        specwinchance[0] = totalsubwinchance

def findhighestpercents(num):
    global winchances
    inds = []
    winchancescopy = winchances
    BubbleSort(winchancescopy)
    winchancescopy = winchancescopy[::-1]
    for i in range(0, num):
        specwinchances = winchancescopy[i]
        inds.append(specwinchances[1])
    while (len(inds) > num):
        del inds[-1]
    return inds

def playgamemult():
    global bingo
    global cardnums
    global numsfilled
    global cardnums
    global winchances
    turns = 0
    oneleft = False
    while (bingo == False):
        if (turns == fiveboards):
            highestfive = findhighestpercents(5)
            newnums = []
            for index in highestfive:
                newnums.append(cardnums[index])
            cardnums = newnums
            
            newnumsfilled = []
            for newindex in highestfive:
                newnumsfilled.append(numsfilled[newindex])
            numsfilled = newnumsfilled
            
            newwinchances = []
            for r in highestfive:
                newwinchances.append(winchances[r])
            winchances = newwinchances
            
            a=0
            for p in winchances:
                p[1] = a
                a+=1


            print()
            print('These are the remaining boards:')
            print()
            printcard(cardnums)
        else:
            if (turns == oneboard):
                highestone = findhighestpercents(1)
                newnums = []
                newnums.append(cardnums[highestone[0]])
                cardnums = newnums

                newnumsfilled = []
                newnumsfilled.append(numsfilled[highestone[0]])
                numsfilled = newnumsfilled
                print()
                print('This is the last board:')
                print()
                printcard(cardnums)
                oneleft = True

        turns +=1
        print()
        try:
            prompt = input('What was the number chosen?\n')
            numarr.remove(int(prompt))
            for i in cardnums:
                if (int(prompt) in i):
                    promptind = i.index(int(prompt))
                    ifilled = numsfilled[cardnums.index(i)]
                    i[promptind] = 'X'
                    ifilled[promptind] = 1
                if (oneleft == True):
                    printsinglecard(cardnums, 0)
            checkbingomult()
        except ValueError as ve:
            raise ValueError('That isn\'t a number.')
        if (bingo == True):
            print()
            print('Looks like you got a bingo on the following board: ')
            print()
            printsinglecard(cardnums, bingoboardindex)

def playbingo():
    startgame()
    if (cont == True):
        playgamemult()


playbingo()