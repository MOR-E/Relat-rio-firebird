; installer.iss - Exemplo para Relatório Firebird
[Setup]
AppName=Relatório Firebird
AppVersion=1.0
; Instala diretamente na raiz do disco do sistema (C:\RelatorioFirebird)
DefaultDirName={sd}\RelatorioFirebird
DefaultGroupName=RelatorioFirebird
OutputDir=.
OutputBaseFilename=Instalador_RelatorioFirebird
SetupIconFile=icone.ico
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin
; Mostra o programa após instalação (opcional)
UninstallDisplayIcon={app}\app.exe

[Languages]
; Você pode selecionar idiomas no wizard; deixe como padrão se não tiver arquivo adicional

[Files]
; Copia o executável principal e demais arquivos (use caminhos relativos ao .iss)
Source: "dist\app.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "query.sql"; DestDir: "{app}"; Flags: ignoreversion
Source: "connection.txt"; DestDir: "{app}"; Flags: ignoreversion
Source: "icone.ico"; DestDir: "{app}"; Flags: ignoreversion
; Se tiver dependências como fbclient.dll (opcional), inclua:
; Source: "lib\fbclient.dll"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{userdesktop}\Relatório Firebird"; Filename: "{app}\app.exe"; IconFilename: "{app}\icone.ico"
Name: "{commonprograms}\Relatório Firebird"; Filename: "{app}\app.exe"; IconFilename: "{app}\icone.ico"

[Run]
; Executa o app após a instalação terminar (opcional). Use Flags: nowait postinstall skipifsilent
Filename: "{app}\app.exe"; Description: "Abrir Relatório Firebird"; Flags: nowait postinstall skipifsilent

[UninstallDelete]
Type: files; Name: "{app}\connection.txt"
Type: files; Name: "{app}\query.sql"
; (Outras entradas se quiser remover arquivos específicos no uninstall)
