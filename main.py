# Thomas Servettaz
# 07.12.2020

def en_tete():
    print("**********STADE GENEVE**********")
    print("********************************")


def en_tete_mieux(nb_etoiles, titre):
    # print("**********STADE GENEVE**********")
    print(nb_etoiles * "*", titre, nb_etoiles * "*")
    print("*" * (nb_etoiles + len(titre) + 2 + nb_etoiles))


if __name__ == '__main__':
    nom_groupe = "Stade Genève - adultes I"
    annee_en_cours = 2020
    names = ['Bob', 'Jane', 'Jack', 'Chloe', 'Mat', 'Beth', 'Xiao']
    ages = [20, 22, 23, 18, 35, 40, 39]
    is_male = [True, False, True, False, True, False, False]
    chrono_manche_1 = [13.4, 15.2, 12.8, 12.7, 12.8, 13.3, 13.9]
    chrono_manche_2 = [13.6, 14.2, 12.7, 12.5, 14.7, 13.4, 13.8]
    chrono_manche_3 = [14.5, 14.1, 12.8, 13.7, 13.4, 13.5, 12.9]
    resultats = [chrono_manche_1, chrono_manche_2, chrono_manche_3]

    # exercice 1 (appel)
    en_tete()

    # exercice2 (appel)
    en_tete_mieux(4, "ALP")
    en_tete_mieux(10, "Thomas Servettaz")
    en_tete_mieux(1, "ESIG")
