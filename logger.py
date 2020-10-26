import requests
import json

url = 'https://discord.com/api/v8/auth/login'
cookies = {
    'locale': 'en-US',
}

headers = {
    'Host': 'discord.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json',
    'Authorization': 'undefined',
    'Origin': 'https://discord.com',
    'DNT': '1',
    'Connection': 'close',
    'TE': 'Trailers',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}
def login(email, password):
    data = '{"email":"' + email + '","password": "' + password + '","undelete":false,"captcha_key":null,"login_source":null,"gift_code_sku_id":null}'
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    jdata = json.loads(str(response.content.decode("utf-8")))
    try:
        return jdata['token']
    except Exception as e:
        return e

def logout(auth_token):
    logout_url = 'https://discord.com/api/v8/auth/logout'
    data = '{"provider":null,"voip_provider":null}'
    headers['Authorization'] = auth_token
    response = requests.post(logout_url, headers=headers, cookies=cookies, data=data)
    return response.content.decode('utf-8')

