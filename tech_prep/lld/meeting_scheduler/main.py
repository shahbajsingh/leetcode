from models import MeetingRoom
from api import MeetingSchedulerAPI

def main():
    rooms = [MeetingRoom("Room A"), MeetingRoom("Room B"), MeetingRoom("Room C")]
    api = MeetingSchedulerAPI(rooms)

    attendees = [
        {"name": "Alice", "email": "alice@example.com"},
        {"name": "Bob", "email": "bob@example.com"} 
    ]

    # Book a meeting
    print(api.book_meeting("2025-03-01T10:00:00", "2025-03-01T11:00:00", attendees))

    # Check room availability
    print(api.check_availability("Room A", "2025-03-01T10:00:00", "2025-03-01T11:00:00"))

    # Get last 20 meetings
    print(api.get_meeting_history())

if __name__ == "__main__":
    main()
