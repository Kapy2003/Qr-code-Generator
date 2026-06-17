from pyqrcode import create
from pathlib import Path
import png
import os


path = Path("./qr-generated/")
path.mkdir(parents=True, exist_ok=True)

name = input("Enter a Name for the QR-Image: ")

if not name.endswith (".png"):
    name = Path(name).stem + ".png"

url = create("this is a test")
url.png(path/str(name),scale=40)

