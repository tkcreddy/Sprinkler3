from com.aak.modules.db.dbDao import Dbdao,Schedule, Base
from sqlalchemy.orm import sessionmaker
import json
import traceback
from sqlalchemy.orm import exc

class Programcurd(object):
    def __init__(self):
        self.Dao = Dbdao()
        self.engine = self.Dao.Connect()
        Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)

    def getProgramdetails(self,id):
        try:
            session = self.DBSession()
            self.sdata = {}
            self.job = session.query(Schedule).filter(Schedule.id == id).one()
            self.sdata = self.job.Job_details.replace("'", "\"")
            self.sdata = json.loads(self.sdata)
            return self.sdata
        except exc.NoResultFound:
            print("No rows")

        finally:
            session.close()

    def updateProgramdetails(self,id, **jd):
        try:
            self.jd = {}
            session = self.DBSession()
            self.job = session.query(Schedule).filter(Schedule.id == id).one()
            self.jd = jd
            self.job.Job_details = str(self.jd)

        except exc.NoResultFound:
            # traceback.print_exc()
            new_entry = Schedule(id=id, Job_details=str(self.jd))
            session.add(new_entry)

        finally:
            session.commit()
            session.close()


#x = Programcurd()


#dic = {"3" : 200}

#x.updateProgramdetails(2, **dic)

# = Programcurd()

#d = x.getProgramdetails(2)

#for k, v in d.items():
#    print("Zone is {} and Time is {} ".format(k, v))