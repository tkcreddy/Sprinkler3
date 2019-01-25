from com.aak.modules.runtime.runzonejob import *

class runjobs():
    def __init__(self,**data):
        self.jobs_hash = {}
        self.jobs_hash = data
        for key, value in self.jobs_hash.items():
            Runzonejob(key,value)
