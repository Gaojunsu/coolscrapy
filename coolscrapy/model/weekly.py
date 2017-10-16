from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from coolscrapy.model import Base


class weekly(Base):
    __tablename__ = 'weekly'

    id=Column(Integer,primary_key=True)
    href =Column(String(500))
    content = Column(String(500))
    title = Column(String(500))

    def __init__(self,href,content,title):
        self.title=title
        self.content=content
        self.href=href

