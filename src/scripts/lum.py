import cv2
import numpy as np

def augmenter_luminosite(image, alpha, beta):
    image_augmentee = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    cv2.imshow("Image originale", image)
    cv2.imshow("Image augmentée", image_augmentee)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

image = cv2.imread("../../samples/4.png")

alpha = 1.5
beta = -30

augmenter_luminosite(image, alpha, beta)