from connector.connector import Connector
import json
import datetime

from database import db_session

class Model:

    def get_data(self, data):
        url = 'https://rem.ru/ajax/catalog/getModels/'
        headers = {
            'Origin': 'https://rem.ru',
            'Referer': 'https://rem.ru/catalog/shini-496/',
            'X-Requested-With': 'XMLHttpRequest',
        }
        conn = Connector(url, headers)
        return conn.post_data(data)

    def process_data(self, data):
        return json.loads(self.get_data(data).text.replace('|SSD|', ''))['json']['models_list']


if __name__ == '__main__':
    model = Model()
    data = {'brand_oid': '281694020042754', 'family_oid': '283175783759904'}
    print(model.process_data(data))
