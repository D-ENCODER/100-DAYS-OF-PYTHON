def defangaddress(address: str):
    return address.replace(".", "[.]")


print(defangaddress("1.1.1.1.1"))

# Defanging an IP address simply means to replace the "." with "[.]"
