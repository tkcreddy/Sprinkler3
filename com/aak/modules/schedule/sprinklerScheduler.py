from flask import Flask, request,jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from com.aak.modules.runtime.runJobs import Runjobs
from com.aak.modules.config.configRead import Configread
import json
import os
schedule_app = Flask(__name__)

getConfig = Configread()
sql_loc = os.path.join(os.path.dirname(os.path.abspath(__file__)), getConfig.scheddb_loc())
# initialize scheduler with your preferred timezone
scheduler = BackgroundScheduler()
scheduler.add_jobstore('sqlalchemy', url='sqlite:///'+ sql_loc)
scheduler.start()


@schedule_app.route('/scheduleTime', methods=['POST'])
def schedule_by_time():
    data = request.get_json()
    time = data.get('time')
    prgid = data.get('prgid')
    date_time = datetime.strptime(str(time), '%Y-%m-%dT%H:%M')
    job = scheduler.add_job(Runjobs,args=[prgid], trigger='date', next_run_time=str(date_time))
    return "job details: %s" % job , 200


@schedule_app.route('/listProgram', methods=['GET'])
def schedule_list():
    for job in scheduler.get_jobs():
        print("name: %s, id: %s, trigger: %s, next run: %s, handler: %s, argument: %s" % (
            job.name, job.id, job.trigger, job.next_run_time, job.func, job.args))
    return "Welcome! %s" % jsonify(request.json)

@schedule_app.route('/getProgram', methods=['POST'])
def schedule_getprogram():
    data = request.get_json()
    prgid = data.get('prgid')
    job = scheduler.get_job(str(prgid))
    #c = json.loads(str(job))
    print("name: %s, id: %s, trigger: %s, next run: %s, handler: %s, argument: %s" % (
        job.name, job.id, job.trigger, job.next_run_time, job.func, job.args))
    #print(c)
    #print(scheduler.get_job(str(prgid)))
    return "Welcome! %s" % jsonify(request.json)


@schedule_app.route('/scheduleProgram', methods=['POST'])
def schedule_program():
    print("hello")
    data = request.get_json()
    print(data)
    prgid = data.get('prgid')
    jobdow = data.get('day_of_week')
    jobhour = data.get('hour')
    jobmin = data.get('minute')
    jobid = str(prgid)
    scheduler.add_job(Runjobs,args=[prgid], trigger='cron', day_of_week=jobdow, hour=jobhour, minute=jobmin, id=jobid)
    return "job details: %s" % jobid , 200

@schedule_app.route('/removeProgram', methods=['POST'])
def schedule_removeprogram():
    #data = request.get_json()
    #scheduler.print_jobs()
    data = request.get_json()
    prgid = data.get('prgid')
    print(scheduler.remove_job(str(prgid)))
    return "Welcome! %s" % jsonify(request.json)


def printing_something(text):
    print("printing %s at %s" % (text, datetime.now()))

schedule_app.run(host='0.0.0.0', port=12345)