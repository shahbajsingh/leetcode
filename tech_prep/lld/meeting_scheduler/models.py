from datetime import datetime
from calendar import Calendar
from email_service import EmailService

class MeetingRoom:
    def __init__(self, name):
        self.name = name
        self.calendar = []
    
    def is_available(self, start: datetime, end: datetime) -> bool:
        for meeting in self.calendar:
            if not (meeting.end <= start or meeting.start >= end):
                return False
        return True
    
    def book_meeting(self, meeting):
        self.calendar.append(meeting)
        
class Meeting:
    id_counter = 1
    
    def __init__(self, room, start: datetime, end: datetime, attendees=None):
        self.id = Meeting.id_counter
        Meeting.id_counter += 1
        self.room = room
        self.start = start
        self.end = end
        self.attendees = attendees if attendees else []
        
    def invite(self, email_service):
        subject = f'Meeting Scheduled in Room {self.room.name}'
        body = f'Your meeting is scheduled from {self.start} to {self.end}'
        for attendee in self.attendees:
            attendee.calendar.add_meeting(self)
            email_service.send_email(attendee.email, subject, body)
            
class Attendee:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.calendar = Calendar(self)
        
    def notify(self, meeting):
        print(f'Notification sent to {self.name} ({self.email} for meeting in Room {meeting.room.name} from {meeting.start} to {meeting.end})')