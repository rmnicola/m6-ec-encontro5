import cv2

# Le imagem
image = cv2.imread('../imagens/dinho.jpg')

# Converte para grayscale
gray_dinho = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Dinho', image)
cv2.imshow('Gray Dinho', gray_dinho)

cv2.waitKey(0)
cv2.destroyAllWindows()