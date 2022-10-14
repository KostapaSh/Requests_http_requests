from pprint import pprint
import requests
from datetime import datetime

class YaDisk:


    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def write_file(self, file):
        current_datetime = str(datetime.now())

        with open('file_to_yadisc.txt', 'w', encoding='utf8') as w_file:
            w_file.writelines(current_datetime)


    def upload_file(self, file):
        w_file = file

        self.write_file(w_file)

        get_up_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": w_file, "overwrite": "true"}

        get_response = requests.get(get_up_url, headers=headers, params=params)
        href = get_response.json().get("href", "")

        pprint(get_response.json())

        put_response = requests.put(href, data=open(w_file, 'rb'))
        put_response.raise_for_status()
        if put_response.status_code == 201:
            print("Success")


ya_d =  YaDisk(token = tok)
ya_d.upload_file('file_to_yadisc.txt')