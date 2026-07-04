# AI Solutions & Automation Portfolio

This repository contains functional scripts and automated workflows designed to reduce manual operational hours, optimize business processes, and deploy AI-assisted data solutions.

## Featured Workflow: Automated Operations Calendar (`calendar_automation.py`)

### Business Problem
Manual scheduling of recurring operational checks, financial reviews, and team reminders consumes valuable administrative hours and is prone to human error (missed notifications, timezone misalignments).

### The Solution
A Python-based workflow that programmatically generates standard `.ics` files containing bulk, localized event data and forced offline push-notification triggers.

### Technical Specifications
* **Language:** Python 3
* **Libraries:** `icalendar`, `pytz`, `datetime`
* **Features:** * Automated bulk event generation across custom date ranges.
  * Strict timezone localization (Africa/Lagos) to resolve system import errors.
  * Integrated `vAlarm` components to force system-level push notifications regardless of the importing calendar client (Google Calendar, Outlook, Apple).

### Deployment
To run this calendar automation script locally, use the following commands:

```bash
# Clone the repository
git clone [https://github.com/TechBruv/AI-AUTOMATION.git](https://github.com/TechBruv/AI-AUTOMATION.git)

# Navigate into the directory
cd AI-AUTOMATION

# Install required dependencies
pip install icalendar pytz

# Execute the script
python calendar_automation.py
