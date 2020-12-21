# Thomas Servettaz
# 07.12.2020

def en_tete():
    print("**********STADE GENEVE**********")
    print("********************************")


def en_tete_mieux(nb_etoiles, titre):
    # print("**********STADE GENEVE**********")
    print(nb_etoiles * "*", titre, nb_etoiles * "*")
    print("*" * (nb_etoiles + len(titre) + 2 + nb_etoiles))


def affiche_categ():
    nom = input('Quel est votre nom? : ')
    genre = input('Quel est votre genre? (h pour homme, f pour femme) : ')
    age = int(input('Quel est votre âge? : '))
    temps = float(input('Quel est votre meilleur temps sur 100m? : '))
    categorie = '?'

    if genre == 'f':
        if age < 18:
            categorie = 'FEMME J'
        elif temps <= 15.0:
            categorie = 'FEMME 1'
        else:
            categorie = 'FEMME 2'
    elif genre == 'h':
        if age < 18:
            categorie = 'HOMME J'
        elif temps < 14.5:
            categorie = 'HOMME 1'
        elif temps <= 16.0:
            categorie = 'HOMME 2'
        else:
            categorie = 'HOMME 3'

    print('votre categorie est: {}'.format(categorie))

def trouve_categorie(age, genre, temps):
    categorie = '?'
    if genre == 'f':
        if age < 18:
            categorie = 'FEMME J'
        elif temps <= 15.0:
            categorie = 'FEMME 1'
        else:
            categorie = 'FEMME 2'
    elif genre == 'h':
        if age < 18:
            categorie = 'HOMME J'
        elif temps < 14.5:
            categorie = 'HOMME 1'
        elif temps <= 16.0:
            categorie = 'HOMME 2'
        else:
            categorie = 'HOMME 3'
    return categorie

def reptemps():
    for i in range(100,161):
        temps = i/10
        categorie = '?'
        if temps <= 15.0:
            categorie = 'FEMME 1'
        else:
            categorie = 'FEMME 2'
        print("{} --> {}".format(temps, categorie))

def reptemps_mieux_1(de , a):
    for i in range(int(de*10),int(a*10)+1):
        temps = i/10
        categorie = '?'
        if temps <= 15.0:
            categorie = 'FEMME 1'
        else:
            categorie = 'FEMME 2'
        print("{} --> {}".format(temps, categorie))

def reptemps_mieux_2(de , a, age, genre):
    for i in range(int(de*10),int(a*10)+1):
        temps = i/10
        print("{} --> {}".format(temps, trouve_categorie(age, genre, temps)))


def afficher_noms(names):
    for n in names:
        print(n)

    #équivalent à
    #for i in range(0,len(names)):
    #    print(names[i])

    #équivalent à
    #i=0
    #while i < len(names):
    #    print(names[i])
    #    i += 1


def affiche_un_athlete(name, age, is_male):
    homme_ou_femme = 'femme'
    if is_male:
        homme_ou_femme = 'homme'
    print('{} - {} - {} ans'.format(name, homme_ou_femme, age))


def afficher_athletes(names, ages, is_male):
    for i in range(0,len(names)):
        affiche_un_athlete(names[i], ages[i], is_male[i])


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
    #en_tete_mieux(10, "Thomas Servettaz")
    #en_tete_mieux(1, "ESIG")

    #exercice 3
    #affiche_categ()
    #affiche_categ()
    #affiche_categ()

    #exercice 4
    #reptemps()

    #exercice 5
    #reptemps_mieux_1(8,16.5)
    #print(' *** ')
    #reptemps_mieux_2(9.5,15.8,25,'f')

    #exercice 6
    #afficher_noms(names)

    #exercice 7
    afficher_athletes(names, ages, is_male)
