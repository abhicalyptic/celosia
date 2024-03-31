import requests
for line in open("/Users/ASUS/Desktop/projects/celosia/sources/wallhaven/sources.txt","r").readlines():
    response=requests.get(line)
    if response.status_code != 200:
        print(line)
