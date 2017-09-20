import requests
import configparser

#config = configparser.ConfigParser()
#config.read('config.ini')


class Connector:

    def __init__(self, url, headers):
        self._url = url
        self._headers = headers

    def get_data(self):

        with requests.get(self._url, headers=self._headers) as resp:
            requests.encoding = 'utf-8'
            if resp.status_code != 200:
                raise RuntimeError("Invalid response received: code: %d, message: %s" % (resp.status_code, resp.text))

            return resp

