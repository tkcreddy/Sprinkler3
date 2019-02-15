from com.aak.modules.db.resetDb import Schedreset,Personalreset,Zonereset,Userreset
from com.aak.modules.db.userDA import Userscurd
Schedreset()
Personalreset()
Zonereset()
Userreset()
users = Userscurd()
users.insertUser("admin","password")
