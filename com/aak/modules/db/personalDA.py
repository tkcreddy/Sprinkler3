from com.aak.modules.db.dbDao import Dbdao,Pernonalized, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import exc
import json
import traceback

class Personalcurd(object):
    def __init__(self):
        self.Dao = Dbdao()
        self.engine = self.Dao.Connect()
        Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)

    def getPersonaldetails(self):
        try:
            session = self.DBSession()
            self.name = ''
            self.personal = session.query(Pernonalized).filter(Pernonalized.id == 1).one()
            self.name = self.personal.name
            self.email = self.personal.email
            self.zip = self.personal.zip
            self.owm_appid = self.personal.owm_appid
            return self.name,self.email,self.zip,self.owm_appid
        except exc.NoResultFound:
            pass
            #print("No rows")

        finally:
            session.close()

    def updatePersonaldetails(self,name,email,zip,owm_appid):
        try:
            self.name = ''
            session = self.DBSession()
            self.personal = session.query(Pernonalized).filter(Pernonalized.id == 1).one()
            self.name = name
            self.personal.name = str(self.name)
            self.personal.email = str(email)
            self.personal.zip = str(zip)
            self.personal.owm_appid = str(owm_appid)
        except exc.NoResultFound:
            #traceback.print_exc()
            new_zone = Pernonalized(id=1, name=name,email=email,zip=zip,owm_appid=owm_appid)
            session.add(new_zone)
        finally:
            session.commit()
            session.close()


x = Personalcurd()


#dic = {"3" : 200}

#x.updateZonedetails(2, 'Test zone')

#y = Zonecurd()
#print(x.getPersonaldetails())
#x.updatePersonaldetails("Krishna Reddy","tkcreddy@yahoo.com",'92631','')
#print(x.getPersonaldetails())
#for k, v in d.items():
#    print("Zone is {} and Time is {} ".format(k, v))