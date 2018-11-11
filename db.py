from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Text, Boolean, Float
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///real_estate.sqlite')

db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()


class Ad(Base):
    __tablename__ = 'ads'

    id = Column(Integer, primary_key=True)
    settlement = Column(String(50), nullable=False)
    under_construction = Column(Boolean, nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Integer, nullable=False)
    oblast_destrict = Column(String(50), nullable=False)
    living_area = Column(Float)
    has_balcony = Column(Boolean, nullable=False)
    address = Column(String(100), nullable=False)
    construction_year = Column(Integer)
    rooms_number = Column(Integer, nullable=False)
    premise_area = Column(Float, nullable=False)
    active = Column(Boolean, nullable=False)


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
