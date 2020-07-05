from connector.connector import Connector
import json
import datetime

from models import Models
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


if __name__ == '__main__':
    model = Family()
    data = {'brand_oid': '281694020042754'}
    r = json.loads(model.get_data(data).text.replace('|SSD|', ''))['json']['families_list']
    print(r)
