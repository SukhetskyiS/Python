# ДЗ №1
import requests

f = open('nginx_logs.txt', 'w+')
f.write(requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text)
f.seek(0)
my_list = []
my_tuple = ()

for line in f:
    remote_addr = line[:line.find('-') - 1]
    request_type = line[line.find('"') + 1:line.find('"') + 4]
    requested_resource = line[line.find('GET') + 4:line.find('HTTP') - 1]
    my_tuple = (remote_addr, request_type, requested_resource)
    my_list.append(my_tuple)

f.close()
print(*my_list, sep='\n')


# ДЗ №2
from collections import Counter

ip_list = []
with open('nginx_logs.txt') as f:
    for line in f:
        remote_addr = line[:line.find('-') - 1]
        ip_list.append(remote_addr)

for key, val in dict(Counter(ip_list).most_common(1)).items():
    print(f'IP адрес спамера: {key}, количество отправленных им запросов: {val}.')
