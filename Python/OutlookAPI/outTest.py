from O365 import Account, MSGraphProtocol
import datetime as dt

CLIENT_ID = '9895b582-58b1-4110-8699-4bfa79360707'
SECRET_ID = 'fnG8Q~6ofLyCbTCudkL3CVQxqAut1x8K5e_.ba3D'

credentials = (CLIENT_ID, SECRET_ID)

#Protocol is type of API we chose (MSGraph)
protocol = MSGraphProtocol() 
#Specifying default resource for the protocol will determine which calendar we are pointed at. 
#If left blank, the calendar is that of the user when they log in during authentication
#protocol = MSGraphProtocol(defualt_resource='<sharedcalendar@domain.com>')

#Scopes represents the permissions granted to this API. 
scopes = ['Calendars.Read', 'Calendars.Read.Shared', 'Calendars.ReadWrite', 'Calendars.ReadWrite.Shared', 'User.Read']
account = Account(credentials, protocol=protocol)

if account.authenticate(scopes=scopes):
   print('Authenticated!')

schedule = account.schedule()
calendar = schedule.get_default_calendar()
#events = calendar.get_events(include_recurring=False) 

q = calendar.new_query('start').greater_equal(dt.datetime(2024, 1, 1))
q.chain('and').on_attribute('end').less_equal(dt.datetime(2024, 2, 24))
events = calendar.get_events(limit=500, query=q, include_recurring=True)

for event in events:
    eventStr = str(event)
    if "Busy" in eventStr or "Word" in eventStr:
        "ignore"
    else:
        print(event)
        print(" ---------- ")
        print(event.attendees)