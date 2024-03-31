import requests
for line in open("C:\\Users\\abhiy\\Desktop\\gitGithub\\celosia\\sources\\wallhaven\\sources.txt").readlines():
    response=requests.get(line)
    if response.status_code != 200:
        print(line)