from django.shortcuts import render
from .form import Schedule_Meeting
from .models import Meeting
from account.models import Account, CounsellorDetail
import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# for calendar API
# from __future__ import print_function
from calendar import calendar
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']

@login_required(login_url='login')
def schedule_meeting(request, id):
    coun_email = Account.objects.get(id=id).email
    print(coun_email)
    counsellor_email = CounsellorDetail.objects.get(id=id).counsellor_email
    print(counsellor_email)
    current_user = request.user
    user_email = current_user.email
    print(user_email)
    # print(user_email)
    user_first_name = current_user.first_name
    user_last_name = current_user.last_name
    full_name = (user_first_name + " " + user_last_name)
    print(full_name)
    form = Schedule_Meeting()
    if request.method == 'POST':
        # get data from account mode
        form = Schedule_Meeting(request.POST)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            meeting_title = form.cleaned_data['meeting_title']
            client_age = form.cleaned_data['client_age']
            marital_status = form.cleaned_data['marital_status']
            meeting_date = form.cleaned_data['meeting_date']
            meeting_time = form.cleaned_data['meeting_time']
            # meeting_location = form.cleaned_data['meeting_location']
            meeting_description = form.cleaned_data['meeting_description']
            # meeting_created_by = form.cleaned_data['meeting_created_by']
            print(meeting_date)
            print(meeting_time)
            meet_schedule = Meeting(meeting_title=meeting_title, client_age=client_age, marital_status=marital_status,
                                    client_details=Account.objects.get(email=user_email), counsellor_details=Account.objects.get(email=coun_email), meeting_date=meeting_date, meeting_time=meeting_time, meeting_description=meeting_description)

            description = ('Meeting with ' + full_name + '\n Age : ' + str(client_age) +
                           ' \n Marital Status :' + marital_status + ' \n Description : ' + meeting_description + '.')
            p_start_time = datetime.datetime.combine(
                meeting_date, meeting_time)
            time_change = datetime.timedelta(minutes=75)
            p_end_time = p_start_time + time_change
            start_time = (str(p_start_time.strftime("%Y-%m-%dT%H:%M:%S")))
            end_time = (str(p_end_time.strftime("%Y-%m-%dT%H:%M:%S")))
            creds = None
            # The file token.json stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists('token.json'):
                creds = Credentials.from_authorized_user_file(
                    'token.json', SCOPES)
                print(creds)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'client_secret.json', SCOPES)
                    creds = flow.run_local_server(port=0)
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
                    'summary': meeting_title,
                    'location': 'Online',
                    'description': description,
                    'status': 'confirmed',
                    'transparency': 'transparent',
                    'visibility': 'private',
                    'maxAttendees': 3,
                    'sendNotifications': True,
                    'colorId': '2',

                    'start': {
                        'dateTime': start_time,
                        'timeZone': 'Asia/Kathmandu',
                    },
                    'end': {
                        'dateTime': end_time,
                        'timeZone': 'Asia/Kathmandu',
                    },
                    'recurrence': [
                        'RRULE:FREQ=DAILY;COUNT=1'
                    ],
                    'attendees': [
                        {"email": "guardian.cpc@gmail.com",
                         "responseStatus": "accepted",
                         "displayName": "Guardian",
                         "organizer": True, },
                        {'email': counsellor_email},
                        {'email': user_email},
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
                event = service.events().insert(calendarId=calendar_id_booking,
                                                body=event, conferenceDataVersion=1).execute()
                print('Event created: %s' % (event.get('htmlLink')))
                event_link = event.get('htmlLink'),
                context = {
                    'event_link': event_link,
                }

                messages.success(request, "Successfully booked!")
                meet_schedule.save()
                return render(request, 'counsellor.html', context)

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
                return(print(f'An error occurred: {error}'))

    else:
        form = Schedule_Meeting()

    context = {
        'form': form,
    }
    return render(request, 'booking/book_meeting.html', context)


def create_event(meeting_title, start_time, end_time, description, counsellor_email, user_email):
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        print(creds)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
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
            'summary': meeting_title,
            'location': 'Online',
            'description': description,
            'status': 'confirmed',
            'transparency': 'transparent',
            'visibility': 'private',
            'maxAttendees': 3,
            'sendNotifications': True,
            'colorId': '2',

            'start': {
                'dateTime': start_time,
                'timeZone': 'Asia/Kathmandu',
            },
            'end': {
                'dateTime': end_time,
                'timeZone': 'Asia/Kathmandu',
            },
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=1'
            ],
            'attendees': [
                {"email": "guardian.cpc@gmail.com",
                 "responseStatus": "accepted",
                 "displayName": "Guardian",
                 "organizer": True, },
                {'email': counsellor_email},
                {'email': user_email},
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
        event = service.events().insert(calendarId=calendar_id_booking,
                                        body=event, conferenceDataVersion=1).execute()
        print('Event created: %s' % (event.get('htmlLink')))
        event_link = event.get('htmlLink')
        status = "success"
        return(event_link, status)

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
        return(print(f'An error occurred: {error}'))
