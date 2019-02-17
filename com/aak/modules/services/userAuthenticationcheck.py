from com.aak.modules.db.userDA import Userscurd


x=Userscurd()
if x.insertUser("admin1","password"):
   print("admin user was added")
else:
  print("failed user")


# if x.checkAuthentication("admin","password"):
#     print("print authentication is successfull")
# else:
#     print(" not valid Passsword")

#x.checkAuthentication("admin","password")



# if x.updatepassword("admin","password","password1"):
#    print("password change is successfull")
#hash = pbkdf2_sha256.encrypt("password", rounds=200000, salt_size=16)


#print(pbkdf2_sha256.verify("password", hash))

#print(x.checkAuthentication("admin","password12"))

# if x.deleteUsername("admin1"):
#     print("admin user was deleted")
# else:
#   print("failed user")


#x.insertUser("admin1","password")

# x.deleteUsername("admin1")