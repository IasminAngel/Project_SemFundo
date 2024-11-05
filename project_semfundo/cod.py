from rembg import remove
from PIL import Image

url = Image.open('Espectro.jpg')
output = remove(url)
output.save('img2.png')