import collections

class Person:
    def __init__(self, p1, p2, name, spouse):
        self.parent1 = p1
        self.parent2 = p2
        self.name = name
        self.spouse = spouse

f = open("family2.txt", "r")
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
            person = dict[pname]
            sp = []
            for x in sorted(person.spouse):
                if x not in sp:
                    sp.append(x)

            for x in sp:
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
            #print("w ancestor test success")
            #person = dict[pname]
            anc = []
            d = collections.deque([pname])
            while len(d) != 0:
                #for some reason new lines are being created in this while loop
                pname = d[0]
                if pname is '':
                    break

                d.popleft()
                p = dict[pname]

                if p.parent1 != '':
                    d.append(p.parent1.strip())
                    anc.append(p.parent1)
                if p.parent2 != '':
                    d.append(p.parent2.strip())
                    anc.append(p.parent2)

            for x in sorted(anc):
                print(x)

        if line[1] == "cousin":
            print("w cousin test success")

        if line[1] == "unrelated":
            #print("w unrelated test success")
            for x in sorted(dict):
                anc = []
                d = collections.deque([x])
                while len(d) != 0:
                    # for some reason new lines are being created in this while loop
                    y = d[0]
                    if y is '':
                        break

                    d.popleft()
                    p = dict[y]

                    if p.parent1 is not None:
                        d.append(p.parent1.strip())
                        anc.append(p.parent1)
                    if p.parent2 is not None:
                        d.append(p.parent2.strip())
                        anc.append(p.parent2)

                if pname in anc:
                    pass
                elif x != pname:
                    anc2 = []
                    d = collections.deque([pname])
                    while len(d) != 0:
                        z = d[0]
                        if z is '':
                            break

                        d.popleft()
                        p = dict[z]

                        if p.parent1 is not None:
                            d.append(p.parent1.strip())
                            anc2.append(p.parent1)
                        if p.parent2 is not None:
                            d.append(p.parent2.strip())
                            anc2.append(p.parent2)

                    if x not in anc2:
                        print(x)

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

            if p1.parent1.strip() == p2.parent1.strip() or p1.parent1.strip() == p2.parent2.strip() \
                    or p1.parent2.strip() == p2.parent1.strip() or p1.parent2.strip() == p2.parent2.strip():
                print("Yes")

            else:
                print("No")

        if line[2] == "ancestor":
            #print("x ancestor test success")
            anc = []
            d = collections.deque([p2name])
            while len(d) != 0:
                # for some reason new lines are being created in this while loop
                pname = d[0]
                if pname is '':
                    break

                d.popleft()
                p = dict[pname]

                if p.parent1 is not None:
                    d.append(p.parent1.strip())
                    anc.append(p.parent1)
                if p.parent2 is not None:
                    d.append(p.parent2.strip())
                    anc.append(p.parent2)

            if p1name in anc:
                print("Yes")
            else:
                print("No")

        if line[2] == "cousin":
            #print("x cousin test success")
            #ctest = True
            if p1name in dict and p2name in dict:
                cous1 = dict[p1name]
                cous2 = dict[p2name]
                c1p1 = cous1.parent1
                c1p2 = cous1.parent2
                c2p1 = cous2.parent1
                c2p2 = cous2.parent2
                """print("Cousin 1 parent 1: " + c1p1)
                print("Cousin 1 parent 2: " + c1p2)
                print("Cousin 2 parent 1: " + c2p1)
                print("Cousin 2 parent 2: " + c2p2)"""

                if c1p1 == c2p1 or c1p1 == c2p2 or c1p2 == c2p1 or c1p2 == c2p2:
                    ctest = False

                elif c1p1 in dict and c1p2 in dict and c2p1 in dict and c2p2 in dict:
                    par11 = dict[c1p1]
                    par12 = dict[c1p2]
                    par21 = dict[c2p1]
                    par22 = dict[c2p2]
                    c1p1p1 = par11.parent1
                    c1p1p2 = par11.parent2
                    c1p2p1 = par12.parent1
                    c1p2p2 = par12.parent2
                    c2p1p1 = par21.parent1
                    c2p1p2 = par21.parent2
                    c2p2p1 = par22.parent1
                    c2p2p2 = par22.parent2
                    """
                    print("c1p1p1: " + c1p1p1)
                    print("c1p1p2: " + c1p1p2)
                    print("c1p2p1: " + c1p2p1)
                    print("c1p2p2: " + c1p2p2)
                    print("c2p1p1: " + c2p1p1)
                    print("c2p1p2: " + c2p1p2)
                    print("c2p2p1: " + c2p2p1)
                    print("c2p2p2: " + c2p2p2)
                    """

                    if c1p1p1 == '' or c1p1p2 == '' or c1p2p1 == '' or c1p2p2 == '' or \
                            c2p1p1 == '' or c2p1p2 == '' or c2p2p1 == '' or c2p2p2 == '':
                        ctest = False

                    elif c1p1p1 == c2p1p1 or c1p1p1 == c2p1p2 or c1p1p1 == c2p2p1 or c1p1p1 == c2p2p2 \
                            or c1p1p2 == c2p1p1 or c1p1p2 == c2p1p2 or c1p1p2 == c2p2p1 or c1p1p2 == c2p2p2 \
                            or c1p2p1 == c2p1p1 or c1p2p1 == c2p1p2 or c1p2p1 == c2p2p1 or c1p2p1 == c2p2p2 \
                            or c1p2p2 == c2p1p1 or c1p2p2 == c2p1p2 or c1p2p2 == c2p2p1 or c1p2p2 == c2p2p2:
                        ctest = True
                else:
                    ctest = False
            else:
                ctest = False

            if ctest == True:
                print("Yes")
            else:
                print("No")

        if line[2] == "unrelated":
            #print("x unrelated test success")
            if p1name in dict and p2name in dict:
                anc = []
                d = collections.deque([p2name])
                while len(d) != 0:
                    pname = d[0]
                    d.popleft()
                    p = dict[pname]

                    if p.parent1 != '':
                        d.append(p.parent1)
                        anc.append(p.parent1)
                    if p.parent2 != '':
                        d.append(p.parent2)
                        anc.append(p.parent2)
                if p1name in anc:
                    print("No")
                else:
                    print("Yes")
            else:
                print("Yes")

        print()


#for x in dict:
    #print(x.strip())