import cv2

# Le imagem do arquivo
image = cv2.imread('../imagens/dinho.jpg')

# Exibe a imagem
cv2.imshow('Dinho', image)
# Espera infinitamente por uma tecla
cv2.waitKey(0)
cv2.destroyAllWindows()