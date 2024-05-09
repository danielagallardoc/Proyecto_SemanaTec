import zipfile
import os
from tkinter import Tk, filedialog, simpledialog

def get_folder_path():
    root = Tk()
    root.withdraw()  
    folder_selected = filedialog.askdirectory() 
    root.destroy()  
    return folder_selected

def compress_file(file_path, password):
    zip_path = f"{file_path}.zip"
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.setpassword(password.encode())  
        zipf.write(file_path, os.path.basename(file_path))
    os.remove(file_path) 

def main():
    folder_path = get_folder_path()
    if folder_path:
        password = simpledialog.askstring("Password", "Introduce una clave para el archivo ZIP:", show='*')
        if password:  
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path): 
                    compress_file(file_path, password)
                    print(f"Archivo comprimido y eliminado: {file_path}.zip")
        else:
            print("No se ha introducido una contraseña.")
    else:
        print("No se seleccionó carpeta.")

if __name__ == "__main__":
    main()







