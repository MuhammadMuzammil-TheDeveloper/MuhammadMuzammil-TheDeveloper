"""
Prep a source photo for ASCII conversion.

A flatly-lit face converts to a dark, unreadable blob if you skip this step.
Three fixes:
  1. Remove the background with rembg so only the subject remains.
  2. Boost local contrast with CLAHE (contrast-limited adaptive histogram
     equalization) so a flat face gets real highlights and shadows.
  3. Composite onto pure white so the background maps to the blank end of
     the ASCII ramp (white -> spaces).

Usage:
    python scripts/prep_photo.py source-photo.jpg
Writes scripts/source-prepped.png (grayscale).
"""
import sys
import os

import cv2
import numpy as np
from PIL import Image
from rembg import remove

OUT_NAME = "source-prepped.png"


def main():
    if len(sys.argv) < 2:
        print("Usage: python prep_photo.py <path-to-photo>")
        sys.exit(1)

    src_path = sys.argv[1]
    out_path = os.path.join(os.path.dirname(__file__), OUT_NAME)

    with open(src_path, "rb") as f:
        input_bytes = f.read()

    # 1. Remove background -> RGBA with transparent background
    result_bytes = remove(input_bytes)
    with open("/tmp/_no_bg.png", "wb") as f:
        f.write(result_bytes)

    rgba = Image.open("/tmp/_no_bg.png").convert("RGBA")

    # 3. Composite onto pure white (do this before contrast boost so the
    # matte doesn't get equalized into visible noise at the edges)
    white_bg = Image.new("RGBA", rgba.size, (255, 255, 255, 255))
    composited = Image.alpha_composite(white_bg, rgba).convert("L")

    # 2. CLAHE contrast boost
    arr = np.array(composited)
    clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8, 8))
    boosted = clahe.apply(arr)

    Image.fromarray(boosted).save(out_path)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
