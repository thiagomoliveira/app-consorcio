import pandas as pd
from entities.notification import Notification
from factories.notification_factory import create_notification

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