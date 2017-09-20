from database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.types import DateTime

class Signups(Base):
    """
    Example Signups table
    """
    __tablename__ = 'signups'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    email = Column(String(256), unique=True)
    date_signed_up = Column(DateTime())


class Models(Base):

    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))
    ext_id = Column(String(256), unique=True)
    parse_date = Column(DateTime())