from com.aak.modules.runtime.runZone import *
from com.aak.modules.db.schedDataAccess import Programcurd
import traceback
class Runjobs():
    def __init__(self,prgid):
        self.prgid = prgid
        self.jobs_hash = {}
        self.db = Programcurd()
        self.jobs_hash = self.db.getProgramdetails(self.prgid)
        try:
            for key, value in self.jobs_hash.items():
                Runzonejob(key,value)

        except Exception as ex:
            traceback.print_exc()

        finally:
            print("completed the job")
            pass

if __name__ == '__main__':
    Runjobs()
