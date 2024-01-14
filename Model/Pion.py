# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)


def construirePion(couleur: int) -> dict:
    """
    fonction qui construit un pion avec la couleur passé en paramètre
    :param couleur: défini par 0 ou 1 pour indiqué la couleur du pion (jaune ou rouge)
    :return: retourne un dictionnaire définissant le pion
    """
    if type(couleur) is not int:
        raise TypeError('construirePion : Le paramètre n’est pas de type entier')
    if couleur not in const.COULEURS:
        raise ValueError(f'construirePion : la couleur {couleur} n’est pas correcte ')
    pion = {const.COULEUR: couleur, const.ID: None}
    return pion
def getCouleurPion(pion: dict) -> int :
    """
    fonction qui retourne la couleur du pion
    :param pion: dictionnaire qui définit le pion
    :return: retourne un entier pour indiquer la couleur du pion
    """
    if type(pion) is not dict:
        raise TypeError('getCouleurPion : Le paramètre n’est pas un pion')
    couleur = pion[const.COULEUR]
    return couleur

def setCouleurPion(pion: dict, couleur: int) -> None:
    """
    fonction qui modifie la couleur du pion passé en paramètre
    :param pion: dictionnaire qui définit le pion
    :param couleur:
    :return:ne retourne rien
    """
    if type(pion) is not dict:
        raise TypeError("setCouleurPion : Le premier paramètre n’est pas un pion")
    if type(couleur) is not int:
        raise TypeError("setCouleurPion : Le second paramètre n’est pas un entier.")
    if couleur not in const.COULEURS:
        raise ValueError(f"setCouleurPion : Le second paramètre {couleur} n’est pas une couleur")
    pion[const.COULEUR] = couleur
    return None

def getIdPion(pion: dict) -> str:
    """
    fonction qui retourne l'identifiant du pion passé en paramètre
    :param pion: dictionnaire qui définit le pion
    :return: retourne l'identifiant du pion
    """
    if not type_pion(pion):
        raise TypeError("getIdPion : Le premier paramètre n’est pas un pion")
    id = pion[const.ID]
    return id

def setIdPion(pion: dict, id: int)->None:
    """
    fonction qui modifie l'identifiant passé en paramètre
    :param pion: dictionnaire qui définit le pion
    :param id: entier qui va remplacer l'identifiant du pion
    :return: ne retourne rien
    """
    if type(pion) is not dict:
        raise TypeError("setIdPion : Le premier paramètre n’est pas un pion")
    if type(id) is not int:
        raise TypeError("setIdPion : Le premier paramètre n’est pas un pion")
    pion[const.ID] = id
    return None