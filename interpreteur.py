import parser

def comp_dico(dico, treatment, mot):
    #obselete if treatment in mot and mot[len(mot)-len(treatment):len(mot):1] == treatment:
    #Pour comprendre pourquoi treatment[-1] est ajouté, regarder le pdf sur lefff
    if treatment[0] == mot:
        dico[mot] = 'verbe' + ' ' + treatment[-1]
    
    return dico

def search_verbe(tab):
    dico_key = tab
    fd_dico = open('lefff-verbs.txt')

    #itération du fichier conjugaison (terminaisons des verbes)
    for line in fd_dico:
        if '#' in line or '-' in line or line == '':
            continue
        else:
            #itération du dict (phrase en input splitted via ' ')
            for mot in tab:
                treatment = parser.parse_ligne(line.rstrip())
                dico_key = comp_dico(dico_key, treatment, mot)
                '''nopunc = mot.strip(punc)
                dico = comp_terminaison(dico, treatment, nopunc)'''
    
    return dico_key

def append_premiere(piste_sujet, v):
    if '1' in v:
        if 's' in v:
            piste_sujet.append('je')
        elif 'p' in v:
            piste_sujet.append('nous')
    
    return piste_sujet

def append_deuxieme(piste_sujet, v):
    if '2' in v:
        if 's' in v:
            piste_sujet.append('tu')
        elif 'p' in v:
            piste_sujet.append('vous')
    
    return piste_sujet

def append_troisieme(piste_sujet, v):
    if '3' in v:
        if 's' in v:
            piste_sujet.append('il')
            piste_sujet.append('elle')
            piste_sujet.append('on')
            piste_sujet.append(piste_sujet[0])
            piste_sujet[0] = '3s'
        elif 'p' in v:
            piste_sujet.append('ils')
            piste_sujet.append('elles')
    
    return piste_sujet


def traitement_forme_verbale(dico_key):
    piste_sujet = []
    for (k, v) in dico_key.items():
        if v == 'nom':
            continue
        
        piste_sujet = append_premiere(piste_sujet, v)

        piste_sujet = append_deuxieme(piste_sujet, v)

        piste_sujet = append_troisieme(piste_sujet, v)

    return piste_sujet
        