import base64
import logging
import re

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import pytesseract
from PIL import Image


digit_pattern = re.compile(r'\d+')


def rsa_encrypt(public_key, src):
    public_key = '-----BEGIN PUBLIC KEY-----\n' + public_key + '\n-----END PUBLIC KEY-----'
    rsa_key = RSA.importKey(public_key)
    cipher = PKCS1_v1_5.new(rsa_key)
    return str(base64.b64encode(cipher.encrypt(src.encode('utf-8'))), 'utf-8')


def clear_image(image):
    image = image.convert('RGB')
    width = image.size[0]
    height = image.size[1]

    for x in range(width):
        for y in range(height):
            rgb = image.getpixel((x, y))
            if rgb[0] >= 140 and rgb[1] >= 140 and rgb[2] >= 140:
                image.putpixel((x, y), (0, 0, 0))
            else:
                image.putpixel((x, y), (255, 255, 255))
    return image


def get_code(img_path):
    image = Image.open(img_path)
    image = clear_image(image)
    code = pytesseract.image_to_string(image, lang='eng', config='--psm 13 --oem 3 -c tessedit_char_whitelist=0123456789')
    digit_list = digit_pattern.findall(code)
    return ''.join(digit_list)

def init_logger():
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(format="[%(levelname)s]:%(message)s")
