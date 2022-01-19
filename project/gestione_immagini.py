import glob
import os
import io
import PIL
from numpy.matlib import rand


# Converte le immagini scaricate in binario dal database(filename) nel formato originario
def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData


# Converte le immagini in formato binario per caricamento su database
def convertToImageData(data, filename):
    # Convert binary data to proper format and write it on Hard disk
    with open(filename, 'wb') as file:
        file.write(data)
    return file


# Cancella Immagini
def delete_image():
    # Cancella immagini in downloads
    files = glob.glob('project/static/downloads/images/*')
    for f in files:
        os.remove(f)
    # Cancella immagini in uploads
    files = glob.glob('project/static/uploads/images/*')
    for f in files:
        os.remove(f)


# Scarica per ogni annuncio la propria immagine assegnado il percorso alla variabile istanza "immagine_caricata"
def download_image_annunci(annuncio, i):
    # Decode the string
    # binary_data = base64.b64decode(annuncio.immagine)
    # Convert the bytes into a PIL image
    immagineTemp = PIL.Image.open(io.BytesIO(annuncio.immagine))
    # Salvo la directory
    index_image_rng = rand(5)
    j = i + index_image_rng
    filename = 'image' + str(i) + str(j)
    dirFile = 'project/static/downloads/images/' + filename + '.' + immagineTemp.format
    annuncio.immagine_caricata = convertToImageData(annuncio.immagine, dirFile).name
    percorso_modificato = annuncio.immagine_caricata.replace("project", "")
    annuncio.immagine_caricata = '' + percorso_modificato
