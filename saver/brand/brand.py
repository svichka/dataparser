from bs4 import BeautifulSoup
from connector.connector import Connector
import datetime

from models import Models
from database import db_session

class Brand:

    def get_data(self):
        url = 'https://rem.ru/catalog/shini-496/'
        headers = {}
        conn = Connector(url, headers)
        return conn.get_data()


if __name__ == '__main__':
    model = Brand()
    r = model.get_data()
    encoding = r.encoding if 'charset' in r.headers.get('content-type', '').lower() else None
    soup = BeautifulSoup(r.content, features="html.parser")
    current_datetime = datetime.datetime.now()

    for option in soup.find('select', class_='brand').find_all('option'):
        if option['value']:
            model = Models(ext_id=option['value'], name=option.get_text(), parse_date=current_datetime)
            db_session.add(model)
            db_session.commit()
