from com.aak.modules.db.userDA import Userscurd


x=Userscurd()
#x.insertUser("admin1","password")
if x.checkAuthentication("admin","password"):
    print("print authentication is successfull")
else:
    print(" not valid Passsword")


#if x.updatepassword("admin","newpassword1","password"):
#   print("password change is successfull")
#hash = pbkdf2_sha256.encrypt("password", rounds=200000, salt_size=16)


#print(pbkdf2_sha256.verify("password", hash))

#print(x.checkAuthentication("admin","password12"))