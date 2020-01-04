from Grammer import Grammer
def cyk(g:Grammer,s:str):
    l = len(s)
    opt = [[0] * l for i in range(l+1)]
    # the i layer
    # range :[1,l]
    for i in range(1, l+1):
        # if it is bottom layer
        if i == 1:
            #set value
            # range: [0,l-i]
            for k in range(l):
                char = s[k]
                v = []
                v.extend(g.get_grammer_by_child(char))
                opt[i][k] = v
            continue;

        # if not bottom layer
        # loop each opt
        # range: [0,l-i]
        for k in range(l-i+1):
            # loop through each split situation
            # 5 []
            # 4 [] []
            # 3 [] [] []
            # 2 [] [] [] []
            # 1 [] [] [] [] []
            #   0  1  2  3  4
            # opt[2,k] = opt[1,k] + opt[1,k+1]
            # opt[3,k] = (opt[1,k] + opt[2,k+1]) + (opt[2,k] + opt[1,k+2])
            # opt[4,k] = (opt[1,k] + opt[3,k+1]) + (opt[2,k] + opt[2,k+2]) + (opt[3,k] + opt[1,k+3])
            char = s[k]
            v = []
            for j in range(1, i):
                c1 = opt[j][k]
                c2 = opt[i-j][k+j]

                if len(c1) and len(c2):
                    # combine
                    for cc1 in c1:
                        for cc2 in c2:
                            v.extend(g.get_grammer_by_child(cc1+cc2))
            # de-duplication
            v = list(set(v))
            opt[i][k] = v

    for i in range(l, 0, -1):
        print(opt[i][:l-i+1])


if __name__ == '__main__':
    g =  Grammer()
    g.add_grammer('S',['AB','BC'])
    g.add_grammer('A',['BA','a'])
    g.add_grammer('B',['CC','b'])
    g.add_grammer('C',['AB','a'])
    cyk(g, "baaba")