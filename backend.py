from pyqrcode import create
from pathlib import Path
import png
import os

def generate_qr(name, entry):
    path = Path("./qr-generated/")
    path.mkdir(parents=True, exist_ok=True)

    if not name.endswith(".png"):
        name = Path(name).stem + ".png"

    url = create(str(entry))
    
    final_destination = path / name
    url.png(str(final_destination), scale=40)
