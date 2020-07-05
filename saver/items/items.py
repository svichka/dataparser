from connector.connector import Connector
import json
import datetime
from bs4 import BeautifulSoup

from models import Models
from database import db_session

class Items:

    def __init__(self):
        self.headers = {
            'Origin': 'https://rem.ru',
            'Referer': 'https://rem.ru/catalog/shini-496/',
            'Sec-Fetch-Site': 'same-origin',
            'X-Requested-With': 'XMLHttpRequest',
        }

    def get_ids(self, data):
        url = 'https://rem.ru/ajax/catalog/getGoodsList/?ajax_display_mode'
        conn = Connector(url, self.headers)
        return conn.post_data(data).text.replace('|SSD|', '')

    def get_data(self, data):
        url = 'https://rem.ru/ajax/catalog/updateGoodsOnPage/'
        conn = Connector(url, self.headers)
        return conn.post_data(data).text.replace('|SSD|', '')

    def process_data(self, data):
        response = json.loads(self.get_ids(data))
        meta = response['json']
        soup = BeautifulSoup(response['content'], features="html.parser")
        current_datetime = datetime.datetime.now()
        items = {}
        i = 0
        for option in soup.find_all('a', class_='good'):
           items[f'items[{i}]'] = (option['data-oid'])
           i += 1

        data = json.loads(self.get_data(items))['json']['goods']
        print(data)
        print(meta['total_count'])


if __name__ == '__main__':
    items = Items()
    data = {
        'filter_by_car[brand_oid]': '281694020042787',
        'filter_by_car[family_oid]': '283175783762516',
        'filter_by_car[model_oid]': '281728379802108',
        'page': 1,
        'category_oid': '283987532579312'
    }
    items.process_data(data)