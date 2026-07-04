import datetime
import pytz
from icalendar import Calendar, Event, vAlarm

def generate_reminder_calendar(start_date, end_date, output_filename="motivation_reminders.ics"):
    """
    Generates an .ics calendar file with hourly financial and motivational reminders.
    Handles strict timezone enforcement for West Africa Time (WAT).
    """
    cal = Calendar()
    cal.add('prodid', '-//BruntWork Automation Portfolio//babatunde//')
    cal.add('version', '2.0')
    
    # Set timezone to Nigeria (WAT)
    wat_tz = pytz.timezone("Africa/Lagos")
    current_time = wat_tz.localize(datetime.datetime.combine(start_date, datetime.time(9, 0)))
    end_time = wat_tz.localize(datetime.datetime.combine(end_date, datetime.time(17, 0)))

    # Alternating reminder messages
    messages = [
        "Focus Check: Execute high-priority tasks.",
        "Financial Review: Track daily metrics.",
        "System Check: Ensure all automated pipelines are running.",
        "Growth: Spend 15 minutes reviewing new AI workflows."
    ]

    event_count = 0
    
    while current_time < end_time:
        # Only schedule between 9 AM and 5 PM
        if 9 <= current_time.hour <= 17:
            event = Event()
            msg = messages[event_count % len(messages)]
            
            event.add('summary', msg)
            event.add('dtstart', current_time)
            event.add('dtend', current_time + datetime.timedelta(minutes=15))
            event.add('dtstamp', datetime.datetime.now(wat_tz))
            
            # Create an explicit alarm for the notification trigger
            alarm = vAlarm()
            alarm.add('action', 'DISPLAY')
            alarm.add('description', msg)
            alarm.add('trigger', datetime.timedelta(minutes=0)) 
            event.add_component(alarm)
            
            cal.add_component(event)
            event_count += 1
            
        current_time += datetime.timedelta(hours=1)

    # Write to file
    with open(output_filename, 'wb') as f:
        f.write(cal.to_ical())
        
    print(f"Success: {output_filename} generated with {event_count} automated events.")

if __name__ == "__main__":
    # Define deployment range (e.g., rest of 2026)
    start = datetime.date(2026, 7, 5)
    end = datetime.date(2026, 12, 31)
    
    generate_reminder_calendar(start, end)
