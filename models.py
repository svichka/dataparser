from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime


class CarBrand(Base):

    __tablename__ = 'car_brand'
    id = Column(String(256), primary_key=True)
    name = Column(String(256))
    parse_date = Column(DateTime())


class CarModelFamily(Base):

    __tablename__ = 'car_model_family'
    id = Column(String(256), primary_key=True)
    brand_id = Column(String(256))
    name = Column(String(256))
    parse_date = Column(DateTime())


class CarModel(Base):

    __tablename__ = 'car_model'
    id = Column(String(256), primary_key=True)
    family_id = Column(String(256))
    name = Column(String(256))
    parse_date = Column(DateTime())


class CarObject(Base):

    __tablename__ = 'car_object'
    id = Column(Integer, primary_key=True)
    brand_id = Column(String(256))
    family_id = Column(String(256))
    model_id = Column(String(256))
    parse_date = Column(DateTime())


class ProductObject(Base):

    __tablename__ = 'product_object'
    id = Column(String(256), primary_key=True)
    code = Column(String(256))
    name = Column(String(256))
    group_code = Column(String(256))
    group_name = Column(String(256))
    price = Column(String(256))
    prof1_price = Column(String(256))
    prof2_price = Column(String(256))
    is_order_allow = Column(Integer)
    producer_name = Column(String(256))
    is_universal = Column(Integer)
    onstock = Column(Integer)
    parse_date = Column(DateTime())


class CarProductLink(Base):

    __tablename__ = 'car_product_link'
    id = Column(Integer, primary_key=True)
    car_object_id = Column(String(256))
    product_object_id = Column(String(256))
    parse_date = Column(DateTime())
