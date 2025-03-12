from datetime import datetime
from scheduler import Scheduler
from models import MeetingRoom, Attendee
from email_service import EmailService

class MeetingSchedulerAPI:
    def __init__(self, rooms):
        self.scheduler = Scheduler(rooms)
        self.email_service = EmailService()
        
    def book_meeting(self, start: str, end: str, attendees_info: list):
        start_dt = datetime.fromisoformat(start)
        end_dt = datetime.fromisoformat(end) 
        attendees =  [Attendee(a['name'], a['email']) for a in attendees_info]
        
        for attendee in attendees:
            if not attendee.calendar.is_available(start_dt, end_dt):
                return {'Status: ': 'Failed', 'Reason: ': f'{attendee.name} is not available'}
            
        try:
            meeting = self.scheduler.book_meeting(start_dt, end_dt, attendees, self.email_service)
            return{'Status: ': 'Success', 'Meeting ID: ': meeting.id}
        except Exception as e:
            return {'Status: ': 'Failed', 'Reason: ': str(e)}
    
    def get_meeting_history(self):
        meetings = self.scheduler.get_meeting_history()
        return [{'Meeting ID: ': m.id, 'Room: ': m.room.name, 'Start: ': m.start.isoformat(), 'End: ': m.end.isoformat()} for m in meetings]
    
    def check_availability(self, room_name: str, start: str, end: str):
        start_dt = datetime.fromisoformat(start)
        end_dt = datetime.fromisoformat(end)
        is_available = self.scheduler.is_room_available(room_name, start_dt, end_dt)
        return {'Room: ': room_name, 'Available: ': is_available}