import requests
import random
import time
import os
from config import *

url = "https://discord.com/api/v8/channels/" + channel_id + "/messages"

cookies = {
    '_ga': 'GA1.2.735792174.1600309507',
    'locale': 'en-US',
}

headers = {
    'Host': 'discord.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json',
    'Authorization': os.environ.get('CASINO_BOT_TOKEN'),
    'Origin': 'https://discord.com',
    'Connection': 'close',
}


def main(message):
    data = '{"content":"' + message + '","nonce":' + \
        str(random.randint(1000, 99999999))+',"tts":false}'
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    return response.content


while True:
    try:
        main('*work')
        time.sleep(2)
        main('*dep all')
        time.sleep(cooldown_time)
        continue
    except:
        pass
