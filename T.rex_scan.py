#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import os.path
import csv
import time
from functools import reduce
import re
# import json
from os import path
from colorama import Back, Fore, init, Style
from time import sleep
from tqdm import tqdm


def almacenardatos():
    """a='c'
    print('s')
    return a"""
    init()
    print(
        Fore.WHITE + "_____________________________________________________________________________________________________________________\n")
    init()
    print(
        Fore.RED + "Coincidencias de (port) o puertos encontrados " + Fore.GREEN + " **************************************")
    print("")
    RED = '\033[1;31m'
    NOCOLOR = '\033[0;0m'

    palabras4 = ['tcp', '.com', 'n/a']

    palabra4 = 'tcp'
    ocurrencias4 = []
    with open('doc.txt') as lineas:
        for linea in lineas:
            if palabra4 in linea:
                ocurrencias4.append(linea)

        # print(aImprimir4)
    return ocurrencias4


def crear_archivo():
    if path.exists('prueba1.txt'):
        print('El archivo ya existe')
        file = open("prueba1.txt", "a")
    else:
        file = open("prueba1.txt", "a")
        print('El archivo fue creado')

        pass


def menu():
    """
Inicio logo         ###################################################################
    """


# Color de texto inicio  ################################################################
# Color de texto fin  ###################################################################
print("")
print("")
print("")
init()
print(Fore.RED + "软件链接 " + Fore.GREEN + " : https://github.com/davenisc")
init()
print(Fore.RED + "描述 " + Fore.GREEN + "：脚本审核页面WORDPRESS")
init()
print(Fore.RED + "联系邮件 " + Fore.GREEN + "  : sysvd@protonmail.com")
init()
print(Fore.RED + "由Shihun汉化，可能有些地方汉化得不到位，请谅解，博客：https://blog.csdn.net/chk218")

# Color de texto inicio ###################################################################

# Color de texto fin    ###################################################################
init()
print(Fore.WHITE + "________________________________________________________________________  ")
print("                                                                                   ")
init()
print(Fore.RED + " ████████╗██████╗ ███████╗██╗  ██╗    ███████╗ ██████╗ █████╗ ███╗   ██╗ ")
init()
print(Fore.RED + " ╚══██╔══╝██╔══██╗██╔════╝╚██╗██╔╝    ██╔════╝██╔════╝██╔══██╗████╗  ██║ ")
init()
print(Fore.RED + "    ██║   ██████╔╝█████╗   ╚███╔╝     ███████╗██║     ███████║██╔██╗ ██║ ")
init()
print(Fore.RED + "    ██║   ██╔══██╗██╔══╝   ██╔██╗     ╚════██║██║     ██╔══██║██║╚██╗██║ ")
init()
print(Fore.RED + "    ██║██╗██║  ██║███████╗██╔╝ ██╗    ███████║╚██████╗██║  ██║██║ ╚████║ ")
init()
print(Fore.RED + "    ╚═╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝ ")
init()
print(Fore.RED + "    ------------------------------------------------------------         ")
init()
print(Fore.RED + "    |   @DaveNISC   |   @Sebastianf94       |  @LuisRamirezMe   |        ")
init()
print(Fore.RED + "    ------------------------------------------------------------         ")
init()
print(Fore.RED + "    | @whitepadawan |    @elcodigok         |                   |        ")
init()
print(Fore.GREEN + "                                                 ____                  ")
init()
print(Fore.GREEN + "     ___                                      .-~    '.                ")
init()
print(Fore.GREEN + "    `-._~-.                                  / /  ~@\   )              ")
init()
print(Fore.GREEN + "         \  \                               | /  \~\.  `\              ")
init()
print(Fore.GREEN + "         ]  |                              /  |  |< ~\(..)             ")
init()
print(Fore.GREEN + "        /   !                        _.--~T   \  \<   .,,              ")
init()
print(Fore.GREEN + "       /   /                 ____.--~ .    _  /~\ \< /                 ")
init()
print(Fore.GREEN + "      /   /             .-~~'        /|   /o\ /-~\ \_|                 ")
init()
print(Fore.GREEN + "     /   /             /     )      |o|  / /|o/_   '--'                ")
init()
print(Fore.GREEN + "    /   /           .-'(     l__   _j \_/ / /\|~    .                  ")
init()
print(Fore.GREEN + "   /    l          /    \       ~~~|    `/ / / \.__/l_                 ")
init()
print(Fore.GREEN + "   |     \     _.-'      ~-\__     l      /_/~-.___.--~                ")
init()
print(Fore.GREEN + "   |      ~---~           /   ~~'---\_    __[o,                        ")
init()
print(Fore.WHITE + "________________________________________________________________________\n")
init()
print(Fore.GREEN + "                            By SySvd  | v 0.1                         \n")

# Color de texto inicio


# Color de texto fin
"""
fin logo
"""
"""
Funci�n que limpia la pantalla y muestra nuevamente el menu
"""


# os.system('clear') # NOTA para windows tienes que cambiar clear por cls

def pedirNumeroEntero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            num = int(input("输入选项："))
            correcto = True
        except ValueError:
            print('输入选项错误')
            print("")

    return num


salir = False
opcion = 0

while not salir:

    init()
    print(Fore.RED + "运行终端" + Fore.GREEN + "      Root")
    init()
    print(Fore.RED + "运行CMD" + Fore.GREEN + "           Administrator \n\n")

    init()
    print(Fore.RED + "1. " + Fore.WHITE + " 搜索漏洞 ")
    init()
    print(Fore.RED + "2. " + Fore.WHITE + " 搜索开放端口  ")
    init()
    print(Fore.RED + "3. " + Fore.WHITE + " 搜索公共电子邮件   ")
    init()
    print(Fore.RED + "4. " + Fore.WHITE + " 显示找到的信息")
    init()
    print(Fore.RED + "5. " + Fore.WHITE + " T.rex_scan的详细信息")
    init()
    print(Fore.RED + "6. " + Fore.WHITE + " 退出")
    print("")
    print("选择一个选项")
    print("")
    opcion = pedirNumeroEntero()

    if opcion == 1:

        ############################################################################################################

        print("")
        init()
        print(Fore.RED + "[*]" + Fore.WHITE + " 用T.rex分析\n\n")
        url_analyze = raw_input('例如，输入要分析的URL: www.mydomain.com\n\n >>> ')
        print("")
        for i in tqdm(range(100)):
            sleep(0.02)
        print("")

        init()
        print(
            Fore.RED + "[*]" + Fore.WHITE + " 该脚本正在运行，此过程可能需要3到10分钟 " + Fore.GREEN + " 在您的互联网速度和发现的信息 " + Fore.WHITE + "T.rex_Scan\n")
        init()
        print(Fore.RED + "[*]" + Fore.WHITE + " 最好在信息收集过程结束时去喝咖啡，当扫描完成后，脚本将返回主菜单。 " + Fore.GREEN + "" + Fore.WHITE + "")
        print("")
        init()
        print(Fore.RED + "   ( ( " + Fore.WHITE + "")
        init()
        print(Fore.RED + "    ) ) " + Fore.WHITE + "")
        init()
        print(Fore.RED + "  ........" + Fore.WHITE + "")
        init()
        print(Fore.RED + "  |      |]" + Fore.WHITE + "  go!! ")
        init()
        print(Fore.RED + "  \      / " + Fore.WHITE + "  and have   ")
        init()
        print(Fore.RED + "   `----'" + Fore.WHITE + "    a coffee   ")
        print("")

        # os.system("gnome-terminal -e 'ping 8.8.8.8'")
        # command = '  nslookup ' + url_analyze +  ' > scan_ip.txt '

        # os.system(command)

        command = '  whatweb -v  ' + url_analyze + ' > scan_version.txt --color never'

        os.system(command)

        command = '  wpscan --url ' + url_analyze + ' --enumerate p > scan_page.txt --batch --no-color --no-banner'

        os.system(command)

        for i in tqdm(range(100)):
            sleep(0.02)
        print("")

        init()
        print(Fore.RED + "[*]" + Fore.GREEN + " Finished analysis }:) \n\n")
        print("")
        time.sleep(5)
        os.system('clear')

    elif opcion == 2:

        ############################################################################################################

        print("")
        init()
        print(Fore.RED + "[*]" + Fore.WHITE + " Analyze with T.rex\n\n")
        ports_analyze = raw_input('例如，输入要分析的URL: www.mydomain.com\n\n >>> ')
        print("")
        for i in tqdm(range(100)):
            sleep(0.02)
        print("")
        init()
        print(Fore.RED + "[*]" + Fore.WHITE + " Starting" + Fore.GREEN + " 端口分析" + Fore.WHITE + "，这可能需要几分钟，请稍候\n")
        print("")
        init()
        print(Fore.GREEN + " ¯\_(ツ)_/¯ " + Fore.WHITE + " 当T.rex_scan扫描端口时，请访问网站www.codeweb.top ")
        print("")

        command = 'nmap -O -sS ' + ports_analyze + ' > scan_ports.txt'

        os.system(command)

        for i in tqdm(range(100)):
            sleep(0.02)
        print("")

        init()
        print(Fore.RED + "[*]" + Fore.GREEN + " Finished analysis }:) \n\n")
        print("")
        time.sleep(5)
        os.system('clear')

    elif opcion == 3:

        ############################################################################################################

        print("")
        init()
        print(Fore.RED + "[*]" + Fore.WHITE + " 用T.rex分析\n\n")
        url_analyze_mail = raw_input('输入要分析的电子邮件域名，例如：mydomain.com\n\n >>> ')
        print("")
        for i in tqdm(range(100)):
            sleep(0.02)
        print("")
        init()
        print(Fore.RED + "[*]" + Fore.WHITE + " 开始" + Fore.GREEN + " 邮件搜索" + Fore.WHITE + ", 这可能需要几分钟，请稍候\n")
        print("")
        init()
        print(Fore.GREEN + " ¯\_(ツ)_/¯ " + Fore.WHITE + " 请记住，公司电子邮件对公司来说是一个很大的安全漏洞 ")
        print("")

        command = 'theharvester -d ' + url_analyze_mail + ' -l 500 -b all > scan_mails.txt '
        os.system(command)

        for i in tqdm(range(100)):
            sleep(0.02)
        print("")

        init()
        print(Fore.RED + "[*]" + Fore.GREEN + " 分析完成 }:) \n\n")
        print("")
        time.sleep(5)
        os.system('clear')

        #########################################################################################
    elif opcion == 4:

        print("")

        init()
        print(Fore.WHITE + "________________________________________________________________________\n")

        print(Fore.RED + "[*]" + Fore.WHITE + " 发现了漏洞 (CVE)\n")

        imp_cve = open('scan_page.txt', 'r')

        # [for].[0-9]+.[0-9]+.[0-9]+.[0-9]+ IP del server
        # [0-9].+[a-z]\s*[a-z]+\s\s[a-z]+ puerto

        regex = '[CVE]+-[0-9]+-[0-9]+'

        list_cve = []

        for line2 in imp_cve:
            line2 = line2.rstrip()
            y = re.findall('[CVE]+-[0-9]+-[0-9]+', line2)
            if len(y) > 0:
                if y[0] not in list_cve:
                    list_cve.append(y[0])
                    print(y[0])
        init()
        print(Fore.WHITE + "________________________________________________________________________\n")
        time.sleep(3)
        print("")
        ########################################################################################

        init()
        print(Fore.WHITE + "________________________________________________________________________\n")

        print(Fore.RED + "[*]" + Fore.WHITE + " Ports found (**)\n")

        imp_ports = open('scan_ports.txt', 'r')

        regex = '[0-9]+/[\w.]+\s*[\w.]+\s*[\w.]+.[\w.]+'

        list_port = []

        for line2 in imp_ports:
            line2 = line2.rstrip()
            x = re.findall('[0-9]+/[\w.]+\s*[\w.]+\s*[\w.]+.[\w.]+', line2)
            if len(x) > 0:
                if x[0] not in list_port:
                    list_port.append(x[0])
                    print(x[0])
        init()
        print(Fore.WHITE + "________________________________________________________________________\n")
        time.sleep(3)
        print("")

        #########################################################################################

        ########################################################################################

        init()
        print(Fore.WHITE + "________________________________________________________________________\n")

        print(Fore.RED + "[*]" + Fore.WHITE + " 查询页面 (**)\n")

        imp_page = open('scan_page.txt', 'r')

        regex2 = '[A-Za-z]+:+//[a-z]+.[a-z]+.[a-z]+.[a-z]+'

        list_pages = []

        for line3 in imp_page:
            line3 = line3.rstrip()
            z = re.findall('[A-Za-z]+:+//[a-z]+.[a-z]+.[a-z]+.[a-z]+[A-Za-z]+', line3)

            if len(z) > 0:
                if z[0] not in list_pages:
                    list_pages.append(z[0])
                    print(z[0])
        init()
        print(Fore.WHITE + "________________________________________________________________________\n")
        time.sleep(3)
        print("")

        #########################################################################################

        ########################################################################################

        init()
        print(Fore.WHITE + "________________________________________________________________________\n")

        print(Fore.RED + "[*]" + Fore.WHITE + " 该网站容易受到攻击 (**)\n")

        imp_vulnerab = open('scan_page.txt', 'r')

        # regex2 = '.*?<= [0-9]+.[0-9]+.(\w+).*'
        list_vulnerab = []

        for line4 in imp_vulnerab:
            line4 = line4.rstrip()
            a = re.findall('-\s[A-Z].*', line4)
            if len(a) > 0:
                if a[0] not in list_vulnerab:
                    list_vulnerab.append(a[0])
                    print(a[0])

        init()
        print(Fore.WHITE + "________________________________________________________________________\n")
        time.sleep(3)
        print("")

        ###############################################################################################

        init()
        print(Fore.WHITE + "________________________________________________________________________\n")

        print(Fore.RED + "[*]" + Fore.WHITE + " 发现邮件 (**)\n")
        mail_search = open('scan_mails.txt', 'r')

        # [\w.]+.[0-9]+.[\w.]+.\n
        # regex2 = '.*?<= [0-9]+.[0-9]+.(\w+).*'
        list_mail = []

        for line5 in mail_search:
            line5 = line5.rstrip()
            a = re.findall('[\w+]+@[\w+]+.[\w+]+.[\w+]+', line5)
            if len(a) > 0:
                if a[0] not in list_mail:
                    list_mail.append(a[0])
                    print(a[0])

        init()
        print(Fore.WHITE + "________________________________________________________________________\n")
        time.sleep(3)
        print("")

        ###############################################################################################

        init()
        print(Fore.WHITE + "________________________________________________________________________\n")

        print(Fore.RED + "[*]" + Fore.WHITE + " CMS (**)\n")

        vers_search = open('scan_page.txt', 'r')
        # [\w.]+.[0-9]+.[\w.]+.\n
        # regex2 = '.*?<= [0-9]+.[0-9]+.(\w+).*'
        list_vers = []

        for line6 in vers_search:
            line6 = line6.rstrip()
            p = re.findall('.[+].\s[\w.]+\s[\w]+\s[0-9]+.[0-9]+.[0-9]', line6)
            if len(p) > 0:
                if p[0] not in list_vers:
                    list_vers.append(p[0])
                    # print (p[0])
                    init()
                    print(Fore.WHITE + (p[0]))

        init()
        print(Fore.WHITE + "________________________________________________________________________\n")
        time.sleep(3)
        print("")

        ###############################################################################################

        init()
        print(Fore.WHITE + "________________________________________________________________________\n")

        print(Fore.RED + "[*]" + Fore.WHITE + " 地址 (**)\n")

        ip_s = open('scan_version.txt', 'r')
        # [\w.]+.[0-9]+.[\w.]+.\n
        # regex2 = '.*?<= [0-9]+.[0-9]+.(\w+).*'
        #:\s[0-9]+.[0-9]+.[0-9]+.[0-9]+\s
        ip_d = []

        for line7 in ip_s:
            line7 = line7.rstrip()
            q = re.findall('[IP]+..........[0-9]+.[0-9]+.[0-9]+.[0-9]+.', line7)
            if len(q) > 0:
                if q[0] not in ip_d:
                    ip_d.append(q[0])
                    # print (p[0])
                    init()
                    print(Fore.WHITE + (q[0]))

        init()
        print(Fore.WHITE + "________________________________________________________________________\n")
        time.sleep(3)
        print("")

        ###############################################################################################

        init()
        print(Fore.WHITE + "________________________________________________________________________\n")

        print(Fore.RED + "[*]" + Fore.WHITE + " Location (**)\n")

        location_g = open('scan_version.txt', 'r')
        # [\w.]+.[0-9]+.[\w.]+.\n
        # regex2 = '.*?<= [0-9]+.[0-9]+.(\w+).*'
        #:\s[0-9]+.[0-9]+.[0-9]+.[0-9]+\s
        local_d = []

        for line8 in location_g:
            line8 = line8.rstrip()
            f = re.findall('[\w]+\s\s\s.\s[A-Z]+\s[A-Z]+', line8)
            if len(f) > 0:
                if f[0] not in local_d:
                    local_d.append(f[0])
                    # print (p[0])
                    init()
                    print(Fore.WHITE + (f[0]))

        init()
        print(Fore.WHITE + "________________________________________________________________________\n")
        time.sleep(3)
        print("")
    elif opcion == 5:
        print("")
        init()
        print(Fore.RED + "[*]" + Fore.WHITE + "    您好，欢迎来到 " + Fore.GREEN + "T.rex_scan (**)\n")
        init()
        print(Fore.CYAN + "[+]" + Fore.WHITE + "   使用此脚本，您可以优化效率，减少审核页面的时间 ")
        init()
        print(Fore.CYAN + "[+]" + Fore.WHITE + "   因为T.rex_scan可以执行您指定的任务并过滤结果。  ")
        init()
        print(Fore.CYAN + "[+]" + Fore.WHITE + "   当我们必须审核网页时，我们必须打开许多控制台，这个想法就诞生了")
        init()
        print(Fore.CYAN + "[+]" + Fore.WHITE + "   要运行许多工具，除此之外我们还要逐一分析日志 ")
        init()
        print(Fore.CYAN + "[+]" + Fore.WHITE + "   拿出我们需要的信息，T.rex扫描是瑞士军刀 ")
        init()
        print(Fore.CYAN + "[+]" + Fore.WHITE + "   日常使用的工具并过滤结果。\n")
        init()
        print(Fore.GREEN + "[!]" + Fore.WHITE + "  显示审核页面的漏洞")
        init()
        print(Fore.GREEN + "[!]" + Fore.WHITE + "  启动端口扫描")
        init()
        print(Fore.GREEN + "[!]" + Fore.WHITE + "  显示与页面关联的CVE")
        init()
        print(Fore.GREEN + "[!]" + Fore.WHITE + "  搜索与网站关联的电子邮件")
        init()
        print(Fore.GREEN + "[!]" + Fore.WHITE + "  它显示IP地址和托管服务器位置\n")
        init()
        print(Fore.RED + "[!]" + Fore.WHITE + "  此脚本使用并依赖于以下工具进行操作 " + Fore.GREEN + ":\n")
        init()
        print(Fore.CYAN + "[1]" + Fore.WHITE + "       WPScan V 2.9.3")
        init()
        print(Fore.CYAN + "[2]" + Fore.WHITE + "       Nmap V 7.60")
        init()
        print(Fore.CYAN + "[3]" + Fore.WHITE + "       Theharvester V 2.7")
        init()
        print(Fore.CYAN + "[4]" + Fore.WHITE + "       WhatWeb V 0.4.9\n")
        init()
        print(Fore.CYAN + "[+]" + Fore.WHITE + "   以同样的方式，T.rex_scan使用正则表达式来过滤 ")
        init()
        print(Fore.CYAN + "[+]" + Fore.WHITE + "   我们需要的数据，使用库（os，time，re，time，color，tqdm和sleep）\n")
        init()
        print(Fore.CYAN + "[+]" + Fore.WHITE + "   重要的是要记住，如果你打算使用Kali linux  ")
        init()
        print(Fore.CYAN + "[+]" + Fore.WHITE + "   你应该只安装tqdm库，但是如果你打算使用Windows")
        init()
        print(Fore.CYAN + "[+]" + Fore.WHITE + "   必须使用pip install选项安装所有库 \n\n")



    elif opcion == 6:
        salir = True
    else:
        print("输入1到5之间的数字")
print("")
print("********完成的脚本***********")
print("")

# comandos error

"""ping 
 apt-cache show nmap
 apt-cache search nmap
 sudo apt-get install python-nmap
 sudo apt-get install python3-nmap
"""

# paginas de consulta
# https://recursospython.com/guias-y-manuales/colorama-texto-fondo-coloreados-la-consola/
# http://www.poketcode.com/es/python/archivos_csv/index.html
# http://python-para-impacientes.blogspot.com/2014/02/ejecutar-un-comando-externo.html


#######################################################################################
# Fuentes
# https://www.solvetic.com/tutoriales/article/3871-como-guardar-resultado-comando-en-archivo-texto-linux/
# https://caminosdigitales.es/ejecutar-systeminfo-y-guardar-en-archivo-con-python/
# https://lapertenencia.wordpress.com/2014/08/16/python-guardando-resultado-comandos-linux-en-una-variable/
