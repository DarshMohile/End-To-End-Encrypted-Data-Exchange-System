from pathlib import Path
from PIL import Image

def reduce_depth(img:Path) -> Path:

    quantised = Path("./data/source/cat_reduced.bmp")

    img = Image.open(img).convert("RGB")

    # Reduce each channel to only 4 levels
    img = img.quantize(colors=16).convert("RGB")

    img.save(quantised, format="BMP")

    return quantised