import io
from random import random

import PIL
from numpy.matlib import rand


def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


def convertToImageData(data, filename):
    # Convert binary data to proper format and write it on Hard disk
    with open(filename, 'wb') as file:
        file.write(data)
    return file


def download_image_annunci(annuncio, i):
    # Decode the string
    # binary_data = base64.b64decode(annuncio.immagine)
    # Convert the bytes into a PIL image
    immagineTemp = PIL.Image.open(io.BytesIO(annuncio.immagine))
    # Salvo la directory
    index_image_rng = rand(2000)
    j = i + index_image_rng
    filename = 'image' + str(i)+str(j)
    dirFile = 'project/static/downloads/images/' + filename + '.' + immagineTemp.format
    annuncio.immagine_caricata = convertToImageData(annuncio.immagine, dirFile).name
    percorso_modificato = annuncio.immagine_caricata.replace("project", "")
    annuncio.immagine_caricata = '' + percorso_modificato