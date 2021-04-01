
punc = '.;:,?!"\')('

def parse_espace(ligne: str):
    tab = str.split(' ')

def init_dico(tab):
    dico = dict
    for mot in tab:
        dico[mot] = "nom"
    return dico

def comp_terminaison(dico, treatment, mot):
    if treatment in mot and mot[len(mot)-len(treatment):len(mot):1] == treatment:
        dico[mot] = "verbe"
    return dico

def parse_dict(tab):
    dico = init_dico(tab)
    fd = open('conjugaison.txt')

    #itération du fichier conjugaison (terminaisons des verbes)
    for line in fd:
        if '#' in line or '-' in line or line == '':
            continue
        else:
            #itération du dict (phrase en input splitted via ' ')
            for mot in tab:
                treatment = line.rstrip()
                dico = comp_terminaison(dico, treatment, mot)
                nopunc = mot.strip(punc)
                dico = comp_terminaison(dico, treatment, nopunc)
