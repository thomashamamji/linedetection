import cv2
import numpy as np

def augmenter_luminosite(image, alpha, beta):
    # Appliquer la transformation linéaire pour augmenter la luminosité
    image_augmentee = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    # Afficher l'image originale et l'image augmentée côte à côte
    cv2.imshow("Image originale", image)
    cv2.imshow("Image augmentée", image_augmentee)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Charger l'image
image = cv2.imread("../../samples/4.png")

# Définir les paramètres pour augmenter la luminosité
alpha = 1.5  # Facteur de multiplication pour les objets clairs (valeur > 1)
beta = -30  # Valeur à ajouter aux pixels pour les objets sombres (valeur négative)

# Appeler la fonction pour augmenter la luminosité de l'image
augmenter_luminosite(image, alpha, beta)