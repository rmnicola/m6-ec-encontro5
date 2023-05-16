import cv2

# Le imagem do arquivo
image = cv2.imread('../imagens/dinho.jpg')

# Recorta a imagem       y        x
cropped_dinho = image[366:510, 361:473]

cv2.imshow('Dinho', image)
cv2.imshow('Cropped Dinho', cropped_dinho)
cv2.waitKey(0)
cv2.destroyAllWindows()