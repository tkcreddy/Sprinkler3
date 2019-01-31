from com.aak.modules.db.schedDao import schedDao,Schedule, Base
from sqlalchemy.orm import sessionmaker
import json

class Programcurd(object):
    def __init__(self):
        self.Dao = schedDao()
        self.engine = self.Dao.Connect()
        Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)

    def getProgramdetails(self,id):
        session = self.DBSession()
        self.sdata = {}
        self.job = session.query(Schedule).filter(Schedule.id == id).one()
        self.sdata = self.job.Job_details.replace("'", "\"")
        self.sdata = json.loads(self.sdata)
        return self.sdata

    def updateProgramdetails(self,id, **jd):
        self.jd = {}
        session = self.DBSession()
        self.job = session.query(Schedule).filter(Schedule.id == id).one()
        self.jd = jd
        print(self.job.Job_details)
        self.job.Job_details = str(self.jd)
        print(self.job.Job_details)
        session.commit()


#x = Programcurd()


#dic = {"3" : 200}

#x.updateProgramdetails(2, **dic)

# = Programcurd()

#d = x.getProgramdetails(2)

#for k, v in d.items():
#    print("Zone is {} and Time is {} ".format(k, v))