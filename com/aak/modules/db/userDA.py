from com.aak.modules.db.dbDao import Dbdao,Users, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import exc
from sqlalchemy import exc
from passlib.hash import pbkdf2_sha256
from sqlite3 import IntegrityError

import json
import traceback

class Userscurd(object):
    def __init__(self):
        self.Dao = Dbdao()
        self.engine = self.Dao.Connect()
        Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)

    def getConnection(self):
        self.session = self.DBSession()
        return self.session

    def getUsername(self,username):
        try:
            session = self.DBSession()
            self.username = ''
            self.userdata = session.query(Users).filter(Users.username == username).one()
            self.username = self.userdata.username
            return self.username
        except exc.NoResultFound:
            print("No rows")

        finally:
            session.close()



    def insertUser(self,username,password):
        try:
            self.username = username
            #self.password = password
            session = self.DBSession()
            self.hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
            self.newuserdata = Users(username=self.username,password=self.hash)
            session.add(self.newuserdata)

        except exc.IntegrityError:
            "print User is already there"
        except IntegrityError:
            "print User is already there"
        finally:
            session.commit()
            session.close()

    def checkAuthentication(self,username,password):
        try:
            session = self.DBSession()
            self.hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
            self.userdata = session.query(Users).filter(Users.username == username).one()
            return pbkdf2_sha256.verify(password, self.userdata.password)

        except exc.NoResultFound:
            print("No user found.")
        finally:
            session.close()



    def updatepassword(self,username,password,newpassword):
        try:
            if self.checkAuthentication(username,password):
                session = self.DBSession()
                self.hash = pbkdf2_sha256.encrypt(newpassword, rounds=200000, salt_size=16)
                self.userdata = session.query(Users).filter(Users.username == username).one()
                self.userdata.password = self.hash


        except exc.NoResultFound:
            #traceback.print_exc()
            print("something failed")
            #session.add(new_zone)
        finally:
            session.commit()
            session.close()