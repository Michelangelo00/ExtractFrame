#pip uninstall opencv-python
#pip install opencv-python==4.5.5.62



import cv2

webcam = cv2.VideoCapture(0)
currentframe = 0

while True:
    success, frame = webcam.read()

    cv2.imshow("Output", frame)
    cv2.imwrite('frame' + str(currentframe) + '.jpg', frame)
    currentframe += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()