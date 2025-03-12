from models import MeetingRoom, Meeting
from collections import deque
from datetime import datetime
from email_service import EmailService

class Scheduler:
    MAX_HISTORY = 20
    
    def __init__(self, meeting_rooms):
        self.meeting_rooms = meeting_rooms
        self.history = deque(maxlen=self.MAX_HISTORY)
        
    
    def book_meeting(self, start: datetime, end: datetime, attendees=None, email_service=None):
        for room in self.meeting_rooms:
            if room.is_available(start, end):
                meeting = Meeting(room, start, end, attendees)
                room.book_meeting(meeting)
                self.history.append(meeting)
                if attendees and email_service:
                    meeting.invite(email_service)
                return meeting
        raise Exception('No meeting rooms available.')
    
    def get_meeting_history(self):
        return list(self.history)
    
    def is_room_available(self, room_name: str, start: datetime, end: datetime) -> bool:
        for room in self.meeting_rooms:
            if room.name == room_name:
                return room.is_available(start, end)
        return False