import urllib.request
from typing import Dict, Tuple

import cv2
import numpy as np
import pytesseract
from Acta import Acta
from static_data import PARTIES

qrCodeDetector = cv2.QRCodeDetector()


def image_from_url(url):
    with urllib.request.urlopen(url) as resp:
        # read image as an numpy array
        image = np.asarray(bytearray(resp.read()), dtype="uint8")

        # use imdecode function
        image = cv2.imdecode(image, cv2.COLOR_BGR2GRAY)
        return image


def replace_symbols(text):
    return text.replace(".", "").replace(" ", "").replace(",", "").strip()


def extract_text_from_image(image) -> Tuple[str, str, str]:
    text = pytesseract.image_to_string(image, lang="spa")
    text = list(filter(lambda a: a not in ["", " ", "   "], text.split("\n")))
    estado = replace_symbols(next(filter(lambda a: "Estado" in a, text)).split("EDO")[-1]) or None
    municipio = (
        replace_symbols(next(filter(lambda a: "Municipio" in a, text)).split("MP")[-1]) or None
    )
    parroquia = (
        replace_symbols(next(filter(lambda a: "Parroquia" in a, text)).split("PQ")[-1]) or None
    )

    return estado, municipio, parroquia


def extract_qr_from_image(image) -> Tuple[str, Dict[str, int]]:
    decoded_text, _, _ = qrCodeDetector.detectAndDecode(image)
    data = decoded_text.split("!")
    acta_id = data[0]
    votes = [int(x) for x in data[1].split(",")]
    total_null = data[2]
    total_invalid = data[3]
    return acta_id, dict(zip(PARTIES, votes)), total_null, total_invalid


if __name__ == "__main__":
    image_path = "actas/017911_139267_0057Acta0057.jpg"
    image_name = image_path.split("/")[-1]
    acta_id, parties_votes, total_null, total_invalid = extract_qr_from_image(image_path)

    state, municipality, parish = extract_text_from_image(image_path)

    acta = Acta(
        acta_id=acta_id,
        image_name=image_name,
        TOTAL_INVALID=total_invalid,
        TOTAL_NULL=total_null,
        STATE=state,
        MUNICIPALITY=municipality,
        PARISH=parish,
        **dict(parties_votes),
    )
    print()
    print(acta.__dict__)
    print()
    print(acta)
