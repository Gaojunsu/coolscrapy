from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engin = create_engine('sqlite:////Users/Jean_Su/Desktop/MeasureAllDat12a.db', echo=True)
Base = declarative_base()

def loadSession():
    Session=sessionmaker(bind=engin)
    session=Session()
    return session