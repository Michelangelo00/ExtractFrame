import os
from subprocess import Popen, PIPE
import glob

"""
    CREARE LA LISTA CMDS_LIST CON IL MODULO OS COME FATTO NEI PRECEDENTI MAIN, QUINDI
    UNIRE IL METODO OS.SYSTEM CON IL MULTIPROCESSING DI SUBPROCESS
"""
pathExtraction = r"D:\Università\Tirocinio\OpenFace_2.2.0_win_x64\FeatureExtraction.exe"
command = " -aus -f"
pathImmagine = r" D:\Università\Tirocinio\Python\ExtractFrame"
pathComplete = r""
pathNoComplete = pathExtraction + command + pathImmagine


f_list = glob.glob('*jpg')


#cmds_list = [[r"D:\Università\Tirocinio\OpenFace_2.2.0_win_x64\FeatureExtraction.exe", " -aus -f ", file_name] for file_name in f_list]
cmds_list = []
for file_name in f_list:
    pathComplete = pathNoComplete + r"\\" + file_name
    cmds_list.append(pathComplete)

procs_list = [Popen(cmd, stdout=PIPE, stderr=PIPE) for cmd in cmds_list]
for processo in procs_list:
    print(processo)
for proc in procs_list:
    proc.wait()