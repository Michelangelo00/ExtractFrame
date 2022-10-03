import os
import glob


def estr(pathNoComplete):

    # CREAZIONE LISTA CHE TUTTI I FRAME SALVATI IN PRECEDENZA
    f_list = glob.glob('*jpg')

    # CREAZIONE LISTA VUOTA --> USATA PER CONTENERE STRINGHE CON IL COMANDO DI ESTRAZIONE PER OGNI FRAME
    cmds_list = []

    # STRINGA DI APPOGGIO
    pathCompleteQuasi = pathNoComplete + "\\"

    # LOOP PER INSERIMENTO COMANDI NELLA LISTA
    for file_name in f_list:
        pathComplete = pathCompleteQuasi + file_name
        cmds_list.append(pathComplete)

    return cmds_list
