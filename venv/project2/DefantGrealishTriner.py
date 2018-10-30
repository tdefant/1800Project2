class Person:
    def __init__(self, p1, p2, name, spouse):
        self.parent1 = p1
        self.parent2 = p2
        self.name = name
        self.spouse = spouse

f = open("family1.txt", "r")
dict = {}

for x in f:
    line = x.split(" ")
    if line[0] == "E":
        #print(x)
        if len(line) == 3:
            p1name = line[1].strip()
            p2name = line[2].strip()
            if p1name in dict:
                p1 = dict[p1name]
                p1.spouse.append(p2name)
                dict[p1name] = p1
            else:
                p1 = Person("", "", p1name, [p2name])
                dict[p1name] = p1

            if p2name in dict:
                p2 = dict[p2name]
                p2.spouse.append(p1name)
                dict[p2name] = p2
            else:
                p2 = Person("", "", p2name, [p1name])
                dict[p2name] = p2

        if len(line) == 4:
            p1name = line[1].strip()
            p2name = line[2].strip()
            cname = line[3].strip()
            if p1name in dict:
                #print(p1name + " is in dict")
                if p2name not in p1.spouse:
                    p1 = dict[p1name]
                    p1.spouse.append(p2name)
                    dict[p1name] = p1
            else:
                p1 = Person("", "", p1name, [p2name])
                dict[p1name] = p1

            if p2name in dict:
                #print(p2name + " is in dict")
                if p1name not in p2.spouse:
                    p2 = dict[p2name]
                    p2.spouse.append(p1name)
                    dict[p2name] = p2
            else:
                p2 = Person("", "", p2name, [p1name])
                dict[p2name] = p2

            person = Person(p1name, p2name, cname, [])
            dict[cname] = person

    if line[0] == "W":
        print(x)
        pname = line[2].strip()

        if line[1] == "child":
            #print("w child test success")
            for x in sorted(dict):
                temp = dict[x]
                if temp.parent1.strip() == pname or temp.parent2.strip() == pname:
                    print(x.strip())

        if line[1] == "spouse":
            #print("w spouse test success")
            temp = dict[pname]
            for x in sorted(temp.spouse):
                print(x)

        if line[1] == "sibling":
            #print("w sibling test success")
            person = dict[pname]
            par1 = person.parent1.strip()
            par2 = person.parent2.strip()
            for x in sorted(dict):
                xpar1 = dict[x].parent1
                xpar2 = dict[x].parent2
                if par1 == xpar1 or par1 == xpar2 or par2 == xpar1 or par2 == xpar2:
                    if not dict[x].name.strip() == person.name:
                        print(dict[x].name.strip())

        if line[1] == "ancestor":
            print("w ancestor test success")

        if line[1] == "cousin":
            print("w cousin test success")

        if line[1] == "unrelated":
            print("w unrelated test success")
        print()

    if line[0] == "X":
        print(x)
        p1name = line[1].strip()
        p2name = line[3].strip()

        if line[2] == "child":
            #print("x child test success")
            p1 = dict[p1name]
            p2 = dict[p2name]
            if p1.parent1 == p2.name:
                print("Yes")
            elif p1.parent2 == p2.name:
                print("Yes")
            else:
                print("No")

        if line[2] == "spouse":
            #print("x spouse test success")
            if p1name in dict[p2name].spouse:
                print("Yes")
            elif p2name in dict[p1name].spouse:
                print("Yes")
            else:
                print("No")

        if line[2] == "sibling":
            #print("x sibling test success")
            p1 = dict[p1name]
            p2 = dict[p2name]
            #print("p1p1 " + p1.parent1)
            #print("p1p2 " + p1.parent2)
            #print("p2p1 " + p2.parent1)
            #print("p2p2 " + p2.parent2)
            if p1.parent1.strip() == p2.parent1.strip() or p1.parent1.strip() == p2.parent2.strip() or p1.parent2.strip() == p2.parent1.strip() or p1.parent2.strip() == p2.parent2.strip():
                print("Yes")
            else:
                print("No")

        if line[2] == "ancestor":
            print("x ancestor test success")

        if line[2] == "cousin":
            print("x cousin test success")

        if line[2] == "unrelated":
            print("x unrelated test success")
        print()

#for x in dict:
    #print(x.strip())