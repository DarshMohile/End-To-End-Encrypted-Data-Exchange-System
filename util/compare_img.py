from pathlib import Path
from PIL import Image
import matplotlib.pyplot as plt

def compare_imgs(src_img_path:Path, ecb_img_path:Path, cbc_img_path:Path) -> None:

    original = Image.open(src_img_path)
    ecb = Image.open(ecb_img_path)
    cbc = Image.open(cbc_img_path)

    fig, axes = plt.subplots(1, 3, figsize=(18, 7))

    axes[0].imshow(original, interpolation="nearest")
    axes[0].set_title("Original")

    axes[1].imshow(ecb, interpolation="nearest")
    axes[1].set_title("AES-ECB")

    axes[2].imshow(cbc, interpolation="nearest")
    axes[2].set_title("AES-CBC")

    for ax in axes:
        ax.axis("off")

    plt.tight_layout()
    plt.savefig(
        "./data/encrypted/ecb_cbc_comparison.png",
        dpi=200
    )

    plt.show()
