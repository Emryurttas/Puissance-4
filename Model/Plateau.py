from Model.Pion import *
from Model.Constantes import *

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
    if not type_plateau(plateau):
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
    if not type_plateau(plateau):
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) is not int:
        raise TypeError("detecter4horizontalPlateau : Le second paramètre n’est pas un entier")
    if couleur not in [0, 1]:
        raise ValueError(f"detecter4horizontalPlateau : La valeur de la couleur {couleur} n’est pas correcte")
    serie_liste = []
    tab = []
    for ligne in range(const.NB_LINES):
        for col in range(const.NB_COLUMNS - 3):
            if plateau[ligne][col] is not None and plateau[ligne][col][const.COULEUR] == couleur and plateau[ligne][col + 1] is not None and plateau[ligne][col + 1][const.COULEUR] == couleur and plateau[ligne][col + 2] is not None and plateau[ligne][col + 2][const.COULEUR] == couleur and plateau[ligne][col + 3] is not None and plateau[ligne][col + 3][const.COULEUR] == couleur:
                coord_pions = [(ligne, col),
                               (ligne, col + 1),
                               (ligne, col + 2),
                               (ligne, col + 3)
                               ]
                i = 0
                while i < 4 and not (coord_pions[i] in tab):
                    i += 1
                if i == 4:
                    tab.extend(coord_pions)

    for coord in tab:
        serie_liste.append(plateau[coord[0]][coord[1]])

    return serie_liste

def detecter4verticalPlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui permet de détecter si 4 pions de la même couleur passé en paramètre sont alignés verticalement dans le plateau
    :param plateau: Liste de liste qui définit le plateau du jeu
    :param couleur:Défini par 0 ou 1 pour indiquer la couleur du pion (jaune ou rouge)
    :return:retourne une liste vide s’il n’y a aucune série de 4 pions de la couleur donnée alignés
    verticalement, sinon une liste de ces pions qui sont alignés par 4
    """
    if not type_plateau(plateau):
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) is not int:
        raise TypeError("detecter4verticalPlateau : Le second paramètre n’est pas un entier")
    if couleur not in [0, 1]:
        raise ValueError(f"detecter4verticalPlateau : La valeur de la couleur {couleur} n’est pas correcte")

    serie_liste = []
    tab = []
    for col in range(const.NB_COLUMNS):
        for ligne in range(const.NB_LINES - 3):
            if (plateau[ligne][col] is not None and plateau[ligne][col][const.COULEUR] == couleur and
                plateau[ligne + 1][col] is not None and plateau[ligne + 1][col][const.COULEUR] == couleur and
                plateau[ligne + 2][col] is not None and plateau[ligne + 2][col][const.COULEUR] == couleur and
                plateau[ligne + 3][col] is not None and plateau[ligne + 3][col][const.COULEUR] == couleur):
                coord_pions = [(ligne, col),
                               (ligne + 1, col),
                               (ligne + 2, col),
                               (ligne + 3, col)]
                i = 0
                while i < 4 and not (coord_pions[i] in tab):
                    i += 1
                if i == 4:
                    tab.extend(coord_pions)

    for coord in tab:
        serie_liste.append(plateau[coord[0]][coord[1]])

    return serie_liste



def detecter4diagonaleDirectePlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui détécte s'il ya un ou plusieurs diagonale directe de 4 pions de la même couleur passé en paramètre
    :param plateau: Liste de liste qui définit le plateau du jeu
    :param couleur: Défini par 0 ou 1 pour indiquer la couleur du pion (jaune ou rouge)
    :return: retourne une liste vide s’il n’y a aucune série de 4 pions de la couleur donnée alignee
    sur une diagonale « directe », sinon une liste de ces pions qui sont alignés par 4
    """
    if not type_plateau(plateau):
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) is not int:
        raise TypeError("detecter4diagonaleDirectePlateau : Le second paramètre n’est pas un entier")
    if couleur not in [0, 1]:
        raise ValueError(f"detecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n’est pas correcte")

    serie_liste = []
    tab = []
    for ligne in range(const.NB_LINES - 3):
        for col in range(const.NB_COLUMNS - 3):
            # Vérifier la diagonale directe
            if (plateau[ligne][col] is not None and plateau[ligne][col][const.COULEUR] == couleur and
                plateau[ligne+1][col+1] is not None and plateau[ligne+1][col+1][const.COULEUR] == couleur and
                plateau[ligne+2][col+2] is not None and plateau[ligne+2][col+2][const.COULEUR] == couleur and
                plateau[ligne+3][col+3] is not None and plateau[ligne+3][col+3][const.COULEUR] == couleur):
                coord_pions = [
                    (ligne, col),
                    (ligne + 1, col + 1),
                    (ligne + 2, col + 2),
                    (ligne + 3, col + 3)
                ]

                i = 0
                while i < 4 and not (coord_pions[i] in tab):
                    i += 1
                if i == 4:
                    tab.extend(coord_pions)

    for coord in tab:
        serie_liste.append(plateau[coord[0]][coord[1]])

    return serie_liste


def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int) -> list:
    """
    Fonction qui détécte s'il ya un ou plusieurs diagonales indirecte de 4 pions de la même couleur passé en paramètre
    :param plateau: Liste de liste qui définit le plateau du jeu
    :param couleur: Défini par 0 ou 1 pour indiquer la couleur du pion (jaune ou rouge)
    :return:retourne une liste vide s’il n’y a aucune série de 4 pions de la couleur donnée
    alignés sur une diagonale « indirecte », sinon une liste de ces pions qui sont alignés par 4
    """
    if not type_plateau(plateau):
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) is not int:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le second paramètre n’est pas un entier")
    if couleur not in [0, 1]:
        raise ValueError(f"detecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n’est pas correcte")
    serie_liste = []
    tab = []
    for ligne in range(3, const.NB_LINES):
        for col in range(const.NB_COLUMNS - 3):
            if (plateau[ligne][col] is not None and plateau[ligne][col][const.COULEUR] == couleur and
                plateau[ligne-1][col+1] is not None and plateau[ligne-1][col+1][const.COULEUR] == couleur and
                plateau[ligne-2][col+2] is not None and plateau[ligne-2][col+2][const.COULEUR] == couleur and
                plateau[ligne-3][col+3] is not None and plateau[ligne-3][col+3][const.COULEUR] == couleur):
                coord_pions = [
                    (ligne, col),
                    (ligne - 1, col + 1),
                    (ligne - 2, col + 2),
                    (ligne - 3, col + 3)
                ]

                i = 0
                while i < 4 and not (coord_pions[i] in tab):
                    i += 1
                if i == 4:
                    tab.extend(coord_pions)

    for coord in tab:
        serie_liste.append(plateau[coord[0]][coord[1]])

    return serie_liste
def getPionsGagnantsPlateau(plateau: list) -> list:
    """
    Fonction qui cherche toutes les séries s de 4 pions alignés trouvées, pour
    les deux couleurs
    :param plateau:Liste de liste qui définit le plateau du jeu
    :return:retourne la liste de toutes les séries de 4 pions alignés trouvées, pour
    les deux couleurs
    """
    if not type_plateau(plateau):
        raise TypeError("getPionsGagnantsPlateau : Le paramètre ne correspond pas à un plateau")
    pions_gagnants = []

    for couleur in [0, 1]:
        pions_gagnants.extend(detecter4horizontalPlateau(plateau, couleur))
        pions_gagnants.extend(detecter4verticalPlateau(plateau, couleur))
        pions_gagnants.extend(detecter4diagonaleDirectePlateau(plateau, couleur))
        pions_gagnants.extend(detecter4diagonaleIndirectePlateau(plateau, couleur))

    return pions_gagnants


def isRempliPlateau(plateau: list) -> bool:
    """
    Fonction qui permet de déterminer si un plateau est rempli
    :param plateau: Liste de liste qui définit le plateau du jeu
    :return: i retourne True si le plateau est complètement rempli de pions, False sinon
    """
    if not type_plateau(plateau):
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


def placerPionLignePlateau(plateau: list, pion: dict, ligne: int, left: bool) -> bool:
    """
    Place le pion sur la ligne indiquée par la gauche si le booléen left vaut True ou par la droite sinon,
    en poussant les éventuels pions existants sur la ligne. Retourne un tuple constitué de la liste des pions
    poussés (commençant par le pion ajouté) et un entier correspondant au numéro de ligne où se retrouve
    le dernier pion de la liste ou None si le dernier pion ne change pas de ligne. Si le dernier pion est éjecté du
    plateau, l’entier vaudra const.NB_LINES.

    :param plateau: Liste représentant le plateau du jeu.
    :param pion: Dictionnaire représentant le pion à placer.
    :param ligne: Numéro de ligne où placer le pion (entre 0 et const.NB_LINES - 1).
    :param left: Booléen indiquant si le pion est poussé par la gauche (True) ou la droite (False).
    :return: Tuple (pions_pousses, dernier_pion_ligne)
    """
    # Validation des types de paramètres
    if not type_plateau(plateau):
        raise TypeError("placerPionLignePlateau : Le premier paramètre n’est pas un plateau")
    if not type_pion(pion):
        raise TypeError("placerPionLignePlateau : Le second paramètre n’est pas un pion")
    if type(ligne) is not int:
        raise TypeError("placerPionLignePlateau : le troisième paramètre n’est pas un entier")
    if ligne < 0 or ligne >= const.NB_LINES:
        raise ValueError(f"placerPionLignePlateau : Le troisième paramètre ({ligne}) ne désigne pas une ligne")
    if type(left) is not bool:
        raise TypeError("placerPionLignePlateau : le quatrième paramètre n’est pas un booléen")

    pions_pousses = [pion]
    dernier_pion_ligne = None

    if left:
        for i in range(const.NB_COLUMNS - 1, 0, -1):
            if plateau[ligne][i - 1] is not None:
                pions_pousses.append(plateau[ligne][i - 1])


        for i in range(1, const.NB_LINES):
            if ligne + i < const.NB_LINES and plateau[ligne + i][0] is None:
                dernier_pion_ligne = ligne + i
            elif ligne + i >= const.NB_LINES or plateau[ligne + i][0] is not None:
                dernier_pion_ligne = min(ligne + i - 1, const.NB_LINES - 1)


        pions_a_placer = pions_pousses

    else:
        for i in range(const.NB_COLUMNS - 1):
            if plateau[ligne][i + 1] is not None:
                pions_pousses.append(plateau[ligne][i + 1])


        for i in range(1, const.NB_LINES):
            if ligne + i < const.NB_LINES and plateau[ligne + i][const.NB_COLUMNS - 1] is None:
                dernier_pion_ligne = ligne + i
            elif ligne + i >= const.NB_LINES or plateau[ligne + i][const.NB_COLUMNS - 1] is not None:
                dernier_pion_ligne = plateau[ligne][i+1]


        pions_a_placer = pions_pousses


    for i, pion in enumerate(pions_a_placer):
        if dernier_pion_ligne is not None:
            target_line = min(dernier_pion_ligne + i, const.NB_LINES - 1)
            plateau[target_line][0] = pion
    return pions_pousses, dernier_pion_ligne