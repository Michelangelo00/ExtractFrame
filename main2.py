#pip uninstall opencv-python
#pip install opencv-python==4.5.5.62



import cv2
import os

webcam = cv2.VideoCapture(0)
currentframe = 0
pathExtraction = r"D:\Università\Tirocinio\OpenFace_2.2.0_win_x64\FeatureExtraction.exe"
command = " -aus -f"
pathImmagine = r" D:\Università\Tirocinio\Python\ExtractFrame"
pathComplete = r""




while True:
    success, frame = webcam.read()
    cv2.imshow("Output", frame)
    #immagine = r"\frame" + str(currentframe) + ".jpg"
    cv2.imwrite('frame' + str(currentframe) + '.jpg', frame)
    #pathComplete = pathExtraction + command + pathImmagine + immagine
    #print(pathComplete)
    #os.system(pathComplete)
    """
        TODO:
            - Estrarre da ogni frame le AU (Provare script bash: FeatureExtraction.exe -aus -f "D:\\Università\\Tirocinio\\Python\\ExtractFrame\\frame32.jpg")
            - Convertire file CSV in output in file JSON
    """
    currentframe += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#print("After saving image:")
#print(os.listdir(r"D:\Università\Tirocinio\Python\ExtractFrame"))
webcam.release()
cv2.destroyAllWindows()
for image in os.listdir(r"D:\Università\Tirocinio\Python\ExtractFrame"):
    if "frame" in image:
        #print(image)
        pathComplete = pathExtraction + command + pathImmagine + "\\" + image
        print(pathComplete)
        os.system(pathComplete)

