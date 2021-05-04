import parser
import interpreteur

def print_dico(dico):
    for k, v in dico.items():
        print(k + ' ' + v)

if __name__ == "__main__":
    phrase = input("Veuillez entrer une phrase à parser : ")

    parsing = parser.init_dico(parser.parse_ligne(phrase))

    find_verb = interpreteur.search_verbe(parsing)
    piste_sujet = interpreteur.traitement_forme_verbale(find_verb)

    res = interpreteur.search_sujet(find_verb, piste_sujet)

    print_dico(res)