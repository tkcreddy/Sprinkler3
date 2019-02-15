from sqlalchemy import Column, Integer, String, JSON, Sequence, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os


from com.aak.modules.config.configRead import Configread

Base = declarative_base()
class Dbdao():
    def __init__(self):
        BASE_PATH = '../db'
        self.getConfig = Configread()
        self.sql_loc = os.path.join(BASE_PATH, self.getConfig.db_loc())

    def Getsql_loc(self):
        pass
        return self.sql_loc

    def Connect(self):
        self.engine = create_engine('sqlite:///' + self.sql_loc)
        Base.metadata.create_all(self.engine)
        return self.engine

class Schedule(Base):
    __tablename__ = 'sched_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    Job_details = Column(String(250), nullable=False)


class Pernonalized(Base):
    __tablename__ = 'personal_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=True)
    email = Column(String(30), nullable=True)
    zip = Column(String(10),nullable=True)
    country = Column(String(5),nullable=True)
    owm_appid = Column(String(30),nullable=True)

class Zonepersonal(Base):
    __tablename__='zone_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=True)

class Users(Base):
    __tablename__='user_table'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(20), nullable=False, unique=True)
    password = Column(String,nullable=False)




