from socket import *
from threading import Thread
import argparse
import time
import json
from pathlib import Path

PORT_DICT_PATH = Path(__file__).parent / 'port_dict.json'
with open(PORT_DICT_PATH, 'r') as f:
    port_dict = json.load(f)

def checking_port(host, port_number):
    s = socket(AF_INET, SOCK_STREAM)
    try:
        s.connect((host, int(port_number)))
        service = port_dict.get(str(port_number), 'unknown')
        print(f'{host}/{port} - open - {service}')
    except:
        pass


arguments = argparse.ArgumentParser()
arguments.add_argument('-i', required=True, action='store', dest='ip', help='IP using to scan ports')

values = arguments.parse_args()
print('\nOpen ports:')
start_time = time.time()
for port in range(0, 65536):
    t = Thread(target=checking_port, args=(values.ip, port))
    t.start()
end_time = time.time()
print(f'Port scan completed in {end_time - start_time:.1f} seconds')
