def p(q):
    for x in q:
        print(x)

def tohrs(x):
    return round(x*188/60000)

class Entry:
    def __init__(self, line):
        l               = line.split("-")
        self.name       = l[0]
        self.category   = l[1]
        self.gender     = l[2]
        self.points     = int(l[3].split("\n")[0])

    def __repr__(self):
        return self.name + (17-len(self.name))*" " +" |   " +str(self.points)+ \
        +(9-len(str(self.points)))*" " + "|   " +self.category \
        +(13-len(self.category))*" " + " |    " +self.gender \
        +(9-len(self.gender))*" " + " |    " +str(tohrs(self.points))\
        +" hrs"

def analyze():
    print("-------------------------------------------")
    totpoints = 0
    for entry in entries:
        if entry.category in catdict:
            catdict[entry.category] += entry.points
        else:
            catdict[entry.category] = entry.points

        if entry.gender in gendict:
            gendict[entry.gender] += entry.points
        else:
            gendict[entry.gender] = entry.points

        totpoints += entry.points

    genorder = reversed(sorted(gendict, key=gendict.get))
    catorder = reversed(sorted(catdict, key=catdict.get))

    print("Your gender watching habits... \n")
    for gender in genorder:
        print(
        gender +(14-len(gender))*" " +" -    " + str(round(gendict[gender]/totpoints*100,2))+"%" \
        + "     - " + str(tohrs(gendict[gender])) + "hrs"
        )

    print("\n"+"Your category watching habits... \n")
    for category in catorder:
        print(
        category +(14-len(category))*" " + " -    " + str(round(catdict[category]/totpoints*100,2))+"%" \
        + "    - " +str(tohrs(catdict[category])) + "hrs"
        )

    print("-------------------------------------------")

    p(points)

entries = []
with open('data.txt') as f:
    for line in f.readlines():
        entries.append(Entry(line))
points = sorted(entries, key=lambda x: -x.points)
catdict = {}
gendict = {}
analyze()
