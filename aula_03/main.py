# IMportação da biblioteca OpenCv
import cv2

# Carregando a imagem e salvando em uma variável.
img = cv2.imread("imagem.jpg", 1)

escala = 20  # Escala de redução em porcentagem %

# Pegando a altura e largura da imagem original.
altura, largura, _ = img.shape

# Usando as dimensões da imagem original para criar as novas
# dimensões da imagem.
n_largura = int(largura * escala/100)
n_altura = int(altura * escala/100)

# Criando uma tupla contendo as novas dimensões da imagem.
dim = (n_largura, n_altura)

# usando o método cv2.resize() para redimensionar a imagem,
# esse método recebe três argumentos, o primeiro é a imagem origianal
# o segundo é as novas dimensões da imagem e o último é o método matemático
# usado para redimensionar a imagem.
n_img = cv2.resize(img, dim, cv2.INTER_AREA)

# agora podemos mostrar a imagem
# original usando o método cv2.imshow()
cv2.imshow("Imagem Original", img)

# Agora podemos mostrar a imagem redimensionada
# usando o método cv2.imshow()
cv2.imshow("Imagem Modificada", n_img)

# O método waitKey(0) é usado para que a imagem fique
# sendo mostrada na tela e não feche enquanto não for
# apertada uma tecla.
cv2.waitKey(0)

# o método cv2.imwrite() é usado para salvar a imagem em disco.
cv2.imwrite("imagem_modificada.png", n_img)

# o método CV2.destroyAllWindows() finaliza todas as janelas
# do opencv abertas.
cv2.destroyAllWindows()
