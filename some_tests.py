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
print("\x1B[43m \x1B[0m : carré jaune ")
print("\x1B[41m \x1B[0m : carré rouge ")
print("\x1B[41mA\x1B[0m : A sur fond rouge")
def test_detecter4horizontalPlateau () -> None:
    exemple_plateau = [
        [1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 1, 1, 1],
    ]
    resultat_detection = detecter4horizontalPlateau(exemple_plateau, 1)
    print(resultat_detection)
    return None

test_detecter4horizontalPlateau()

def test_detecter4verticalPlateau () -> None:
    exemple_plateau = [
        [1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 0, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1],
    ]
    resultat_detection = detecter4verticalPlateau(exemple_plateau, 1)
    print(resultat_detection)
    return None

test_detecter4verticalPlateau()
def test_detecter4diagonaleDirectePlateau() -> None:
    exemple_plateau = [
        [1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 0, 1],
        [1, 0, 0, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 1, 1, 1, 1],
    ]
    resultat_detection = detecter4diagonaleDirectePlateau(exemple_plateau, 1)
    print(resultat_detection)
    return None
test_detecter4diagonaleDirectePlateau()

def test_detecter4diagonaleIndirectePlateau() -> None:
    exemple_plateau = [
        [1, 1, 1, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 1],
        [0, 1, 0, 1, 0, 1, 1],
        [1, 0, 0, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 1],
    ]
    resultat_detection = detecter4diagonaleIndirectePlateau(exemple_plateau, 1)
    print(resultat_detection)
    return None
test_detecter4horizontalPlateau()

def test_getPionsGagnantsPlateau() -> None:
    exemple_plateau = [
        [1, 1, 0, 1, 0, 1, 1],
        [0, 0, 0, 1, 1, 0, 1],
        [1, 0, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 1, 0],
        [1, 0, 0, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 1, 1],
    ]
    resultat_detection = getPionsGagnantsPlateau(exemple_plateau)
    print(resultat_detection)
    return None
test_getPionsGagnantsPlateau()
