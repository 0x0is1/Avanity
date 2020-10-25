from logger import *
import requests
import random
import time
from config import *
import sys

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
    'Authorization': 'null',
    'Origin': 'https://discord.com',
    'Connection': 'close',
}


def main(message, auth_token):
    headers['Authorization'] = auth_token
    data = '{"content":"' + message + '","nonce":' + \
        str(random.randint(1000, 99999999))+',"tts":false}'
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    return response.content

def logging():
    email = input('Enter your email address: ')
    password = input('Enter your password: ')
    print('Logging in...')
    try:
        token = login(email, password)
        if len(token) == 59:
            print('Login successfull')
            f = open('tempfile.txt', 'w')
            f.write(token)
            f.close()
        else:
            print(token)
            exit(0)
    except:
        print('check email and password again!')
        exit(0)
        

def log_check():
    file = open('tempfile.txt', 'r')
    try:
        auth_token = file.read()   
    except Exception as e:
        logging()
        auth_token = file.read()
    file.close()
    return auth_token

def app():
    i = 0
    while True:
        auth_token = log_check()
        if auth_token == '':
            print('You are not logged in, please login')
            logging()
            continue
        i += 1
        try:
            if i == 1:
                res = main('ping', auth_token).decode('utf-8')
                try:
                    if '401: Unauthorized' in json.loads(res['message']):
                        print(json.loads(res['message']))
                        exit(0)
                except:
                    pass
            print('Bot running for count: ' + str(i))
            if work:
                time.sleep(wait_duration)
                main('*work', auth_token)
            if crime:
                time.sleep(wait_duration)
                main('*crime', auth_token)
            if slut:
                time.sleep(wait_duration)
                main('*slut', auth_token)
            time.sleep(wait_duration)
            main('*dep all', auth_token)
            time.sleep(cooldown_time)

        except KeyboardInterrupt:
            print('You pressed ctr+C')
            choice = input('Press c for continue, e for exit, l for lougout and exit: ')
            if choice == 'c':
                pass
            if choice == 'e':
                break
            if choice == 'l':
                logout(auth_token)
                file = open('tempfile.txt', 'w')
                file.write('')
                file.close()
                print('Logged out!')
                break
            else:
                print('Unknown choice entered, exiting...')
        except:
            pass

try:
    if sys.argv[1] == '--version':
        print('Avanity version 1.0')
        print('Author: 0x0is1')
except:
    print('Avanity version 1.0')
    print('Author: 0x0is1')
    app()
