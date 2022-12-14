#pip uninstall opencv-python
#pip install opencv-python==4.5.5.62



import cv2
import os
import subprocess

webcam = cv2.VideoCapture(0)
currentframe = 0
pathExtraction = r"D:\Università\Tirocinio\OpenFace_2.2.0_win_x64\FeatureExtraction.exe"
command = " -aus -f"
pathImmagine = r" D:\Università\Tirocinio\Python\ExtractFrame"
pathComplete = r""



while True:
    success, frame = webcam.read()
    cv2.imshow("Output", frame)
    immagine = r"\frame" + str(currentframe) + ".jpg"
    cv2.imwrite('frame' + str(currentframe) + '.jpg', frame)
    imageComplete = pathImmagine + immagine
    subprocess.run([r"D:\Università\Tirocinio\OpenFace_2.2.0_win_x64\FeatureExtraction.exe", "-aus", "-f", imageComplete])
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

webcam.release()
cv2.destroyAllWindows()
