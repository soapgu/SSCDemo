from zeroconf import ServiceBrowser, ServiceListener, Zeroconf,ServiceInfo
import time
import socket

info:ServiceInfo = None

class MyListener(ServiceListener):

    def update_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} updated")

    def remove_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        print(f"Service {name} removed")

    def add_service(self, zc: Zeroconf, type_: str, name: str) -> None:
        global info
        info = zc.get_service_info(type_, name)
        print(f"Service {name} added, service info: {info}")
        print(f"name:{info.name} addr:{info.parsed_addresses()[0]} and port{info.port}")


zeroconf = Zeroconf()
listener = MyListener()
#browser = ServiceBrowser(zeroconf, "_http._tcp.local.", listener)
browser = ServiceBrowser(zeroconf, "_ssc._udp.local.", listener)
print("begin scan....")
time.sleep(1)

#print(info)
if info is not None:
    print('find device')
    connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address =(info.parsed_addresses()[0] , info.port)
    connect.setblocking(True)
    command = '{"device":{"identity":{"vendor":null}}}'
    #command = '{"audio":{"out":{"mute":true}}}'
    request_raw = f'{command}\r\n'.encode('utf-8')
    connect.sendto( request_raw , server_address)
    time.sleep(1)
    data = connect.recv(128)
    print(data.decode('utf-8'))
else:
    print("can not find device")

try:
    input("Press enter to exit...\n\n")
finally:
    zeroconf.close()