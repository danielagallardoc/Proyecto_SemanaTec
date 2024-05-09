import os
import zipfile
import pyminizip

def compress_files_with_password(folder_path, zip_path, password):
    # Comprimir los archivos de la carpeta en un archivo ZIP temporal
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path):
                zipf.write(file_path, file_name)

    # Agregar contraseña al archivo ZIP
    pyminizip.compress(zip_path, None, zip_path + ".zip", password, 0)

    # Eliminar el archivo ZIP temporal
    os.remove(zip_path)

# Ruta de la carpeta que contiene los archivos que quieres comprimir
folder_path = '/Users/leonardoreyes/Documents/archivoST'

# Ruta donde quieres guardar el archivo ZIP resultante
zip_path = '/Users/leonardoreyes/Documents/archivoST'

# Contraseña que quieres agregar al archivo ZIP
password = 'contraseña'

# Comprimir los archivos con contraseña
compress_files_with_password(folder_path, zip_path, password)