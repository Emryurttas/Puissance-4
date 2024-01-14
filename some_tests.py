from Model.Constantes import *
from Model.Plateau import *
from Model.Pion import *
p = construirePlateau()
print(p)
pion = construirePion(const.JAUNE)
line = placerPionPlateau(p, pion, 2)
print("Placement d’un pion en colonne 2. Numéro de ligne :", line)
print(p)
# Essais sur les couleurs


def couleur_carre(color):
    if color == 0:
        return "\x1B[43m \x1B[0m"  # Carré jaune
    elif color == 1:
        return "\x1B[41m \x1B[0m"  # Carré rouge
    else:
        return " "

def gagnant(board, piece_gagnant):
    for row in board:
        row_str = ""
        for square in row:
            if {'Couleur': square} in piece_gagnant:
                row_str += f"\x1B[31m{couleur_carre(square)}\x1B[0m"
            else:
                row_str += couleur_carre(square)
        print(row_str)
# Exemple de plateau
exemple_plateau = [
    [1, 1, 1, 1, 0, 1, 1],
    [0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 1, 1],
]

# Pièces gagnantes
piece_gagnant = [{'Couleur': 1}, {'Couleur': 1}, {'Couleur': 1}, {'Couleur': 1}]

# Affichage du plateau avec les pièces gagnantes mises en évidence
gagnant(exemple_plateau, piece_gagnant)

print(detecter4horizontalPlateau(exemple_plateau, 1))
print(detecter4verticalPlateau(exemple_plateau, 1))
print(detecter4diagonaleDirectePlateau(exemple_plateau, 1))
print(detecter4diagonaleIndirectePlateau(exemple_plateau, 1))
print(getPionsGagnantsPlateau(exemple_plateau))