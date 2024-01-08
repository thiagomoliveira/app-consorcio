import pandas as pd
from entities.notification import Notification
from factories.notification_factory import create_notification
from utils.notification_validations import validate_notification_data
from utils.type_conversion import convert_date
from sqlalchemy import and_
import calendar

def add_notifications_to_database(session, notifications):
    try:
        # Add each valid notification to the session
        for notification in notifications:
            session.add(notification)
    except Exception as e:
        # In case of an error, error handling and rollback should be done externally
        print(f"Error preparing notifications for addition: {e}")
        raise

def import_notifications_from_excel(file_path):
    df = pd.read_excel(file_path)
    valid_notifications = []
    invalid_notifications = []
    for _, row in df.iterrows():
        notification = create_notification(row)
        if notification.is_valid:
            valid_notifications.append(notification)
        else:
            invalid_notifications.append(notification)

    return valid_notifications, invalid_notifications

def revalidate_notification(self):
        self.is_valid, self.errors = validate_notification_data(
            self.group, self.quota, self.send_date, self.return_date, self.return_type,
            self.office, self.state, self.registry_office, self.name, self.contract, self.justification
        )

        if self.is_valid:
            self.send_date = convert_date(self.send_date)
            self.return_date = convert_date(self.return_date)
            return {"status": "success", "message": "Notification successfully validated."}
        else:
            return {"status": "error", "message": "Validation errors found.", "errors": self.errors}
        
def filter_notifications_by_date(query, start_date=None, end_date=None, granularity='daily'):
    if start_date:
        start_date = convert_date(start_date)

    if end_date:
        end_date = convert_date(end_date)
        if granularity == 'monthly':

            last_day = calendar.monthrange(end_date.year, end_date.month)[1]
            end_date = end_date.replace(day=last_day)

    date_filters = []
    if start_date:
        date_filters.append(Notification._send_date >= start_date)
    if end_date:
        date_filters.append(Notification._send_date <= end_date)

    return query.filter(and_(*date_filters))

def filter_notifications_by_state(query, states=None):
    if states:
        return query.filter(Notification._state.in_(states))
    return query