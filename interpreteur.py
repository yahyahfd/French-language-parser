#!/usr/bin/env python3
import parser
import re

#Balise pour détecter lorsque qu'un verbe est conjugué à la 3ème personne du singulier 
balise_3s = '3s'

def comp_dico(dico_tuple, treatment, mot):
    #obselete if treatment in mot and mot[len(mot)-len(treatment):len(mot):1] == treatment:
    #Pour comprendre comment treatment[-1] est utilisé, regarder le pdf sur lefff
    if treatment[0] == mot.lower():
        if 'W' in treatment[-1]:
            return (mot, 'Verbe Infinitif')
        elif 'Verbe' in dico_tuple[1]:
            return (mot, dico_tuple[1] + treatment[-1])
        else:
            return (mot, 'Verbe' + ' ' + treatment[-1])
    
    return None


def search_verbe(tab):
    dico_tuple = tab
    fd_dico = open('lefff-verbs.txt')

    #itération du fichier conjugaison (terminaisons des verbes)
    for line in fd_dico:
        if '#' in line or line == '':
            continue
        else:
            #itération du dict (phrase en input splitted via ' ')
            for i in range(len(dico_tuple)):
                treatment = line.rstrip().split('\t')
                tmp = comp_dico(dico_tuple[i], treatment, dico_tuple[i][0])
                if tmp != None:
                    dico_tuple[i] = tmp
                '''nopunc = mot.strip(punc)
                dico = comp_terminaison(dico, treatment, nopunc)'''
    
    return dico_tuple


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


def traitement_forme_verbale(dico_tuple):
    piste_sujet = []
    for (k, v) in dico_tuple:
        if v == 'Nom':
            continue
        
        piste_sujet = append_premiere(piste_sujet, v)

        piste_sujet = append_deuxieme(piste_sujet, v)

        piste_sujet = append_troisieme(piste_sujet, v)

    return piste_sujet


def search_sujet_nom_propre(dico_tuple):
    '''tab_stock = []
    for i in range(len(dico_tuple)):
        tab_stock.append((mot, categorie))'''

    for i in range(1, len(dico_tuple)):
        #s3 est une convention du dictionnaire lefff pour indiquer un verbe à la 3ème personne singulier
        #un mot est un Nom propre sujet s'il est suivit d'un verbe à la 3ème personne du singulier
        #et s'il possède une majuscule
        if 'Verbe' in dico_tuple[i][1] and dico_tuple[i-1][0][0].isupper() and 's3' in dico_tuple[i][1]:
            dico_tuple[i-1] = (dico_tuple[i-1][0], 'Nom propre sujet')
    
    return dico_tuple


def search_sujet(dico_tuple, piste_sujet):
    piste_sujet = list(set(piste_sujet))
    for pronom in piste_sujet:   
        if pronom == balise_3s:
            dico_tuple = search_sujet_nom_propre(dico_tuple)
            continue
        
        for i in range(len(dico_tuple)): 
            #if 'Verbe' not in categorie:
            if dico_tuple[i][0].lower() == pronom:
                dico_tuple[i] = (dico_tuple[i][0], 'Sujet')
            #else:
            #    break
    
    return dico_tuple

def search_nom_propre(dico_tuple):
    premier_mot = True
    for i in range(len(dico_tuple)):
        if premier_mot:
            premier_mot = False
            continue
        
        if dico_tuple[i][1] == 'Nom' and dico_tuple[i][0][0].isupper() and not dico_tuple[i][0].isupper():
            dico_tuple[i] = (dico_tuple[i][0], 'Nom Propre')

    return dico_tuple

def lever_ambiguite_det(dico_tuple):
    fd = open('determinants.txt')
    etait_det = False

    for determinant in fd:
        for i in range(len(dico_tuple)): 
            if 'Verbe' in dico_tuple[i][1] and etait_det and dico_tuple[i][1] != 'Verbe Infinitif':
                dico_tuple[i] = (dico_tuple[i][0], 'Nom')
            
            etait_det = False

            if dico_tuple[i][0] == determinant.rstrip():
                dico_tuple[i] = (dico_tuple[i][0], 'Déterminant')
                etait_det = True

    return dico_tuple
