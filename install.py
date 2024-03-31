import ctypes
import os
SPI_SETDESKWALLPAPER = 20 
directory=os.getcwd()
image="celosia\sample.png"
directory=directory+"/"+image
print(directory)
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,directory, 3) 
