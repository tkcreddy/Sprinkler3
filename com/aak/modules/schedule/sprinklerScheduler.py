from flask import Flask,jsonify,flash, redirect, render_template, request, session, abort
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.base import *
from datetime import datetime
from com.aak.modules.runtime.runJobs import Runjobs
from com.aak.modules.config.configRead import Configread
from com.aak.modules.db.schedDataAccess import Programcurd
from com.aak.modules.db.personalDA import Personalcurd
from com.aak.modules.db.zonepersonalDA import Zonecurd
from com.aak.modules.db.userDA import Userscurd
from flask import render_template
import traceback
import os
import json


BASE_PATH = '../db'

schedule_app = Flask(__name__)
schedule_app.secret_key = os.urandom(12)
getConfig = Configread()
sql_loc = os.path.join(BASE_PATH, getConfig.db_loc())
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

def checkprofile():
    PA = Personalcurd()
    name, email, zip, country, owm_appid = PA.getPersonaldetails()
    print(name, email, zip, country, owm_appid)
    if name == '' or email == '' or zip == '' or country == '' or owm_appid == '':
        return 'profile.html'
    else:
        return 'index.html'


@schedule_app.route('/', methods=['GET'])
def index():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template(checkprofile())



@schedule_app.route('/login', methods=['POST'])
def do_admin_login():
    login_auth = Userscurd()
    if login_auth.checkAuthentication(request.form['username'],request.form['password']):
        session['logged_in'] = True
        return render_template(checkprofile())
    else:
        error = 'Invalid Credentials. Please try again.'
        return render_template('login.html', error=error)

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
        schedaoobj = Programcurd()
        jobd = schedaoobj.getProgramdetails(int(data.get('prgid')))
        print("name: %s, id: %s, trigger: %s, next run: %s, handler: %s, argument: %s, Job Details: %s" % (
            job.name, job.id, job.trigger, job.next_run_time, job.func, job.args, jobd))
    except AttributeError as ex:
            print("Getting none rows")
            #traceback.print_exc()
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
        print("Getting none rows")
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


@schedule_app.route('/personalUpdate', methods=['POST'])
def schedule_personalUpdate():
    try:
        data = request.get_json()
        personalObject = Personalcurd()
        personalObject.updatePersonaldetails(data.get('name'),data.get('email'),data.get('zip'),data.get('country'),data.get('owm_appid'))
    except Exception as ex:
        pass
        traceback.print_exc()
    return  "Personal details update"



@schedule_app.route('/getPersonal', methods=['GET'])
def schedule_getPersonal():
    try:
        personalObject = Personalcurd()
        name, email, zip, country, owm_appid = personalObject.getPersonaldetails()
        # print(name,email,zip,country,owm_appid)
    except Exception as ex:
        pass
        traceback.print_exc()
    finally:
        # print(name, email, zip, country, owm_appid)
        return  "Personal details update %s %s %s %s %s" % (str(name), str(email), str(zip), str(country), str(owm_appid))


@schedule_app.route('/zoneinfoUpdate', methods=['POST'])
def schedule_zoneinfoUpdate():
    try:
        data = request.get_json()
        zoneinfoObject = Zonecurd()
        #zoneinfoObject.updateZonedetails()
        zoneinfoObject.updateZonedetails(data.get('id'),data.get('zname'))
    except Exception as ex:
        pass
        traceback.print_exc()
    return  "zone details update"

@schedule_app.route('/getZoneinfo', methods=['GET'])
def schedule_getZoneinfo():
    try:
        data = request.get_json()
        zoneinfoObject = Zonecurd()
        name = zoneinfoObject.getZonedetails(data.get('id'))
        print(data.get('id'),name)
    except Exception as ex:
        pass
        traceback.print_exc()
    return  "Zone details Get"


@schedule_app.route('/getZonelist', methods=['GET'])
def schedule_getZonelist():
    try:
        zoneinfoObject = Zonecurd()
        lists = zoneinfoObject.listAllzones()
        for list in lists:
            print(list.id , list.name)
    except Exception as ex:
        pass
        traceback.print_exc()
    return  "Zone list details"


schedule_app.run(host='0.0.0.0', port=8080)