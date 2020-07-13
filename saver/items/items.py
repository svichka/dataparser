from connector.connector import Connector
import json
import datetime
from bs4 import BeautifulSoup

from database import db_session

class Items:

    def __init__(self):
        self.meta = {}
        self.headers = {
            'Origin': 'https://rem.ru',
            'Referer': 'https://rem.ru/catalog/shini-496/',
            'Sec-Fetch-Site': 'same-origin',
            'X-Requested-With': 'XMLHttpRequest',
        }
        self.page = 1
        self.category_uid = '283987532579312'

    def get_ids(self, data):
        url = 'https://rem.ru/ajax/catalog/getGoodsList/?ajax_display_mode'
        conn = Connector(url, self.headers)
        return conn.post_data(data).text.replace('|SSD|', '')

    def get_data(self, data):
        url = 'https://rem.ru/ajax/catalog/updateGoodsOnPage/'
        conn = Connector(url, self.headers)
        return conn.post_data(data).text.replace('|SSD|', '')

    def process_data(self, data):
        data['page'] = self.page
        data['category_oid'] = self.category_uid
        response = json.loads(self.get_ids(data))
        self.meta = response['json']
        soup = BeautifulSoup(response['content'], features="html.parser")
        items = {}
        i = 0
        for option in soup.find_all('a', class_='good'):
           items[f'items[{i}]'] = (option['data-oid'])
           i += 1

        if i == 0:
            return None

        self.page += 1
        return json.loads(self.get_data(items))['json']['goods']


if __name__ == '__main__':
    items = Items()
    data = {
        'filter_by_car[brand_oid]': '281694020042787',
        'filter_by_car[family_oid]': '283175783762516',
        'filter_by_car[model_oid]': '281728379802108'
    }
    while True:
        result = items.process_data(data)
        if result is None:
            break
