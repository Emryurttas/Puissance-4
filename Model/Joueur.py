from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *



#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.

    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None
            and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and
        not type_plateau(joueur[const.PLATEAU])):
        return False
    return True


def getCouleurJoueur(joueur: dict) -> int:
    """
    Fonction qui reçoit un dictionnaire représentant un joueur et renvoie la couleur du joueur
    :param joueur:Dictionnaire représentant un joueur
    :return:La couleur du joueur (0 ou 1)
    """
    if not type_joueur(joueur):
        raise TypeError("getCouleurJoueur : Le paramètre ne correspond pas à un joueur")
    couleur = joueur[const.COULEUR]
    return couleur

def getPlateauJoueur(joueur: dict) -> list:
    """
        Fonction qui reçoit un dictionnaire représentant un joueur et renvoie le plateau du joueur
        :param joueur: Dictionnaire représentant un joueur
        :return: Le plateau du joueur (une liste de listes)
        """
    if not type_joueur(joueur):
        raise TypeError("getPlateauJoueur : Le paramètre ne correspond pas à un joueur")
    plateau = joueur[const.PLATEAU]

    return plateau

def getPlacerPionJoueur(joueur: dict) -> callable:
    """
    Fonction qui reçoit un dictionnaire représentant un joueur et renvoie la fonction de placement de pion du joueur
    :param joueur: Dictionnaire représentant un joueur
    :return: La fonction de placement de pion du joueur
    """
    if not type_joueur(joueur):
        raise TypeError("getPlacerPionJoueur : Le paramètre ne correspond pas à un joueur")
    placer_pion = joueur[const.PLACER_PION]
    return placer_pion

def getPionJoueur(joueur: dict) -> dict:
    """
    Fonction qui reçoit un dictionnaire représentant un joueur et retourne un pion de la couleur du joueur
    :param joueur: Dictionnaire représentant un joueur
    :return: Un pion de la couleur du joueur
    """
    if not type_joueur(joueur):
        raise TypeError("getPionJoueur : Le paramètre ne correspond pas à un joueur")

    couleur = joueur[const.COULEUR]
    pion = {const.COULEUR: couleur, const.ID: None}
    return pion

def setPlateauJoueur(joueur: dict, plateau: list) -> None:
    """
    Affecte un plateau au joueur.
    :param joueur: Dictionnaire représentant un joueur.
    :param plateau: Liste représentant un plateau.
    :return: None
    """
    if not type_joueur(joueur):
        raise TypeError("setPlateauJoueur : Le premier paramètre ne correspond pas à un joueur")

    if not type_plateau(plateau):
        raise TypeError("setPlateauJoueur : Le second paramètre ne correspond pas à un plateau")

    joueur[const.PLATEAU] = plateau
    return None

def setPlacerPionJoueur(joueur: dict, placer_pion_func: callable) -> None:
    """
    Affecte une fonction de placement de pion à un joueur.

    :param joueur: Dictionnaire représentant un joueur.
    :param placer_pion_func: Callable contenant une fonction de placement de pion.
    :return: None
    """
    if not type_joueur(joueur):
        raise TypeError("setPlacerPionJoueur : Le premier paramètre ne correspond pas à un joueur")

    if not callable(placer_pion_func):
        raise TypeError("setPlacerPionJoueur : Le second paramètre n'est pas une fonction")

    joueur[const.PLACER_PION] = placer_pion_func
    return None


def _placerPionJoueur(joueur: dict) -> int:
    """
    Place un pion pour le joueur sur le plateau en choisissant une colonne aléatoire.

    :param joueur: Dictionnaire représentant un joueur.
    :return: Colonne choisie pour placer le pion
    """
    from random import randint
    if not type_joueur(joueur):
        raise TypeError("_placerPionJoueur : Le paramètre n’est pas un joueur")

    plateau = joueur.get(const.PLATEAU)
    colonnes_disponibles = list(range(const.NB_COLUMNS))
    pas_rempli = True
    i = 0

    while pas_rempli and i < const.NB_LINES:
        colonne = None

        while colonne is None and colonnes_disponibles:
            colonne_candidat = colonnes_disponibles.pop(randint(0, len(colonnes_disponibles) - 1))
            if plateau[i][colonne_candidat] is None:
                colonne = colonne_candidat

        if colonne is not None:
            pas_rempli = False
        i += 1

    return colonne

def initialiserIAJoueur(joueur: dict, premier: bool) -> None:
    """
    Initialise la fonction de placement de pion d'un joueur en utilisant _placerPionJoueur.

    :param joueur: Dictionnaire représentant un joueur.
    :param premier: Booléen indiquant si le joueur joue en premier (True) ou en second (False).
    :return: Ne retourne rien.
    """
    if not type_joueur(joueur):
        raise TypeError("initialiserIAJoueur : Le premier paramètre n’est pas un joueur")
    if not type(premier) is bool:
        raise TypeError("initialiserIAJoueur : Le second paramètre n’est pas un booléen")
    setPlacerPionJoueur(joueur, _placerPionJoueur)
    return None
