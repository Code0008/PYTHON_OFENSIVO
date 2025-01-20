import requests
import re
import sys
import datetime
from pwn import *

def validar_target(target_usuario):

    if re.match(r"""[\w\-]+(\.[\w\-]+)+[/#?]?.*$""", target_usuario ) != None:
        try:
            soliciutd_exitencia = requests.request('GET', "https://"+target_usuario, timeout=1)
        except requests.exceptions.ConnectionError as conerr:
            print(f"""
                [!] no existe el dominio
                """)
            sys.exit(1)
        if soliciutd_exitencia.status_code==200:
            return True
    print(f"""
        /////////////////////
        Objetivo invalido.
        {target_usuario}
          """)
    sys.exit(1)
    


def impresion_dominio(subdominios_obtenidos, **argumentos_extra):
    #respuestas = {}
    #  URL | ESTADO | HORA_ESCANEO
    soliciutd_progres = log.progress("ESCANEANDO")
    respuesta_progreeso = log.progress("CODIGO: ")
    existe_salida= False
    if argumentos_extra["salida"]:
        existe_salida = True
        datos= {}

    def validar(url, datos):
        url  = "https://" + url
        try:
            solicitud = requests.request('GET', url, timeout=2)
            soliciutd_progres.status(url)

            if solicitud.status_code == 200 or solicitud.status_code == 302:
                respuesta_progreeso.status(solicitud.status_code)
                fecha = datetime.datetime.now()
                if existe_salida:
                    datos[url] = [200,fecha.strftime("%m/%d/%Y, %H:%M:%S") ]                
                #respuestas[url] = True
        except Exception as e:
            soliciutd_progres.status(f"Ocurrio un error inesperado")
            if existe_salida:
                fecha = datetime.datetime.now().date()
                datos[url] = ['No respuesta',fecha.strftime("%m/%d/%Y, %H:%M:%S")]

    hilos = []
    for url in subdominios_obtenidos:
        threard = threading.Thread(target=validar,args=(url,datos if existe_salida else None))
        hilos.append(threard)
        threard.start()
        threard.join()
    if existe_salida:
        return datos