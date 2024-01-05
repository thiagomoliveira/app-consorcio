import pandas as pd
from entities.notification import Notification
from factories.notification_factory import create_notification
from utils.notification_validations import validate_notification_data
from utils.type_conversion import convert_date

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