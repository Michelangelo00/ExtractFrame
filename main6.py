

import cv2
from subprocess import Popen, PIPE
import glob

# APERTURA WEBCAM
webcam = cv2.VideoCapture(0)

#INIZIALIZZAZIONE VARIABILE PER IL CONTEGGIO DEI FRAME
currentframe = 0

#PATH DOV'E' SITUATO IL FILE CHE PERMETTE L'ESTRAZIONE DELLE AU
pathExtraction = r"D:\Università\Tirocinio\OpenFace_2.2.0_win_x64\FeatureExtraction.exe"

#COMANDI BASH CHE PERMETTO L'ESTRAZIONE UNICA DELLE AU
command = " -aus -f"

#PATH DOVE SONO SITUATE LE IMMAGINI CHE VERRANNO RACCOLTE DALLA WEBCAM
pathImmagine = r" D:\Università\Tirocinio\Python\ExtractFrame"

#PATH FINALE CHE VERRà RIEMPITA DI TUTTE LE STRINGHE PRECEDENTI
pathComplete = r""

#PATH CONTENENTE TUTTE LE STRINGHE PRECEDENTI, MA NON L'IMMAGINE DA DOVE ESTRARRE LE AU
pathNoComplete = pathExtraction + command + pathImmagine

#LOOP INFINITO
while True:
    success, frame = webcam.read()
    cv2.imshow("Output", frame)

    #SALVATAGGIO FRAME NELLA CARTELLA EXTRACTFRAME
    cv2.imwrite('frame' + str(currentframe) + '.jpg', frame)

    #INCREMENTO VARIABILE PER CONTEGGIO FRAME
    currentframe += 1

    #SETTAGGIO TASTO DI SPEGNIMENTO IA
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

#CREAZIONE LISTA CHE TUTTI I FRAME SALVATI IN PRECEDENZA
f_list = glob.glob('*jpg')

#CREAZIONE LISTA VUOTA --> USATA PER CONTENERE STRINGHE CON IL COMANDO DI ESTRAZIONE PER OGNI FRAME
cmds_list = []

#STRINGA DI APPOGGIO
pathCompleteQuasi = pathNoComplete + "\\"

#LOOP PER INSERIMENTO COMANDI NELLA LISTA
for file_name in f_list:
    pathComplete = pathCompleteQuasi + file_name
    cmds_list.append(pathComplete)

#LISTA CHE CONTIENE I COMANDI CHE VENGONO PARALLELIZZATI
procs_list = [Popen(cmd, stdout=PIPE, stderr=PIPE) for cmd in cmds_list]
for processo in procs_list:
    print(processo)
for proc in procs_list:
    proc.wait()


