import cv2

img = cv2.imread("imagem.jpg", 1)

escala = 10  # Escala de redução em porcentagem %

altura, largura, _ = img.shape

n_largura = int(largura * escala/100)
n_altura = int(altura * escala/100)

dim = (n_largura, n_altura)

n_img = cv2.resize(img, dim, cv2.INTER_AREA)

cv2.imshow("Imagem Original", img)

cv2.imshow("Imagem Modificada", n_img)

cv2.waitKey(0)

cv2.imwrite("imagem_modificada.png", n_img)

cv2.destroyAllWindows()
