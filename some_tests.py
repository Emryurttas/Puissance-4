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



exemple_plateau = [
    [{const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 0, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}],
    [{const.COULEUR: 0, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 0, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}],
    [{const.COULEUR: 1, const.ID: None}, {const.COULEUR: 0, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 0, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 0, const.ID: None}],
    [{const.COULEUR: 0, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 0, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}],
    [{const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 0, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 0, const.ID: None}, {const.COULEUR: 0, const.ID: None}, {const.COULEUR: 0, const.ID: None}],
    [{const.COULEUR: 0, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 0, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}, {const.COULEUR: 1, const.ID: None}]
    ]





print(type_plateau(exemple_plateau))
print(detecter4horizontalPlateau(exemple_plateau, 1))
print(detecter4verticalPlateau(exemple_plateau, 0))
print(detecter4diagonaleDirectePlateau(exemple_plateau, 1))
print(detecter4diagonaleIndirectePlateau(exemple_plateau, 1))
