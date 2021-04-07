#!/usr/bin/env python3
# dans une phrase simple, les mots sont séparés par des espaces: On cherche à séparer ces termes et à les mettre dans une liste
# le premier séparateur est l'espace, le deuxième est la virgule et autres ponctuations (collés aux termes), le troisième est l'apostrophe comme dans "l'espace".
import re

def parse_ligne(text):
    l = re.split(" |! |, |: |\? |\. |; |\.\.\. |\"|\'|\(|\)|!|,|:|\?|\.|;|\.\.\.",text)
    while("" in l) :
        l.remove("")
    
    return l
    '''for x in range(len(l)):
        print(l[x])'''

test = parse_ligne("Bonjour! Ceci est un test, bien sûr. (Comment) \"ça\"? Et bien c'est très simple: chaque mot; doit apparaitre seul...")

punc = '.;:,?!"\')('

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

