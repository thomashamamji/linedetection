import cv2
import numpy as np

def diminuer_luminosite(image, gamma):
    inv_gamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
    image_diminuee = cv2.LUT(image, table)

    cv2.imshow("Image originale", image)
    cv2.imshow("Image diminuée", image_diminuee)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = cv2.imread("../../samples/4.png")

gamma = 0.45

diminuer_luminosite(image, gamma)