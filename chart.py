from Grammer import Grammer
def chart(g:Grammer, Q:[]):
    i = 0
    # Agenda
    Ag = []
    # ActiveArc
    AA = []
    # Chart
    C = []
    while i < len(Q):
        if len(Ag) == 0:
            Ag.append({
                's': Q[i],
                'l': i,
                'r': i+1
            })
            i += 1
        # a = Ag.pop()
        a = Ag[0]
        Ag.remove(a)
        x = a['s']
        for p in g.get_grammer():
            if p['c'][0] == x:
                p['dot'] = 1
                p['l'] = a['l']
                p['r'] = a['r']
                AA.append(p)
        C.append(a)
        for aa in AA:
            if aa['c'][aa['dot']] == x and aa['dot'] == (len(aa['c']) - 1):
                if aa['p'] == 'S':
                    C.append({
                        's': 'S',
                        'l': 0,
                        'r': len(Q)
                    })
                    break
                else:
                    Ag.append({
                        's': aa['p'],
                        'l': aa['l'],
                        'r': a['r']
                    })

            if aa['c'][aa['dot']] == x and aa['dot'] < (len(aa['c']) - 1):
                aa['dot'] += 1
                aa['r'] = a['r']
                AA.append(aa)


    for c in C:
        print(str(c['l']+1) + '---' + c['s'] + '---' + str(c['r']+1))






if __name__ == '__main__':
    g = Grammer()
    g.add_grammer('S', ['NP','VP'])
    g.add_grammer('NP', ['det','N'])
    g.add_grammer('VP', ['V','NP'])
    g.add_grammer('VP', ['VP','PP'])
    g.add_grammer('PP', ['p','NP'])
    chart(g, ['det','N','V','det','N','p','det','N'])