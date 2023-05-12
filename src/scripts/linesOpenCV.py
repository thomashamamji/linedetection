import cv2
import numpy as np
import sys

logPath = "../../log/lineOpenCV.log"

sys.path.insert(1, logPath)
from lib.logger import LOG
internal = LOG(logPath)

def detecter_ligne(image):
    # Convertir l'image en niveaux de gris
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou gaussien pour réduire le bruit
    flou = cv2.GaussianBlur(gris, (5, 5), 0)

    # Appliquer la détection de contours de Canny
    contours = cv2.Canny(flou, 50, 150)

    # Trouver les lignes à l'aide de la transformation de Hough
    lignes = cv2.HoughLinesP(contours, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

    # Dessiner les lignes détectées sur l'image originale
    if lignes is not None:
        internal.log(f"New lines detected !")
        for ligne in lignes:
            x1, y1, x2, y2 = ligne[0]
            internal.log(f"[({x1},{x2},{y1},{y2})]")
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)

    # Afficher l'image avec les lignes détectées
    cv2.imshow("Detection de ligne", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Charger l'image
image = cv2.imread("../../samples/5.jpg")

# Appeler la fonction pour détecter la ligne
detecter_ligne(image)