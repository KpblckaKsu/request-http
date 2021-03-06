TOKEN = 'AQ...b3_KY' #Изменила токен по рекомендации преподавателя
import requests
import os

class YaUploader:
    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload(self, disk_file_path, filename):
        link = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(link, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    path = os.getcwd()
    file_name = "testHW.txt"
    path_to_file = os.path.join(path, file_name)
    disk_file_path = "netology/testHW.txt"
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(disk_file_path, path_to_file)



