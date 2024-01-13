from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True

def construirePlateau()->list:
    """
    Fonction qui créé un tableau 2D vide avec nb_ligne et nb_colonne qui sont constantes.
    :return:retourne une liste de liste avec nb_ligne et nb_colonne qui sont constantes.
    """
    plateau = []
    for ligne in range(const.NB_LINES):
        tab = []
        for col in range(const.NB_COLUMNS):
            tab.append(None)
        plateau.append(tab)
    return plateau

def placerPionPlateau(plateau: list, pion: dict, num_col: int) -> int:
    """
    Fonction qui dépose le pion dans la colonne indiquée
    :param plateau: liste de liste qui définit le plateau du jeu
    :param pion: dictionnaire qui définit la couleur et l'identifiant du pion
    :param num_col: le numéro de colonne pour placer le pion dans le plateau
    :return: retourne le numéro de ligne où se trouve le pion
    """
    if type(plateau) is not list:
        raise TypeError("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(pion) is not dict:
        raise TypeError("placerPionPlateau : Le second paramètre n’est pas un pion ")
    if type(num_col) is not int:
        raise TypeError("placerPionPlateau : Le troisième paramètre n’est pas un entier")
    if num_col > const.NB_COLUMNS-1 and num_col < 0:
        raise ValueError(f"placerPionPlateau : La valeur de la colonne {num_col} n’est pas correcte")
    num_ligne = const.NB_LINES - 1
    while num_ligne >= 0 and plateau[num_ligne][num_col] is not None:
        num_ligne -= 1
    if num_ligne >= 0:
        plateau[num_ligne][num_col] = pion
    return num_ligne


def detecter4horizontalPlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui permet de détecter si 4 pions de la même couleur passé en paramètre sont alignés horizontalement
    :param plateau: Liste de liste qui définit le plateau du jeu
    :param couleur: Défini par 0 ou 1 pour indiquer la couleur du pion (jaune ou rouge)
    :return: Retourne une liste vide s’il n’y a aucune série de 4 pions alignés horizontalement
    du couleur passé en paramètre,
    sinon une liste de pions de la couleur donnée en paramètre qui sont alignés par 4
    """
    if type(plateau) is not list:
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) is not int:
        raise TypeError("detecter4horizontalPlateau : Le second paramètre n’est pas un entier")
    if couleur not in [0, 1]:
        raise ValueError(f"detecter4horizontalPlateau : La valeur de la couleur {couleur} n’est pas correcte")
    serie_liste = []
    compteur = 0
    derniere_ligne = None
    for ligne in range(const.NB_LINES):
        for col in range(const.NB_COLUMNS):
            if plateau[ligne][col] == couleur:
                compteur += 1
                if compteur == 4 and col >= 3:
                    serie_liste.extend([
                        {const.COULEUR: couleur},
                        {const.COULEUR: couleur},
                        {const.COULEUR: couleur},
                        {const.COULEUR: couleur},
                    ])
                    compteur = 0
            else:
                compteur = 0

        if derniere_ligne is not None and derniere_ligne != ligne:
            compteur = 0
        derniere_ligne = ligne
    return serie_liste

def detecter4verticalPlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui permet de détecter si 4 pions de la même couleur passé en paramètre sont alignés verticalement dans le plateau
    :param plateau: Liste de liste qui définit le plateau du jeu
    :param couleur:Défini par 0 ou 1 pour indiquer la couleur du pion (jaune ou rouge)
    :return:retourne une liste vide s’il n’y a aucune série de 4 pions de la couleur donnée alignés
    verticalement, sinon une liste de ces pions qui sont alignés par 4
    """
    if type(plateau) is not list:
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) is not int:
        raise TypeError("detecter4verticalPlateau : Le second paramètre n’est pas un entier")
    if couleur not in [0, 1]:
        raise ValueError(f"detecter4verticalPlateau : La valeur de la couleur {couleur} n’est pas correcte")

    serie_liste = []
    compteur = 0
    derniere_colonne = None

    for col in range(const.NB_COLUMNS):
        for ligne in range(const.NB_LINES):
            if plateau[ligne][col] == couleur:
                compteur += 1
                if compteur == 4 and ligne >= 3:
                    serie_liste.extend([
                        {const.COULEUR: couleur},
                        {const.COULEUR: couleur},
                        {const.COULEUR: couleur},
                        {const.COULEUR: couleur},
                    ])
                    compteur = 0
            else:
                compteur = 0

        if derniere_colonne is not None and derniere_colonne != col:
            compteur = 0
        derniere_colonne = col
    return serie_liste



def detecter4diagonaleDirectePlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui détécte s'il ya un ou plusieurs diagonale directe de 4 pions de la même couleur passé en paramètre
    :param plateau: Liste de liste qui définit le plateau du jeu
    :param couleur: Défini par 0 ou 1 pour indiquer la couleur du pion (jaune ou rouge)
    :return: retourne une liste vide s’il n’y a aucune série de 4 pions de la couleur donnée alignee
    sur une diagonale « directe », sinon une liste de ces pions qui sont alignés par 4
    """
    if type(plateau) is not list:
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) is not int:
        raise TypeError("detecter4diagonaleDirectePlateau : Le second paramètre n’est pas un entier")
    if couleur not in [0, 1]:
        raise ValueError(f"detecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n’est pas correcte")
    serie_liste = []
    tab = []
    for ligne in range(const.NB_LINES - 3):
        for col in range(const.NB_COLUMNS - 3):
            if plateau[ligne][col] == couleur and plateau[ligne+1][col+1] == couleur and plateau[ligne+2][col+2] == couleur and plateau[ligne+3][col+3] == couleur:
                coord_pions = [(ligne, col),
                               (ligne + 1, col + 1),
                               (ligne + 2, col + 2),
                               (ligne + 3, col + 3)
                               ]
                i = 0
                while i < 4 and not (coord_pions[i] in tab):
                    i += 1
                if i == 4:
                    tab.extend(coord_pions)

    for i in range(len(tab)):
        serie_liste.append({const.COULEUR: couleur})

    return serie_liste


def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui détécte s'il ya un ou plusieurs diagonales indirecte de 4 pions de la même couleur passé en paramètre
    :param plateau: Liste de liste qui définit le plateau du jeu
    :param couleur: Défini par 0 ou 1 pour indiquer la couleur du pion (jaune ou rouge)
    :return:retourne une liste vide s’il n’y a aucune série de 4 pions de la couleur donnée
    alignés sur une diagonale « indirecte », sinon une liste de ces pions qui sont alignés par 4
    """
    if type(plateau) is not list:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) is not int:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le second paramètre n’est pas un entier")
    if couleur not in [0, 1]:
        raise ValueError(f"detecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n’est pas correcte")
    serie_liste = []
    tab = []
    for ligne in range(3, const.NB_LINES):
        for col in range(const.NB_COLUMNS - 3):
            if plateau[ligne][col] == couleur and plateau[ligne-1][col+1] == couleur and plateau[ligne-2][col+2] == couleur and plateau[ligne-3][col+3] == couleur:
                coord_pions = [
                    (ligne - 3, col + 3),
                    (ligne - 2, col + 2),
                    (ligne - 1, col + 1),
                    (ligne, col)
                ]

                i = 0
                while i < 4 and not (coord_pions[i] in tab):
                    i += 1
                if i == 4:
                    tab.extend(coord_pions)
    for i in range(len(tab)):
        serie_liste.append({const.COULEUR: couleur})
    return serie_liste


def getPionsGagnantsPlateau(plateau: list) -> list:
    """
    Fonction qui cherche toutes les séries s de 4 pions alignés trouvées, pour
    les deux couleurs
    :param plateau:Liste de liste qui définit le plateau du jeu
    :return:retourne la liste de toutes les séries de 4 pions alignés trouvées, pour
    les deux couleurs
    """
    if type(plateau) is not list:
        raise TypeError("getPionsGagnantsPlateau : Le paramètre ne correspond pas à un plateau")
    pions_gagnants = []

    for couleur in [0, 1]:
        series_couleur = []
        series_couleur.extend(detecter4diagonaleIndirectePlateau(plateau, couleur))
        series_couleur.extend(detecter4diagonaleDirectePlateau(plateau, couleur))
        series_couleur.extend(detecter4verticalPlateau(plateau, couleur))
        series_couleur.extend(detecter4horizontalPlateau(plateau, couleur))

        if series_couleur:
            pions_gagnants.append(series_couleur)
    return pions_gagnants

def isRempliPlateau(plateau: list) -> bool:
    """
    Fonction qui permet de déterminer si un plateau est rempli
    :param plateau: Liste de liste qui définit le plateau du jeu
    :return: i retourne True si le plateau est complètement rempli de pions, False sinon
    """
    if type(plateau) is not list:
        raise TypeError("isRempliPlateau : Le paramètre ne correspond pas à un plateau")
    i = 0
    est_rempli = True

    while i < len(plateau) and est_rempli:
        j = 0
        while j < len(plateau[i]) and est_rempli:
            if plateau[i][j] is None:
                est_rempli = False
            j += 1
        i += 1
    return est_rempli


def construireJoueur(couleur: int) -> dict:
    """
    Fonction qui permet de construire un joueur en l'associant à un couleur
    :param couleur: Défini par 0 ou 1 pour indiquer la couleur du pion (jaune ou rouge)
    :return: retourne un dictionnaire représentant un joueur dans lequel la
    couleur sera initialisée avec le paramètre donné
    """

    if type(couleur) is not int:
        raise TypeError("detecter4diagonaleDirectePlateau : Le second paramètre n’est pas un entier")

    if couleur not in [0, 1]:
        raise ValueError(f"detecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n’est pas correcte")
    joueur = {const.COULEUR: couleur, const.PLATEAU: None, const.PLACER_PION: None}
    return joueur
