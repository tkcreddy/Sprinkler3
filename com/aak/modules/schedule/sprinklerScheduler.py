from flask import Flask, request,jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import *
from datetime import datetime
from com.aak.modules.runtime.runJobs import Runjobs
from com.aak.modules.config.configRead import Configread
from com.aak.modules.db.schedDataAccess import Programcurd
import traceback
import os
import json


BASE_PATH = '../db'

schedule_app = Flask(__name__)
getConfig = Configread()
sql_loc = os.path.join(BASE_PATH, getConfig.scheddb_loc())
scheduler = BackgroundScheduler()
scheduler.add_jobstore('sqlalchemy', url='sqlite:///'+ sql_loc)
scheduler.start()



def addprogram(prgid,dow,hour,min ):
    try:
        scheduler.add_job(Runjobs,args=[prgid], trigger='cron', day_of_week=dow, hour=hour, minute=min, id=str(prgid))
    except ConflictingIdError as ex:
        print("Please delete the Program and re-added it")



def remprogram(prgid):
    try:
        scheduler.remove_job(str(prgid))
    except JobLookupError as e:
        print("There is no Job with that id")
    except Exception as ex:
        traceback.print_exc()



@schedule_app.route('/scheduleTime', methods=['POST'])
def schedule_by_time():
    try:
        data = request.get_json()
        time = data.get('time')
        prgid = data.get('prgid')
        date_time = datetime.strptime(str(time), '%Y-%m-%dT%H:%M')
        job = scheduler.add_job(Runjobs, args=[prgid], trigger='date', next_run_time=str(date_time))

    except ConflictingIdError as ex:
        print("Please delete the Program and re-added it")
        #traceback.print_exc()

    return "job details: %s" % ex , 200




@schedule_app.route('/listProgram', methods=['GET'])
def schedule_list():
    try:
        for job in scheduler.get_jobs():
            print("name: %s, id: %s, trigger: %s, next run: %s, handler: %s, argument: %s" % (
                job.name, job.id, job.trigger, job.next_run_time, job.func, job.args))

    except Exception as ex:
            traceback.print_exc()

    return "Welcome! %s" % jsonify(request.json)



@schedule_app.route('/getProgram', methods=['POST'])
def schedule_getprogram():
    try:
        data = request.get_json()
        job = scheduler.get_job(data.get('prgid'))
        print("name: %s, id: %s, trigger: %s, next run: %s, handler: %s, argument: %s" % (
            job.name, job.id, job.trigger, job.next_run_time, job.func, job.args))
    except Exception as ex:
            traceback.print_exc()
    return "Welcome!"




@schedule_app.route('/scheduleProgram', methods=['POST'])
def schedule_program():
    try:
        data = request.get_json()
        jobd = '{' + data.get('jobdetails') + '}'
        pjobd = json.loads(jobd)
        schedaoobj = Programcurd()
        schedaoobj.updateProgramdetails(data.get('prgid'),**pjobd)
        addprogram(data.get('prgid'), data.get('day_of_week'), str(int(data.get('hour'))), str(int(data.get('minute'))))
    except Exception as ex:
        traceback.print_exc()
    return "job details: %s" % data.get('prgid') , 200
    #return "job details:"



@schedule_app.route('/updateProgram', methods=['POST'])
def schedule_updateprogram():
    try:
        data = request.get_json()
        jobd = '{' + data.get('jobdetails') + '}'
        pjobd = json.loads(jobd)
        schedaoobj = Programcurd()
        remprogram(data.get('prgid'))
        schedaoobj.updateProgramdetails(data.get('prgid'),**pjobd)
        addprogram(data.get('prgid'), data.get('day_of_week'), str(int(data.get('hour'))), str(int(data.get('minute'))))
    except Exception as ex:
        traceback.print_exc()

    return "job details: %s" % data.get('prgid') , 200



@schedule_app.route('/removeProgram', methods=['POST'])
def schedule_removeprogram():
    try:
        data = request.get_json()
        pjobd = { "":""}
        schedaoobj = Programcurd()
        remprogram(data.get('prgid'))
        schedaoobj.updateProgramdetails(data.get('prgid'),**pjobd)
    except Exception as ex:
        traceback.print_exc()
    return "Welcome! %s" % jsonify(request.json)


schedule_app.run(host='0.0.0.0', port=12345)