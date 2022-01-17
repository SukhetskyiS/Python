import re
import requests

my_tuple = ()
my_list = []
with open('nginx_logs.txt', 'w+') as f:
    f.write(requests.get(
        'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs').text)
    f.seek(0)
    for line in f:
        remote_addr = str(re.compile(r"(?:\d+\.){3}\d+\s").findall(line))[2:-3]
        request_datetime = str(re.compile(r"\[[\S\s]*\]").findall(line))[3:-3]
        request_type = str(re.compile(r"GET").findall(line))[2:-2]
        requested_resource = str(re.compile(r"\/downloads/product_\d").findall(line))[2:-2]
        response_code = str(re.compile(r"\s\d+\s").findall(line))[3:-3]
        response_size = str(re.compile(r"\s\d+\s\"").findall(line))[3:-4]
        my_tuple = (remote_addr, request_datetime, request_type, requested_resource, response_code, response_size)
        my_list.append(my_tuple)
print(*my_list, sep='\n')
