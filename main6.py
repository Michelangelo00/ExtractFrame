import cv2
import os
from subprocess import Popen, PIPE
import glob

webcam = cv2.VideoCapture(0)
currentframe = 0
pathExtraction = r"D:\Università\Tirocinio\OpenFace_2.2.0_win_x64\FeatureExtraction.exe"
command = " -aus -f"
pathImmagine = r" D:\Università\Tirocinio\Python\ExtractFrame"
pathComplete = r""
pathNoComplete = pathExtraction + command + pathImmagine


while True:
    success, frame = webcam.read()
    cv2.imshow("Output", frame)
    cv2.imwrite('frame' + str(currentframe) + '.jpg', frame)
    currentframe += 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

f_list = glob.glob('*jpg')
cmds_list = []
pathCompleteQuasi = pathNoComplete + "\\"

for file_name in f_list:
    pathComplete = pathCompleteQuasi + file_name
    cmds_list.append(pathComplete)

procs_list = [Popen(cmd, stdout=PIPE, stderr=PIPE) for cmd in cmds_list]
for processo in procs_list:
    print(processo)
for proc in procs_list:
    proc.wait()


