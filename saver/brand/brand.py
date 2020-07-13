from bs4 import BeautifulSoup
from connector.connector import Connector
import datetime

from models import CarBrand
from database import db_session


class Brand:

    def get_data(self):
        url = 'https://rem.ru/catalog/shini-496/'
        headers = {}
        conn = Connector(url, headers)
        return conn.get_data()

    def process_data(self, data):
        result = []
        soup = BeautifulSoup(self.get_data().content, features="html.parser")
        for option in soup.find('select', class_='brand').find_all('option'):
            if option['value']:
                result.append({
                    'id': option['value'],
                    'name': option.get_text()
                })

        return result


if __name__ == '__main__':
    brand = Brand()
    current_datetime = datetime.datetime.now()
    for item in brand.process_data():
         model = CarBrand(id=item['id'], name=item['name'], parse_date=current_datetime)
         db_session.merge(model)
         db_session.commit()
