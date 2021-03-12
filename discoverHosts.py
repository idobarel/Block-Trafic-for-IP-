def getIPs():
    x = os.popen('nmap -sn 192.168.68.0/24').read()
    return x
