from __future__ import print_function
from calendar import calendar
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def create_event():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=8000)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Call the Gmail API
        service = build('calendar', 'v3', credentials=creds)

        calendar_id_booking = '6icigfdeq51qnhjar08kiuk9ck@group.calendar.google.com'

        # Refer to the Python quickstart on how to setup the environment:
        # https://developers.google.com/calendar/quickstart/python
        # Change the scope to 'https://www.googleapis.com/auth/calendar' and delete any
        # stored credentials.

        event = {
            'summary': 'Counselling Session',
            'location': 'Online',
            'description': 'A test event creation.',
            'status': 'confirmed',
            'transparency': 'transparent',
            'visibility': 'private',
            'maxAttendees': 3,
            'sendNotifications': True,
            'colorId': '2',

            'start': {
                'dateTime': '2022-04-28T09:00:00-07:00',
                'timeZone': 'Asia/Katmandu',
            },
            'end': {
                'dateTime': '2022-04-28T09:00:00-08:00',
                'timeZone': 'Asia/Katmandu',
            },
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=1'
            ],
            'attendees': [
                {"email": "guardian.cpc@gmail.com",
                "responseStatus": "accepted",
                "displayName": "Guardian",
                "organizer": True,},
                {'email': 'manishstha338@gmail.com'},
                {'email': 'rishi.shrestha101@gmail.com'},
            ],
            "hangoutLink": 'http://meet.google.com',
            "conferenceData": {
                "createRequest": {
                "requestId": 'sample123',
                "conferenceSolutionKey": {
                    "type": 'hangoutsMeet'
                },
                "status": {
                    "statusCode": 'success'
                }
                },
            },
            'reminders': {
                'useDefault': False,
                'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
                ],
            },
        }
        event = service.events().insert(calendarId=calendar_id_booking, body=event, conferenceDataVersion= 1).execute()
        print ('Event created: %s' % (event.get('htmlLink')))


        # request_body = {
        #     'summary': 'Booking',
        # }


        # to create a calendar

        # response = service.calendars().insert(body=request_body).execute()
        # print(response)

        # to delete calendar and id is needed to be changed
        # response = service.calendars().delete(calendarId='u0hj64f8itccgremcvv9ddr4n8@group.calendar.google.com').execute()

    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}')

