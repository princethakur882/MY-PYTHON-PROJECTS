import getpass
database = {"prince": "123456", "rohit": "654321", "vinay":"988200", "bharat":"789123", "subham":"146709"}
username = input("Enter Your Username : ")
password = getpass.getpass("Enter Your Password : ")
for i in database.keys():
    if username == i:
        while password != database.get(i):
            password = getpass.getpass("Enter Your Password Again : ")
        break
print("Verified")