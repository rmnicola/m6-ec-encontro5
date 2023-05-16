import cv2

# Le imagem do arquivo
image = cv2.imread('../imagens/dinho.jpg')

# Converte para grayscale
gray_dinho = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplica operador de detecção de bordas
edges_dinho = cv2.Canny(gray_dinho, 100, 200)

cv2.imshow('Dinho', image)
cv2.imshow('Gray Dinho', gray_dinho)
cv2.imshow('Bordas dinho', edges_dinho)
cv2.waitKey(0)
cv2.destroyAllWindows()