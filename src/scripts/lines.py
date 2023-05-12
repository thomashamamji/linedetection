import cv2
import numpy as np
import sys

logPath = "../../logs/lines.log"

sys.path.insert(1, logPath)
from lib.logger import LOG
internal = LOG(logPath)

def detecter_line(image):
    # Convertir l'image en niveaux de grey
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    vague = cv2.GaussianBlur(grey, (5, 5), 0)

    # Appliquer la détection de contours de Canny
    contours = cv2.Canny(vague, 50, 150)

    # Trouver les lines à l'aide de la transformation de Hough
    lines = cv2.HoughLinesP(contours, 1, np.pi / 180, 100, minLineLength=100, maxLineGap=10)

    # Dessiner les lines détectées sur l'image originale
    if lines is not None:
        internal.log(f"New lines detected !")
        for line in lines:
            x1, y1, x2, y2 = line[0]
            internal.log(f"[({x1},{x2},{y1},{y2})]")
            cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 3)

    # Afficher l'image avec les lines détectées
    cv2.imshow("Line detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function calls

image = cv2.imread("../../samples/5.jpg")
detecter_line(image)