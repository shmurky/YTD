import os
import winshell
from win32com.client import Dispatch

def create_shortcut():
    desktop = winshell.desktop()
    path = os.path.join(desktop, "youtube_downloader.lnk")
    target = r"ścieżka/do/youtube_downloader.exe"  # Zmień na właściwą ścieżkę do twojego pliku wykonywalnego youtube_downloader.exe
    wDir = r"ścieżka/do/"  # Zmień na katalog zawierający plik wykonywalny
    icon = r"ścieżka/do/ikonki.ico"  # Opcjonalnie: ścieżka do ikony, którą chcesz użyć dla skrótu

    shell = Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(path)
    shortcut.Targetpath = target
    shortcut.WorkingDirectory = wDir
    shortcut.IconLocation = icon
    shortcut.save()

if __name__ == "__main__":
    create_shortcut()
