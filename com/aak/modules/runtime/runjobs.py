from com.aak.modules.runtime.runzonejob import *
import traceback
class runjobs():
    def __init__(self,**data):
        self.jobs_hash = {}
        self.jobs_hash = data
        try:
            for key, value in self.jobs_hash.items():
                Runzonejob(key,value)

        except Exception as ex:
            traceback.print_exc()

        finally:
            print("completed the job")
            pass

