import cv2
import numpy as np

def diminuer_luminosite(image, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    image_diminuee = cv2.LUT(image, table)

    # Afficher l'image originale et l'image diminuée côte à côte
    cv2.imshow("Image originale", image)
    cv2.imshow("Image diminuée", image_diminuee)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Charger l'image
image = cv2.imread("../../samples/4.png")

# Définir le paramètre gamma pour diminuer la luminosité
gamma = 0.45  # Valeur entre 0 et 1 (plus petit = plus sombre)

# Appeler la fonction pour diminuer la luminosité de l'image
diminuer_luminosite(image, gamma)