from com.aak.modules.db.schedDataAccess import Programcurd
from com.aak.modules.db.personalDA import Personalcurd
from com.aak.modules.db.zonepersonalDA import Zonecurd
from com.aak.modules.config.configRead import Configread
from com.aak.modules.db.dbDao import Dbdao,Users,Zonepersonal

class Schedreset(object):
    def __init__(self):
        self.Da = Programcurd()
        self.getConfig = Configread()
        self.num_prg = self.getConfig.num_programs() + 1
        for i in range(self.num_prg):
            if i != 0:
                jbdetails = {}
                self.Da.updateProgramdetails(i, **jbdetails)

class Personalreset(object):
    def __init__(self):
        self.Da = Personalcurd()
        self.Da.updatePersonaldetails('','','','','')

class Zonereset(object):
    def __init__(self):
        self.zonep = Zonepersonal()
        self.x = Dbdao()
        self.engine = self.x.Connect()
        self.zonep.__table__.drop(self.engine)

        self.Da = Zonecurd()
        self.getConfig = Configread()
        self.num_zones = int(self.getConfig.num_zones()) + 1
        for i in range(self.num_zones):
            if i != 0:
                zname=''
                self.Da.updateZonedetails(i,zname)


class Userreset(object):
    def __init__(self):
        self.users = Users()
        self.x = Dbdao()
        self.engine = self.x.Connect()
        self.users.__table__.drop(self.engine)


