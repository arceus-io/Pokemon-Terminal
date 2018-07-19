import os

from . import WallpaperProvider as _WProv
from ctypes import *

class WindowsProvider(_WProv):
    __SPI_SETDESKWALLPAPER = 20

    def change_wallpaper(path: str):
        windll.user32.SystemParametersInfoW(WindowsProvider.__SPI_SETDESKWALLPAPER, 0, path, 0)

    def is_compatible() -> bool:
        return os.name == 'nt'

    def __str__():
        return "Windows Desktop"
