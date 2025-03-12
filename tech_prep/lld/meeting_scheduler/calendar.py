from datetime import datetime

class Calendar:
    def __init__(self, owner):
        self.owner = owner
        self.meetings = []
    
    def add_meeting(self, meeting):
        self.meetings.append(meeting)
    
    def is_available(self,start: datetime, end: datetime) -> bool:
        for meeting in self.meetings:
            if not (meeting.end <= start or meeting.start >= end):
                return False
        return True
    
    def get_schedule(self):
        return [{'Room:': m.room.name, 'Start:': m.start.isoformat(), 'End:': m.end.isoformat()} for m in self.meetings]
