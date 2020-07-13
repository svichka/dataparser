from abc import ABC, abstractmethod
from models import CarBrand
from models import CarModelFamily
from models import CarModel
from models import CarObject
from models import ProductObject
from models import CarProductLink
from saver.brand.brand import Brand
from saver.family.family import Family
from saver.model.model import Model
from saver.items.items import Items
from database import db_session
import datetime


class AbstracSaver(ABC):

    def __init__(self):
        self.getter = None
        self.model = None
        self.items = None
        self.current_datetime = datetime.datetime.now()

    def set_items(self, data):
        self.items = self.getter.process_data(data)

    def get_items(self):
        return self.items

    def commit(self):
        db_session.commit()

    @abstractmethod
    def save(self, data):
        pass

    def get_or_create(self, model, **kwargs):
        instance = db_session.query(model).filter_by(**kwargs).first()
        if not instance:
            instance = model(parse_date=self.current_datetime, **kwargs)
            db_session.add(instance)


class BrandSaver(AbstracSaver):

    def __init__(self):
        super().__init__()
        self.getter = Brand()

    def save(self, data):
        self.set_items(data)
        if self.items is None:
            return
        for item in self.items:
            self.get_or_create(CarBrand, id=item['id'], name=item['name'])

        self.commit()


class FamilySaver(AbstracSaver):

    def __init__(self):
        super().__init__()
        self.getter = Family()

    def save(self, data):
        self.set_items(data)
        if self.items is None:
            return
        for item in self.items:
            self.get_or_create(CarModelFamily,
                               id=str(item['value']),
                               name=item['name'],
                               brand_id=str(data['brand_oid'])
                               )
            #print(f'{item["value"]} processed')
        self.commit()


class ModelSaver(AbstracSaver):

    def __init__(self):
        super().__init__()
        self.getter = Model()

    def save(self, data):
        self.set_items(data)
        if self.items is None:
            return
        for item in self.items:
            self.get_or_create(CarModel,
                               id=str(item['value']),
                               name=item['name'],
                               family_id=str(data['family_oid'])
                               )
            #print(f'{item["value"]} processed')
        self.commit()


class ObjectSaver(AbstracSaver):

    def __init__(self):
        super().__init__()

    def save(self, data):
        self.get_or_create(CarObject,
                           family_id=data['family_id'],
                           brand_id=data['brand_id'],
                           model_id=data['model_id']
                           )
        self.commit()


class ProductSaver(AbstracSaver):

    def __init__(self):
        super().__init__()
        self.object_id = None
        self.getter = Items()

    def set_object_id(self, object_id):
        self.object_id = object_id

    def save(self, data):
        while True:
            self.set_items(data)
            if self.items is None:
                return
            if len(self.items.keys()) != db_session.query(ProductObject).filter(ProductObject.id.in_(self.items.keys())).count():
                for key in self.items:
                    item = self.items[key]
                    self.get_or_create(ProductObject,
                                       id=str(item['oid']),
                                       code=str(item['code']),
                                       name=str(item['name']),
                                       group_code=str(item['group_code']),
                                       group_name=str(item['group_name']),
                                       price=str(item['price']),
                                       prof1_price=str(item['prof1_price']),
                                       prof2_price=str(item['prof2_price']),
                                       is_order_allow=int(item['group_code']),
                                       producer_name=str(item['producer_name']),
                                       is_universal=int(item['is_universal']),
                                       )

            for key in self.items:
                item = self.items[key]
                if self.object_id is not None:
                    self.model = CarProductLink(car_object_id=self.object_id, product_object_id=item['oid'])
                    self.get_or_create(CarProductLink,
                                       car_object_id=str(self.object_id),
                                       product_object_id=str(item['oid'])
                                       )

            self.commit()
