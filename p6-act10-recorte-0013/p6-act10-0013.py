import numpy as np
import cv2

#Vision Artificial Act10 NC 0013
# Lee la imagen en escala de grises
img = cv2.imread("Serpiente1.jpg", cv2.IMREAD_GRAYSCALE)

# Abre la ventana con la imagen
cv2.imshow("Serpiente1 0013", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Linea
print("La Linea 0013")
# Crea una imagen negra
img = np.zeros((512,512,3), np.uint8)

# Dibuja una diagonal blanca de 3px desde una esquina a la otra
img = cv2.line(img,(0,0),(511,511),(255,255,255),3)
# Abre la ventana con la imagen
cv2.imshow("Serpiente1 0013", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Circulo
print("El Circulo 0013")
# Dibuja un circulo azul de radio 10px al centro de la imagen
img = cv2.circle(img, (260,260), 10, (255,0,0),-1)
# Abre la ventana con la imagen
cv2.imshow("Serpiente1 0013", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Texto
print("El Texto 0013")
# Añade a la imagen el texto "Serpiente" en color blanco
img = cv2.putText(img, "Serpiente", (200, 30),cv2.FONT_HERSHEY_SIMPLEX, \
                  0.5, (255, 255, 255), 2)
# Abre la ventana con la imagen
cv2.imshow("Serpiente1 0013", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Trackbars

img = cv2.imread('Serpiente1.jpg',0)

ret,thr1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thr2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thr3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thr4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thr5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

cv2.imshow('BINARY',thr1)
cv2.imshow('BINARY_INV',thr2)
cv2.imshow('TRUNC',thr3)
cv2.imshow('TOZERO',thr4)
cv2.imshow('TOZERO_INV',thr5)

# Abre la ventana con la imagen
cv2.imshow("Serpiente1 0013", img)
cv2.waitKey(0)
cv2.destroyAllWindows()