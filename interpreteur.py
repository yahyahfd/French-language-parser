#!/usr/bin/env python3
import parser
import re

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
                treatment = parse_ligne(line.rstrip())
                dico = comp_dico(dico, treatment, mot)
                '''nopunc = mot.strip(punc)
                dico = comp_terminaison(dico, treatment, nopunc)'''

# On ne traite pas des paragraphes ici: text est une phrase, et donc le "?" est le dernier caractère
def is_question(text):
    res = re.split(' |\? |\?',text)
    while('' in res) :
        res.remove('')
    for a in res:
        if '-' in a:
            if '-t-' in a:
                return a[a.find('-t-')+3:]
            else:
                return a[a.find('-')+1:]

#dé-commenter pour le test
#print(is_question('Que voulez-vous?'))
#print(is_question('A-t-il un stylo sur lui?'))
