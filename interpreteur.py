#!/usr/bin/env python3
import parser
import re


def comp_dico(dico_key, treatment, mot):
    #obselete if treatment in mot and mot[len(mot)-len(treatment):len(mot):1] == treatment:
    #Pour comprendre pourquoi treatment[-1] est ajouté, regarder le pdf sur lefff
    if treatment[0] == mot:
        dico_key[mot] = 'Verbe' + ' ' + treatment[-1]
    
    return dico_key


def search_verbe(tab):
    dico_key = tab
    fd_dico = open('lefff-verbs.txt')

    #itération du fichier conjugaison (terminaisons des verbes)
    for line in fd_dico:
        if '#' in line or line == '':
            continue
        else:
            #itération du dict (phrase en input splitted via ' ')
            for mot, categorie in dico_key.items():
                treatment = line.rstrip().split('\t')
                dico_key = comp_dico(dico_key, treatment, mot)
                '''nopunc = mot.strip(punc)
                dico = comp_terminaison(dico, treatment, nopunc)'''
    
    return dico_key


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
        if v == 'Nom':
            continue
        
        piste_sujet = append_premiere(piste_sujet, v)

        piste_sujet = append_deuxieme(piste_sujet, v)

        piste_sujet = append_troisieme(piste_sujet, v)

    return piste_sujet


def search_nom_propre(dico_key):
    i = 0
    for mot, categorie in dico_key.items():
        if i == 0 and mot[0].isupper():
            dico_key[mot] = 'Début de phrase, possible sujet nom propre'
            i = i + 1
            continue 
        
        if 'Verbe' in categorie:
            break

        if mot[0].isupper():
            dico_key[mot] = 'Nom propre sujet'
    
    return dico_key


def search_sujet(dico_key, piste_sujet):
    for pronom in piste_sujet:   
        if pronom == '3s':
            dico_key = search_nom_propre(dico_key)
            continue
        
        for mot, categorie in dico_key.items(): 
            if 'Verbe' not in categorie:
                if mot.lower() == pronom:
                    dico_key[mot] = 'Sujet'
            else:
                break
    
    return dico_key
