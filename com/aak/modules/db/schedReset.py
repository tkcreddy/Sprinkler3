from com.aak.modules.db.schedDataAccess import Programcurd

class Schedreset(object):
    def __init__(self):
        self.Da = Programcurd()
        num_prg = 11
        for i in range(num_prg):
            if i != 0:
                jbdetails = {}
                self.Da.updateProgramdetails(i, **jbdetails)

    '''def reset(self):
        num_prg = 11
        for i in range(num_prg):
            if i != 0:
                jbdetails = {}
                self.Da.updateProgramdetails(i,**jbdetails)'''
