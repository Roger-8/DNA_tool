def DNA2mRNA(dna):
    DNA = dna.upper()
    print("DNA  : " + DNA)
    rna = {"A" : "U", "T" : "A", "C" : "G", "G" : "C"}
    RNA = str()
    for n in DNA:
        RNA += rna[n]
    print("mRNA : " + RNA)
    return RNA


def Genetic_code(rna):
    lenth = len(rna)
    long = lenth//3
#    print("'" + str(long) + "' genetic code in total")
    t = 1
    num = 0
    code = ['']*lenth
    for m in rna:
        code[num] += m
        if t == (3):
            num += 1
            t = 0
        t += 1
    print("Genetic Code : ")
    print(" -----")
    for i in range(lenth//3):
        print(" |" + code[i] + "|")
    print(" -----")
    def check_code():
        totallong = long
        for t1 in range(lenth//3):
            stime = long-1
            for t2 in range(long):
                if t1 != stime:
                    if code[t1] == code[stime]:
                        totallong = totallong-1
                    stime = stime-1
        print("'" + str(long) + "' genetic code in total")
#        print("'" + str(totallong) + "' type of genetic code")
    check_code()

import sys
#a = argv[0]
#a = input("input:")
mrna = DNA2mRNA(sys.argv[1])
Genetic_code(mrna)
