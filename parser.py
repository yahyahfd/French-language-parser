#!/usr/bin/env python3
# dans une phrase simple, les mots sont séparés par des espaces: On cherche à séparer ces termes et à les mettre dans une liste
# le premier séparateur est l'espace, le deuxième est la virgule et autres ponctuations (collés aux termes), le troisième est l'apostrophe comme dans "l'espace".
import re

def test(text):
    l= re.split(" |! |, |: |\? |\. |; |\.\.\. |\"|\'|\(|\)|!|,|:|\?|\.|;|\.\.\.",text)
    while("" in l) :
        l.remove("")
    for x in range(len(l)):
        print(l[x])

test("Bonjour! Ceci est un test, bien sûr. (Comment) \"ça\"? Et bien c'est très simple: chaque mot; doit apparaitre seul...")
