import requests
import json
import datetime
import time

d = datetime.timedelta(0,180,0)

def media(list_value):
    total = 0
    for i in list_value:
        total = total + int(i)
    return total/len(list_value)

url_device = "http://network_device:5000/service/status"
url_bbdd = "http://database:8086/write"
database_name = "monitoring"
auth_data = {'user': 'username', 'password': 'pass'}

while True:
    ti = datetime.datetime.now()
    resp = requests.get(url_device, data=auth_data)
    if resp.status_code == '200':
        j = json.loads(resp.text)
        aggregated_data = media(j['data'])
        payload = {'database': database_name,'data': aggregated_data}
        try:
            r = requests.post(url_bbdd, json=payload)
        except:
            print(f"Failed to write in {databasename}")
    else:
    print("Failed to connect with the network device")
    te = datetime.datetime.now()
    dt = te - ti
    if dt.seconds < d.seconds:
        time.sleep(float(d.seconds - dt.seconds))