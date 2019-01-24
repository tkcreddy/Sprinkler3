from config_read import configread

x=configread()
#print("", x.GPIO(4))
m = x.num_zones() + 1
k=x.list()
for i in range(m):
    if i != 0:
        print("Zone {} GPIO is {}".format(i,k[i]) )


#x = configread(2)