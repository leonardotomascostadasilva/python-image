from PIL import Image
import pytesseract
import os


caminho_imagem = os.path.abspath('images/test.png')

imagem = Image.open(caminho_imagem)

texto = pytesseract.image_to_string(imagem, lang='por')

print(texto)
