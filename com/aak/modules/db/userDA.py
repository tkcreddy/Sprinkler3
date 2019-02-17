from com.aak.modules.db.dbDao import Dbdao,Users, Base
from sqlalchemy.orm import sessionmaker,exc
from sqlalchemy.exc import IntegrityError as sqlerr
from passlib.hash import pbkdf2_sha256
from sqlite3 import IntegrityError as sqerr
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
            self.session = self.DBSession()
            self.username = ''
            self.userdata = self.session.query(Users).filter(Users.username == username).one()
            self.username = self.userdata.username
            return self.username
        except exc.NoResultFound:
            print("No rows")

        finally:
            self.session.close()



    def insertUser(self,username,password):

        self.username = username
        self.session = self.DBSession()
        self.hash = pbkdf2_sha256.encrypt(password, rounds=200000, salt_size=16)
        self.newuserdata = Users(username=self.username,password=self.hash)
        self.session.add(self.newuserdata)
        try:
            self.session.commit()
            self.rv = True

        except sqerr as e:
            self.session.rollback()
            print("print User is already there sqerr", e)
            self.rv = False
        except sqlerr as err:
            self.session.rollback()
            if "UNIQUE constraint failed: self.username" in str(err):
                return False, "error, username already exists (%s)" % self.username
            print("print User is already there exc", err)
            self.rv = False


        finally:

            self.session.close()
            #print(self.rv)
            return self.rv

    def checkAuthentication(self,username,password):
        try:
            self.session = self.DBSession()
            self.userdata = self.session.query(Users).filter(Users.username == username).one()
            return pbkdf2_sha256.verify(password, self.userdata.password)

        except exc.NoResultFound:
            print("No user found.")
        finally:
            self.session.close()



    def updatepassword(self,username,password,newpassword):
        try:
            if self.checkAuthentication(username,password):
                self.session = self.DBSession()
                self.hash = pbkdf2_sha256.encrypt(newpassword, rounds=200000, salt_size=16)
                self.userdata = self.session.query(Users).filter(Users.username == username).one()
                self.userdata.password = self.hash
                self.returnvalue = 1
            else:
                self.returnvalue = 2
        except exc.NoResultFound:
            #traceback.print_exc()
            print("something failed")
            #session.add(new_zone)
        finally:
            self.session.commit()
            self.session.close()
            return self.returnvalue


    def deleteUsername(self,username):
        try:
            self.session = self.DBSession()
            self.username = ''
            self.session.query(Users).filter(Users.username == username).delete()
            self.rv = True

            # User.query.filter_by(id=123).delete()
            # User.query.filter(User.id == 123).delete()
            # self.username = self.userdata.username
            # return self.username
        except exc.NoResultFound:
            print("No rows")
            self.rv = False


        finally:
            self.session.commit()
            self.session.close()
            return self.rv
