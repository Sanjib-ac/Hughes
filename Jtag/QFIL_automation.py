import subprocess
from SerialSearch import *

#start of user configurable parameter
com_port_vid_pid='05C6:9008'
com_port_str2search='QDLoader'
qfil_exe_path = 'C:\\Program Files (x86)\\Qualcomm\\QPST\\bin\\Qfil.exe'
qfil_programmer_path = '-PROGRAMMER=TRUE;\"C:\hnsops\Executable\QC_Image_C01\prog_nand_firehose_9x55.mbn\"'
qfil_xml_search_path = '-SEARCHPATH=\"C:\hnsops\Executable\QC_Image_C01\"'
qfil_rawprogram_path = '-RawProgram=qpst_mimic_sbl.xml'
qfil_logfile_path = '-LOGFILEPATH=\"C:\hnsops\Executable\QC_Image_C01\qfil_log1.txt\"'
#end of user configurable parameter

# search a comport with com_port_vid_pid and com_port_str2search
com_port = serial_ports(com_port_vid_pid, com_port_str2search, verbose=False)
print(f'Port:{com_port}')
if len(com_port) == 0:
    print(f'Port not found:{com_port}')
    exit()
#make a command string
param_list = [qfil_programmer_path, '-Mode=3 -DOWNLOADFLAT', qfil_xml_search_path, qfil_rawprogram_path, qfil_logfile_path]
for param in param_list :
    qfil_exe_path += ' ' + param

timeout_val_sec = 30
try :
    proc = subprocess.run(qfil_exe_path, capture_output=True, timeout=timeout_val_sec)
    # succeed if "Download Succeed" in stdout
    if 'Download Succeed' in proc.stdout.decode():
        print('Download Succeed')
    #else:
     #   print('Download Fail')

except Exception as e:
    print(f'Download Fail:{str(e)}')
