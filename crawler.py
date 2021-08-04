import logging
import json

import requests

from utils import rsa_encrypt, get_code
from settings import settings

session = requests.session()


def study_record():
    resp = session.post(url="https://m.fjcyl.com/studyRecord")
    if resp.json().get('success'):
        logging.info("study success recorded")
    else:
        logging.warning("study record failed")

def login(validate_code):
    data = {
        'userName': rsa_encrypt(settings.PUBLIC_KEY, settings.USERNAME),
        'pwd': rsa_encrypt(settings.PUBLIC_KEY, settings.PASSWORD),
        'validateCode': rsa_encrypt(settings.PUBLIC_KEY, validate_code)
    }

    resp = session.post("https://m.fjcyl.com/mobileNologin", data=data)

    if resp.status_code == requests.codes.ok:
        logging.info('login ' + resp.json().get('errmsg'))
    else:
        logging.error(f'官方服务器发生异常,错误代码:{resp.status_code},信息:{resp.text}')
        raise RuntimeError('server error')

    if '验证码错误' in resp.json().get('errmsg'):
        return False
    else :
        return True

def save_code_image():
    res = session.get(url="https://m.fjcyl.com/validateCode?0.123123&width=58&height=19&num=4")
    with open('code.jpg', 'wb') as f:
        f.write(res.content)


def crawl():
    times = 0
    while times < int(settings.MAX_TRIES):
        save_code_image()
        code = get_code('code.jpg')
        if len(code) != 4:
            continue
        try:
            if login(code):
                study_record()
                break
            else:
                times += 1
        except RuntimeError:
            logging.info(f'尝试重新登录，重试次数{times}')
            times += 1
