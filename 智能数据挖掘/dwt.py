import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.fftpack import fft,ifft
import math
import pywt
from pandas import DataFrame;
protocol_list=['tcp','udp','icmp']
service_list=['aol','auth','bgp','courier','csnet_ns','ctf','daytime','discard','domain','domain_u',
    'echo','eco_i','ecr_i','efs','exec','finger','ftp','ftp_data','gopher','harvest','hostnames',
    'http','http_2784','http_443','http_8001','imap4','IRC','iso_tsap','klogin','kshell','ldap',
    'link','login','mtp','name','netbios_dgm','netbios_ns','netbios_ssn','netstat','nnsp','nntp',
    'ntp_u','other','pm_dump','pop_2','pop_3','printer','private','red_i','remote_job','rje','shell',
    'smtp','sql_net','ssh','sunrpc','supdup','systat','telnet','tftp_u','tim_i','time','urh_i','urp_i',
    'uucp','uucp_path','vmnet','whois','X11','Z39_50']
flag_list=['OTH','REJ','RSTO','RSTOS0','RSTR','S0','S1','S2','S3','SF','SH']
label_list=['normal.', 'buffer_overflow.', 'loadmodule.', 'perl.', 'neptune.', 'smurf.',
    'guess_passwd.', 'pod.', 'teardrop.', 'portsweep.', 'ipsweep.', 'land.', 'ftp_write.',
    'back.', 'imap.', 'satan.', 'phf.', 'nmap.', 'multihop.', 'warezmaster.', 'warezclient.',
    'spy.', 'rootkit.']



odata=pd.read_csv("D:\code\python\learn\kddcup99\kddcup.data_10_percent_corrected",header =None)
data=np.array(odata)
for m in data:     #字符特征转换为数值
    m[1]=int(protocol_list.index(m[1]))
    m[2]=int(service_list.index(m[2]))
    m[3]=int(flag_list.index(m[3]))
    m[len(data[0])-1]=int(label_list.index(m[len(data[0])-1]))


data_x = data[:][:len(data[0])-1]
wavename = 'db5'
cA, cD = pywt.dwt(data_x, wavename)
ya = pywt.idwt(cA, None, wavename, 'smooth')  # approximated component
yd = pywt.idwt(None, cD, wavename, 'smooth')  # detailed component
x = range(len(data_x))
plt.figure(figsize=(12, 9))
plt.subplot(311)
plt.plot(x, data_x)
plt.title('original signal')
plt.subplot(312)
plt.plot(x, ya)
plt.title('approximated component')
plt.subplot(313)
plt.plot(x, yd)
plt.title('detailed component')
plt.tight_layout()
plt.show()