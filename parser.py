#!/usr/bin/env python3
# dans une phrase simple, les mots sont séparés par des espaces: On cherche à séparer ces termes et à les mettre dans une liste
# le premier séparateur est l'espace, le deuxième est la virgule et autres ponctuations (collés aux termes), le troisième est l'apostrophe comme dans "l'espace".
import re

def parse_ligne(text):
    l = re.split(" |! |, |: |\? |\. |; |\.\.\. |\"|\'|\(|\)|!|,|:|\?|\.|;|\.\.\.",text)
    while("" in l) :
        l.remove("")
    
    return l

test = parse_ligne("Bonjour! Ceci est un test, bien sûr. (Comment) \"ça\"? Et bien c'est très simple: chaque mot; doit apparaitre seul...")

#punc = '.;:,?!"\')('

def init_dico(tab):
    dico = dict
    for mot in tab:
        dico[mot] = 'Nom'
    return dico


