#!/usr/bin/env python3
import parser
import re

#Balise pour détecter lorsque qu'un verbe est conjugué à la 3ème personne du singulier 
balise_3s = '3s'

def comp_dico(dico_key, treatment, mot):
    #obselete if treatment in mot and mot[len(mot)-len(treatment):len(mot):1] == treatment:
    #Pour comprendre comment treatment[-1] est utilisé, regarder le pdf sur lefff
    if treatment[0] == mot:
        if 'W' in treatment[-1]:
            dico_key[mot] = 'Verbe Infinitif'
        else:
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
    '''res = re.split(' |\? |\?',text)
    while('' in res) :
        res.remove('')'''
    res = parser.parse_ligne(text)
    for a in res:
        if '-' in a:
            if '-t-' in a:
                return (a[0:a.find('-t-')], 't', a[a.find('-t-')+3:])
            else:
                return (a[0:a.find('-')], a[a.find('-')+1:])
    
    return None

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
            if piste_sujet[0] != balise_3s:
                piste_sujet.append(piste_sujet[0])
                piste_sujet[0] = balise_3s
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


def search_sujet_nom_propre(dico_key):
    tab_stock = []
    for mot, categorie in dico_key.items():
        tab_stock.append((mot, categorie))

    for i in range(len(tab_stock)):
        #s3 est une convention du dictionnaire lefff pour indiquer un verbe à la 3ème personne singulier
        if 'Verbe' in tab_stock[i][1] and tab_stock[i-1][0][0].isupper() and 's3' in tab_stock[i][1]:
            dico_key[tab_stock[i-1][0]] = 'Nom propre sujet'
    
    return dico_key


def search_sujet(dico_key, piste_sujet):
    for pronom in piste_sujet:   
        if pronom == balise_3s:
            dico_key = search_sujet_nom_propre(dico_key)
            continue
        
        for mot, categorie in dico_key.items(): 
            #if 'Verbe' not in categorie:
            if mot.lower() == pronom:
                dico_key[mot] = 'Sujet'
            #else:
            #    break
    
    return dico_key

def lever_ambiguite_det(dico_key):
    fd = open('determinants.txt')
    was = False

    for determinant in fd:
        for mot, categorie in dico_key.items(): 
            if 'Verbe' in categorie and was and categorie != 'Verbe Infinitif':
                dico_key[mot] = 'Nom'
            
            was = False

            if mot == determinant.rstrip():
                dico_key[mot] = 'Déterminant'
                was = True

    return dico_key
