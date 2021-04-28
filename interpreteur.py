import parser

def comp_dico(dico, treatment, mot):
    #obselete if treatment in mot and mot[len(mot)-len(treatment):len(mot):1] == treatment:
    #Pour comprendre pourquoi treatment[-1] est ajouté, regarder le pdf sur lefff
    if treatment[0] == mot:
        dico[mot] = 'verbe' + ' ' + treatment[-1]
    
    return dico

def parse_dict(tab):
    dico = tab
    fd = open('lefff-verbs.txt')

    #itération du fichier conjugaison (terminaisons des verbes)
    for line in fd:
        if '#' in line or '-' in line or line == '':
            continue
        else:
            #itération du dict (phrase en input splitted via ' ')
            for mot in tab:
                treatment = parser.parse_ligne(line.rstrip())
                dico = comp_dico(dico, treatment, mot)
                '''nopunc = mot.strip(punc)
                dico = comp_terminaison(dico, treatment, nopunc)'''