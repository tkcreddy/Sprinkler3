from com.aak.modules.db.dbDao import Dbdao,Zonepersonal, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import exc
import json
import traceback

class Zonecurd(object):
    def __init__(self):
        self.Dao = Dbdao()
        self.engine = self.Dao.Connect()
        Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)

    def getZonedetails(self,id):
        try:
            session = self.DBSession()
            self.zname = ''
            self.zonep = session.query(Zonepersonal).filter(Zonepersonal.id == id).one()
            self.sname = self.zonep.name
            return self.sname
        except exc.NoResultFound:
            print("No rows")

        finally:
            session.close()

    def updateZonedetails(self,id,zname):
        try:
            self.zname = ''
            session = self.DBSession()
            self.zonep = session.query(Zonepersonal).filter(Zonepersonal.id == id).one()
            self.zname = zname
            self.zonep.name = str(self.zname)
        except exc.NoResultFound:
            #traceback.print_exc()
            new_zone = Zonepersonal(id=id, name=zname)
            session.add(new_zone)
        finally:
            session.commit()
            session.close()


x = Zonecurd()


#dic = {"3" : 200}

x.updateZonedetails(2, 'Test zone')

y = Zonecurd()
print(y.getZonedetails(2))

#for k, v in d.items():
#    print("Zone is {} and Time is {} ".format(k, v))