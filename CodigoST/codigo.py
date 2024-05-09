# -*- coding: utf-8 -*-
import os
import zipfile

def descomprimir_archivo(archivo_zip):
    # Obtener la carpeta donde se encuentra el archivo zip
    carpeta_destino = os.path.dirname(archivo_zip)
    
    # Descomprimir el archivo zip en la misma carpeta
    with zipfile.ZipFile(archivo_zip, 'r') as zip_ref:
        zip_ref.extractall(carpeta_destino)
    
    # Eliminar el archivo zip después de descomprimirlo
    os.remove(archivo_zip)

if __name__ == "__main__":
    archivo_zip = "/Users/leonardoreyes/Documents/archivoST/archivo.txt.zip"
    
    descomprimir_archivo(archivo_zip)