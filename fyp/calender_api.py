from print import pprint

from Google import Create_Service, convert_to_RFC_datetime

CLIENT_SECRET_FILE = 'client_secret_GoogleCloudDemo.json"

API_NAME = 'calendar'

API_VERSION = "V3"

SCOPES = ['https://www.googleapis.com/auth/calendar']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

calendar_id_chicago = '2h56pnrdsnhdnc02p7sigpfkfo@group.calendar.google.com'