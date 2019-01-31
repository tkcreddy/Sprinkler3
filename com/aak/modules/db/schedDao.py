from sqlalchemy import Column, Integer, String, JSON, Sequence, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import os
from com.aak.modules.config.configRead import Configread

Base = declarative_base()
class schedDao():
    def __init__(self):
        self.getConfig = Configread()
        self.sql_loc = os.path.join(os.path.dirname(os.path.abspath(__file__)), self.getConfig.scheddb_loc())

    def Connect(self):
        self.engine = create_engine('sqlite:///' + self.sql_loc)
        Base.metadata.create_all(self.engine)
        return self.engine

class Schedule(Base):
    __tablename__ = 'sched_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    Job_details = Column(String(250), nullable=False)



