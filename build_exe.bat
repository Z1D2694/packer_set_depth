@echo off
echo ============================================
echo  Visualizador Direccional de Pozo - Builder
echo ============================================
echo.

echo [1/3] Instalando dependencias Python...
pip install pywebview pyinstaller
if errorlevel 1 (
    echo ERROR: Fallo la instalacion. Verificar que Python este en el PATH.
    pause & exit /b 1
)

echo.
echo [2/3] Generando ejecutable...
pyinstaller --onefile --windowed ^
  --name "VisualizadorPozo" ^
  --add-data "visualizador_pozo.html;." ^
  launcher.py

if errorlevel 1 (
    echo ERROR: Fallo la compilacion.
    pause & exit /b 1
)

echo.
echo [3/3] Listo!
echo El ejecutable se encuentra en:  dist\VisualizadorPozo.exe
echo Peso aproximado: 25-35 MB (sin instalacion adicional)
echo.
pause
