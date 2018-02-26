from datetime import *
import twilio
from twilio.rest import Client
import csv, os.path

accountSID='ACa4bbdbdaa5d55b49cfb291cfe9c03c29'
authToken='b7c2577a76456cfc4bf287a155d8f35a'
client = Client(accountSID, authToken)

myTwilioNumber = '+14142401173'
myCellPhone = '+15132908160'

now = str(datetime.now())
today = now[5:10]
##today = '04-25'


filename="birthdays.csv"


while True:
    file_exists = os.path.isfile(filename)
    newEntry = input("Add a New Birthday? (Yes, No): ").upper()
    if newEntry == "YES":
        name = input("Enter Persons Name: ").title()
        birthday = input(str("Enter Persons Birthday (mm-dd-yyyy): "))
        month_day=birthday[:5]
        year=birthday[6:]
                
        myData = [name,month_day]
        myFile = open(filename, 'a')
    
        
        with myFile:
            writer = csv.writer(myFile)
            writer.writerow(myData)
        
    else:
        break
    

reader = csv.reader(open(filename, 'r'))
birthdays = {}

for row in reader:
    name, birthday = row
    birthdays[name] = birthday
for name in birthdays:
    if birthdays[name] == today:
        print(birthdays[name])
        print("Today is "+name+"'s Birthday. Give Them a Call!")
        message = client.messages.create(body="Today is "+name+"'s Birthday. Give Them a Call!", from_=myTwilioNumber, to=myCellPhone)
    else:
        print("Not Today!")
                







