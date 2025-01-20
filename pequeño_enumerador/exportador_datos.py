import pandas as pd

def exportar_datos(datos, salida_name):
    dataframe =  pd.DataFrame.from_dict(datos,
                                         orient='index',                                          
                                        )
    dataframe.reset_index(inplace=True)
    dataframe.columns = ["URL", "CODIGO_ESTADO", "FECHA_ESCANEO"]
    dataframe.to_csv(salida_name)




