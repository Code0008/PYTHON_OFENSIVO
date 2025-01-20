import requests
import json
from argparse import ArgumentParser
from exportador_datos import exportar_datos
from funciones_internet import validar_target, impresion_dominio
subdominos_obtenidos = {}


    
def arguments():
    lector_argumentos = ArgumentParser(description="Enumerador de subdominios bien pendejo")
    lector_argumentos.add_help
    lector_argumentos.add_argument("-t", "--target", required=True, dest="target", help="Dominio a enumerar yiii")
    lector_argumentos.add_argument("-O", "--output", dest="formato_salida", help="Ocupas almacenas los datos de tu escaneo")
    lector_argumentos.add_argument("-sI", "--shodan-info", dest="shod_api", help="Quieres ver informaciond de shodan")
    args = lector_argumentos.parse_args()
    return args.target, args.formato_salida


def solicitar_informacion(url):
    solicitud = requests.request('GET', f"https://crt.sh/json?q={url}")
    carga_json= json.loads(solicitud.text)
    for subdomino_metadata in carga_json:
        if subdomino_metadata["common_name"] not in subdominos_obtenidos:
            subdominos_obtenidos[subdomino_metadata["common_name"]] = []
            
def main():
    target, salida = arguments()
    if validar_target(target):
        solicitar_informacion( target)
        data_export = impresion_dominio(subdominos_obtenidos, salida= True if salida else None)     
        if salida:
            exportar_datos(data_export, salida)

if __name__ == '__main__':
    main()



