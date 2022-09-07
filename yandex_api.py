import requests
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    # Создание папки на яндекс диске
    def new_folder(self, path_folder):
        new_folder_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": path_folder}
        res = requests.put(new_folder_url, headers=headers, params=params).status_code
        if res == 202 or res == 201:
            pprint(f'ПАПКА: {path_folder},СОЗДАНА ДЛЯ ЗАПИСИ ФОТО НА ЯНДЕКС ДИСК СОЗДАНА!!!')

        return res

    def find_for_name_folder(self, name_folder):
        yandex_disc_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": name_folder}
        res = requests.get(yandex_disc_url, headers=headers, params=params).status_code
        return res

    def amount_folder(self, path):
        amount = 0
        yandex_disc_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        params = {"path": path, "type": "dir"}
        res = requests.get(yandex_disc_url, headers=headers, params=params).json()
        for i in res['_embedded']['items']:
            if i['type'] == 'dir':
                amount += 1
        return amount

