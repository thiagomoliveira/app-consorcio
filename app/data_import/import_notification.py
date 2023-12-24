import pandas as pd
from entities.invalid_notification import InvalidNotification
from factories.notification_factory import create_notification

def import_notification(file_path):
    df = pd.read_excel(file_path)
    valid_notifications = []
    invalid_notifications = []
    for _, row in df.iterrows():
        notification = create_notification(row)
        if isinstance(notification, InvalidNotification):
            invalid_notifications.append(notification)
        else:
            valid_notifications.append(notification)

    return valid_notifications, invalid_notifications
