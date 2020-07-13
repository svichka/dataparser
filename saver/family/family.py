from connector.connector import Connector
import json
import datetime

from database import db_session

class Family:

    def get_data(self, data):
        url = 'https://rem.ru/ajax/catalog/getFamilies/'
        headers = {
            'Origin': 'https://rem.ru',
            'Referer': 'https://rem.ru/catalog/shini-496/',
            'X-Requested-With': 'XMLHttpRequest',
        }
        conn = Connector(url, headers)
        return conn.post_data(data)

    def process_data(self, data):
        js = json.loads(self.get_data(data).text.replace('|SSD|', ''))['json']
        return None if js is None else json.loads(self.get_data(data).text.replace('|SSD|', ''))['json']['families_list']


if __name__ == '__main__':
    model = Family()
    data = {'brand_oid': '281694020042754'}
    print(model.process_data(data))
