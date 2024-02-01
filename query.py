import socket
import time

connect = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address =('172.16.16.151' , 45)
connect.setblocking(True)
vendor_command = '{"device":{"identity":{"vendor":null}}}'
#command = '{"audio":{"out":{"mute":true}}}'
rx1_warnings_command = '{"rx1":{"warnings":null}}'
rx1_name_command = '{"rx1":{"name":null}}'
rx2_presets_command = '{"rx2":{"sync_settings":{"led",null}}}}'
rx1_rsqi_command = '{"m":{"rx1":{"rsqi",null}}}}' 
rx2_rsqi_command = '{"m":{"rx2":{"rsqi",null}}}}' 

rx1_af_command = '{"m":{"rx1":{"af",null}}}}' 
rx2_af_command = '{"m":{"rx2":{"af",null}}}}' 

tx1_mute = '{"mates":{"tx1":{"mute",null}}}}'
tx2_mute = '{"mates":{"tx2":{"mute",null}}}}'

txt1_battery_lifetime = '{"mates":{"tx1":{"battery",{"gauge",null}}}}}}'
txt2_battery_lifetime = '{"mates":{"tx2":{"battery",{"gauge",null}}}}}}'

def send_cmd( cmd:str ):
    request_raw = f'{cmd}\r\n'.encode('utf-8')
    connect.sendto( request_raw , server_address)
    time.sleep(1)
    data = connect.recv(128)
    print(data.decode('utf-8'))

send_cmd( txt1_battery_lifetime )
send_cmd( txt2_battery_lifetime )