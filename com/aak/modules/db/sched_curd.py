from sqlalchemy.orm import sessionmaker
from com.aak.modules.db.schedDao import schedDao,Schedule, Base
schedDao()
engine = schedDao().Connect()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

def add_programs():
    num_prg = 11
    for i in range(num_prg):
        if i != 0:
            new_job = Schedule(id=i, name='Program ' + i,Job_details='{}')
            session.add(new_job)
            session.commit()



#job = session.query(Schedule).filter(Schedule.id == '3').one()
#print(job.Job_details)
#job.Job_details = '{"3" : 5}'
#session.commit()

#session.update(Schedule).values(Job_details = {"3" : 30, "4" : 10}).where(id == 2)
#print("",new_job.id, new_job.name, new_job.Job_details)
#session.add(new_job)
#session.commit()
