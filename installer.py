import os
import shutil
import sys
import win32com.client

# Nome da pasta onde o sistema será instalado
INSTALL_DIR = r"C:\RelatorioFirebird"

# Caminho da área de trabalho do usuário
DESKTOP = os.path.join(os.path.expanduser("~"), "Desktop")

# Arquivos que devem ser copiados para a pasta do sistema
FILES_TO_COPY = [
    "dist\\app.exe",     # o executável gerado pelo PyInstaller
    "query.sql",
    "connection.txt",
    "icone.ico"          # opcional
]

def criar_pasta_instalacao():
    if not os.path.exists(INSTALL_DIR):
        os.makedirs(INSTALL_DIR)
        print(f"Pasta criada em: {INSTALL_DIR}")
    else:
        print(f"Pasta já existe: {INSTALL_DIR}")

def copiar_arquivos():
    for file in FILES_TO_COPY:
        if os.path.exists(file):
            destino = os.path.join(INSTALL_DIR, os.path.basename(file))
            shutil.copy(file, destino)
            print(f"Copiado: {file} → {destino}")
        else:
            print(f"Arquivo não encontrado: {file}")

def criar_atalho():
    caminho_exe = os.path.join(INSTALL_DIR, "app.exe")
    caminho_atalho = os.path.join(DESKTOP, "Relatório Firebird.lnk")

    shell = win32com.client.Dispatch("WScript.Shell")
    atalho = shell.CreateShortCut(caminho_atalho)
    atalho.TargetPath = caminho_exe
    atalho.WorkingDirectory = INSTALL_DIR
    atalho.IconLocation = os.path.join(INSTALL_DIR, "icone.ico")
    atalho.save()

    print(f"Atalho criado na área de trabalho: {caminho_atalho}")

def main():
    criar_pasta_instalacao()
    copiar_arquivos()
    criar_atalho()
    print("✅ Instalação concluída!")

if __name__ == "__main__":
    main()
