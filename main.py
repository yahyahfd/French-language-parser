import parser
import interpreteur

def print_dico_tuple(dico):
    for (k, v) in dico:
        if 'Verbe' in v and v != 'Verbe Infinitif':
            print(k + ' ' + v.split(' ')[0])
        else:
            print(k + ' ' + v)

def adapte_tirets(tab):
    res = []
    for elt in tab:
        if '-' not in elt:
            res.append(elt)
        else:
            tmp = elt.split('-')
            for sub in tmp:
                res.append(sub)
    
    return res

def cas_question(phrase, tab):
    decoupe = adapte_tirets(tab)
    parsing = parser.init_dico(decoupe)

    res = interpreteur.is_question(phrase)

    parcourt = 0
    for i in range(len(parsing)):
        if parcourt < len(res) and parsing[i][0] == res[parcourt]:
            if parcourt == 0:
                parsing[i] = (parsing[i][0], 'Verbe')
            elif (len(res) == 2 and parcourt == 1) or (len(res) == 3 and parcourt == 2):
                parsing[i] = (parsing[i][0], 'Sujet')
            else:
                parsing[i] = (parsing[i][0], 'Pronom')
            parcourt = parcourt + 1
    
    parsing.append(('?', 'Punctuation'))
    print_dico_tuple(parsing)

if __name__ == "__main__":
    phrase = input("Veuillez entrer une phrase à parser : ")

    traitement = parser.parse_ligne(phrase)
    if '?' in phrase:
        cas_question(phrase, traitement)
    else:
        parsing = parser.init_dico(traitement)

        find_verb = interpreteur.search_verbe(parsing)
        piste_sujet = interpreteur.traitement_forme_verbale(find_verb)

        res = interpreteur.search_sujet(find_verb, piste_sujet)
        res = interpreteur.lever_ambiguite_det(res)
        res = interpreteur.search_nom_propre(res)
        
        print_dico_tuple(res)