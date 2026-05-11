"""
Visualizador Direccional de Pozo - Launcher
============================================
Requiere:  pip install pywebview pyinstaller
Para generar el .exe ejecutar build_exe.bat
"""
import webview
import os
import sys


def resource_path(filename):
    """Resuelve la ruta tanto en modo dev como desde el .exe de PyInstaller."""
    if getattr(sys, 'frozen', False):
        # Corriendo desde el .exe generado por PyInstaller
        base = sys._MEIPASS
    else:
        # Corriendo directamente con python launcher.py
        base = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base, filename)


if __name__ == '__main__':
    html_file = resource_path('visualizador_pozo.html')
    window = webview.create_window(
        title='Visualizador Direccional de Pozo v1.0',
        url='file:///' + html_file.replace('\\', '/'),
        width=1280,
        height=860,
        resizable=True,
        min_size=(900, 600),
    )
    webview.start()
