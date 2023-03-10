import cv2

# Para ler uma imagem é usada o método cv2.imread("imagem.jpg", 0)
# o segundo argumento "0" define a imagem na escala de cinza
img = cv2.imread("imagem.jpg", 0)

escala = 20   # porcentagem %

# Largura e altura da imagem
altura, largura = img.shape

# Redimencionando a imagem
n_largura = int(largura * (escala / 100))
n_altura = int(altura * (escala / 100))

# Tupla contendo as novas dimensões da imagem
dim = (n_largura, n_altura)

# Redimensionando a imagem usando o método cv2.resize()
img_redimencionada = cv2.resize(img, dim, cv2.INTER_AREA)

# Para visualizar a imagem em uma tela, usa-se o método cv2.imshow()
cv2.imshow("Imagem Original", img)

# Mostrando imagem redimencionada
cv2.imshow("Imagem Redimencionanda", img_redimencionada)

# Para que a imagem não feche, usa-se o método cv2.waitKey(0),
# o 0 ezpecifica um loop infinito
cv2.waitKey(0)

# O método cv2.destroyAllWindows() destroi todas as janelas criadas
cv2.destroyAllWindows()

# O método cv2.imwrite() é usada para salvar uma imagem.
cv2.imwrite("Imagem na Escala de Cinza.png", img)
