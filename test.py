import cv2

video = cv2.VideoCapture("aula_03/demo.mp4")

if (video.isOpened()):
    fps = video.get(5)
    print(f"Quadros por segundo: {fps}FPS")

    contagem_quadros = video.get(7)
    print(f"Contagem de quadros: {contagem_quadros}")
else:
    print("Erro ao abrir o vídeo!")

tr = True
while tr:
    ret, quadro = video.read()
    tr = ret
    if ret is True:
        cv2.imshow("Quadro", quadro)

        key = cv2.waitKey(20)

        if key == ord("q"):
            break
video.release()
cv2.destroyAllWindows()
