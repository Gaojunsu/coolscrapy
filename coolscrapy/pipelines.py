# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import sqlalchemy
import win32com.client as  win32
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from coolscrapy.model import weekly, Base, engin, loadSession


class SomethingPipeline(object):

    def __init__(self):
        Base.metadata.create_all(engin)
        app = 'Excel'
        self.x1 = win32.gencache.EnsureDispatch('%s.Application' % app)
        self.ss = self.x1.Workbooks.Add()
        self.sh = self.ss.ActiveSheet
        self.x1.Visible = True
        self.session = loadSession()
        self.i = 2
        self.j = 5
    def process_item(self,item,spider):
        self.sh.Cells(self.j-1, 1).Value = "标题"
        self.sh.Cells(self.j,1).Value = "URL连接"
        self.sh.Cells(self.j + 1,1).Value = "内容简介"

        #content = json.dumps(dict(item), ensure_ascii=False) + "\n"#生成一条json
        if item['href'] and item['content'] is not None:
            self.sh.Cells(self.j-1, self.i).Value = item['title']
            self.sh.Cells(self.j - 1, self.i).Font.Bold=True
            self.sh.Cells(self.j, self.i).Value = item['href']
            self.sh.Cells(self.j + 1, self.i).Value =item['content']
            self.i = self.i + 1
            bean=weekly.weekly(href=str(item['href']),content=str(item['content']),title=str(item['title']))
            self.session.add(bean)
            self.session.commit()
            if self.i>10:
                self.i=2
                self.j+=3
        return item



    def open_spider(self,spider):
        pass
    def close_spider(self,spider):
        self.ss.Close(True)
        self.x1.Application.Quit()

