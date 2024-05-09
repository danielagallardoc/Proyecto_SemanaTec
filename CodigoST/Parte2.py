import zipfile
import os
from tkinter import Tk, filedialog, simpledialog

def get_folder_path():
    """ Abrir un diálogo para seleccionar una carpeta que contiene los archivos ZIP. """
    root = Tk()
    root.withdraw()  # Ocultar la ventana principal de Tkinter
    folder_selected = filedialog.askdirectory()  # Abrir el diálogo para elegir carpeta
    root.destroy()  # Cerrar la ventana de Tkinter
    return folder_selected

def unzip_file(zip_path, password):
    """ Descomprimir un archivo ZIP usando una contraseña y luego eliminar el archivo ZIP. """
    # Extraer el nombre del archivo sin la extensión '.zip'
    output_folder = os.path.splitext(zip_path)[0]
    os.makedirs(output_folder, exist_ok=True)  # Crear la carpeta si no existe
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        # Intentar abrir el archivo con la contraseña dada
        try:
            zipf.extractall(path=output_folder, pwd=password.encode())
            print(f"Archivo descomprimido exitosamente en: {output_folder}")
            os.remove(zip_path)  # Eliminar el archivo ZIP después de descomprimir
            print(f"Archivo ZIP eliminado: {zip_path}")
        except RuntimeError as e:
            print(f"No se pudo descomprimir {zip_path}: {e}")
        except Exception as e:
            print(f"Error al eliminar el archivo ZIP {zip_path}: {e}")

def main():
    folder_path = get_folder_path()
    if folder_path:
        password = simpledialog.askstring("Password", "Introduce la clave para descomprimir los archivos ZIP:", show='*')
        if password:
            for filename in os.listdir(folder_path):
                if filename.endswith('.zip'):
                    zip_path = os.path.join(folder_path, filename)
                    unzip_file(zip_path, password)
        else:
            print("No se ha introducido una contraseña.")
    else:
        print("No se seleccionó carpeta.")

if __name__ == "__main__":
    main()
